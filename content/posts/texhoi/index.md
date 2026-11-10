---
title: "TexHOI: Seeing an Object's True Color When a Hand Is Holding It"
date: 2026-11-10
url: /posts/texhoi/
summary: "A hand holding an object casts shadows on it and bounces skin-colored light onto it. Reconstruction methods bake both into the texture. TexHOI models the hand's effect on lighting so it can be removed."
tags:
    - research
    - 3d-vision
    - inverse-rendering
---
{{< katex >}}

Pick up a mug and look at it. Your fingers cast small shadows on it, and the side facing your palm picks up a faint warm tint from your skin. You don't notice either, because your brain separates "the mug's color" from "how the mug is lit right now."

A 3D reconstruction method doesn't make that separation for free. Give it a video of a hand turning an object, and it will often produce a texture with dark finger-shaped smudges and a skin-colored cast painted into it. The shadow becomes part of the object.

[TexHOI](/research/texhoi/) is my paper on fixing this, with Ningna Wang and Xiaohu Guo at UT Dallas. It was published in IEEE TVCG (CVM 2025), where it won the Best Paper Award. This post explains the problem and the idea, without the full paper's detail.

## Color vs appearance

What a camera records at a pixel is not the object's color. It is the object's color *after* lighting has been applied. The rendering equation makes this explicit (I wrote about it [here](/posts/sg-render/)):

$$
R(o) = \int_{S^2} L(i)\, V(i)\, \rho_o(i)\, \max(0, i \cdot n)\, di
$$

The quantity we want is the **albedo**, inside the BRDF $\rho_o$: the color the surface would have under perfectly even white light. Everything else in the integral is about the scene. $L(i)$ is how much light arrives from direction $i$, and $V(i)$ says whether that direction is blocked.

Recovering albedo from photos is called *inverse rendering*: you fit the albedo, the lighting and the visibility so that rendering them reproduces the images. If you get the lighting or the visibility wrong, the error has to go somewhere, and it goes into the albedo.

## What the hand changes

In hand-object video the hand breaks two of the usual assumptions.

**The hand blocks light.** $V(i)$ is no longer only about the object shadowing itself. Fingers block parts of the sky for each point on the surface, and they move every frame.

**The hand adds light.** Skin reflects light back onto the object. That is extra *indirect* illumination, tinted by skin color, that a model of the environment light alone can't explain.

There is also a third problem upstream: the hand hides parts of the object, so the object's pose in each frame is harder to estimate. A texture fitted with slightly wrong poses comes out blurry, however good the lighting model is.

## The idea: model the hand, then subtract it

TexHOI works in two stages.

**Stage 1: get the geometry and poses right.** Three neural radiance fields model the hand, the object and the background, and their outputs are composited along each camera ray. The hand and object poses are optimized jointly with the fields. This stage gives the object's shape, accurate per-frame poses, and a mask showing where the object is actually visible.

**Stage 2: separate color from lighting.** With geometry fixed, the method switches to physics-based rendering:

- **Environment light** is a mixture of 128 spherical Gaussians (see [this post](/posts/sg/) for what those are).
- **Material** is a small network predicting albedo and roughness at each surface point.
- **Hand visibility** is the key part. The hand is approximated by 108 spheres attached to a parametric hand model, so they move and resize with the hand's pose and shape. For each point on the object, the method computes how much of each light lobe the spheres block, using a closed-form approximation for spherical Gaussians from Iwasaki et al. No ray tracing is needed.
- **Skin bounce** is a learned indirect-light term, initialized to a skin tone and added where the hand occludes the object.

Because the shadows and the skin tint are now explained by the hand, the optimizer no longer needs to paint them into the albedo.

## A toy version of the visibility idea

Spheres are a good choice because the question "does this sphere block this direction?" has an exact answer. Seen from a point, a sphere of radius $r$ whose center is distance $d$ away covers a cone of half-angle $\arcsin(r/d)$. A direction is blocked if it falls inside that cone.

```python
import numpy as np

def blocked(x, light_dirs, centers, radii):
    """True where a ray from surface point x toward a light direction hits any sphere."""
    hit = np.zeros(len(light_dirs), dtype=bool)
    for c, r in zip(centers, radii):
        to_c = c - x
        dist = np.linalg.norm(to_c)
        cos_cone = np.sqrt(max(0.0, 1 - (r / dist) ** 2))   # sphere's angular radius
        hit |= light_dirs @ (to_c / dist) > cos_cone
    return hit

rng = np.random.default_rng(0)
dirs = rng.normal(size=(100_000, 3))
dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
dirs = dirs[dirs[:, 2] > 0]                               # upper hemisphere (normal = +z)

x = np.zeros(3)                                           # a point on the object
finger = [np.array([0.0, 0.0, 0.03])], [0.01]             # a 1 cm "finger" sphere, 3 cm away
print(f"{blocked(x, dirs, *finger).mean():.1%}")          # 5.8%
finger = [np.array([0.0, 0.0, 0.10])], [0.01]             # the same finger, 10 cm away
print(f"{blocked(x, dirs, *finger).mean():.1%}")          # 0.5%
```

Move one fingertip from 10 cm to 3 cm and it blocks over ten times more of the sky. That is why hand shadows are so strong where fingers touch the object. TexHOI does the same calculation for all 108 spheres, against spherical Gaussian lobes instead of sampled directions, in every frame.

## Results

On six textured objects from the HO3D dataset, TexHOI was compared with HOLD and with InvRender, measured against ground-truth textures:

| Method | PSNR ↑ | SSIM ↑ | LPIPS ↓ |
|---|---|---|---|
| InvRender | 19.23 | 0.9301 | 0.154 |
| HOLD | 20.61 | 0.9354 | 0.101 |
| **TexHOI** | **20.96** | **0.9387** | **0.095** |

The averages are best on all three metrics, but not every object wins. HOLD scores a higher PSNR on three of the six objects. Pixel metrics partly reward a texture that matches the images, shadows included, so the visual comparison tells the story better:

{{< figure src="/research/texhoi/fig7-comparison.png" alt="Input frames and reconstructions by InvRender, HOLD and TexHOI for six hand-held objects" caption="TexHOI's albedo avoids the hand shadows and lighting that other methods bake into the texture. (Fig. 7 in the paper.)" >}}

Once color and lighting are separated, the object can be relit under a new environment, which you can't do with a texture that has shadows painted in:

{{< figure src="/research/texhoi/fig9-relighting.png" alt="A kettle held by a hand, reconstructed by TexHOI and relit under different environment maps" caption="A reconstructed kettle relit under different environments. (Fig. 9 in the paper.)" >}}

## Limitations

- If the hand never moves relative to the object, its imprint still gets baked in. The method needs the hand to shift so it can tell shadow from surface.
- Spheres near the fingertips can slightly penetrate the object, which causes small errors in the occlusion.
- It handles a single right hand, and the two stages are optimized separately, not jointly.
- Skin bounce is a single learned term, not a full model of skin reflectance.

## Why it matters

Hand-held capture is how most people would naturally scan an object: pick it up and turn it in front of a phone. If reconstruction can't handle the hand, you either need a turntable or you get a texture with fingers in it. TexHOI was, as far as we know, the first method to account for hand-object interaction in object texture reconstruction.

This research can be further used with Gaussian splats. Along with inpainting methods (including diffusion-based inpainting), the geometric shape can be extracted even in scenarios of heavy hand occlusion on the object.

## Links

- Paper: [arXiv 2501.03525](https://arxiv.org/abs/2501.03525) · [IEEE TVCG](https://doi.org/10.1109/TVCG.2025.3567276)
- Code: [github.com/alakhag/TexHOI](https://github.com/alakhag/TexHOI)
- Talk: [YouTube](https://youtu.be/G6iyfrgBCbI)
- Background on this blog: [Spherical Gaussians](/posts/sg/) and [rendering with them](/posts/sg-render/)

*Previously: [The pinhole camera](/posts/pinhole-camera/). Next week: Foundations of 3D Vision, Part 2: homogeneous coordinates.*
