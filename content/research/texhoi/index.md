---
title: "TexHOI"
summary: "IEEE TVCG (CVM 2025), Best Paper Award. Reconstructs the shape and true surface color of an unknown object from a single video of a hand handling it."
weight: 1
aliases: ["/publication/2024-TexHOI/"]
---
**TexHOI: Reconstructing Textures of 3D Unknown Objects in Monocular Hand-Object Interaction Scenes**
Alakh Aggarwal, Ningna Wang, Xiaohu Guo. *IEEE TVCG (CVM 2025).* **Best Paper Award.**

{{< button href="https://alakhag.github.io/TexHOI-website/" target="_blank" >}}Project page{{< /button >}}
{{< button href="https://arxiv.org/abs/2501.03525" target="_blank" >}}Paper{{< /button >}}
{{< button href="https://github.com/alakhag/TexHOI" target="_blank" >}}Code{{< /button >}}

Reconstructs the shape and true surface color of an unknown object from a single video of a hand handling it. It accounts for the shadows and reflected light the hand casts on the object.

## Abstract
Reconstructing 3D models of dynamic, real-world objects with high-fidelity textures from monocular frame sequences has been a challenging problem in recent years. This difficulty stems from factors such as shadows, indirect illumination, and inaccurate object-pose estimations due to occluding hand-object interactions. To address these challenges, we propose a novel approach that predicts the hand’s impact on environmental visibility and indirect illumination on the object's surface albedo. Our method first learns the geometry and low-fidelity texture of the object, hand, and background through composite rendering of radiance fields. Simultaneously, we optimize the hand and object poses to achieve accurate object-pose estimations. We then refine physics-based rendering parameters—including roughness, specularity, albedo, hand visibility, skin color reflections, and environmental illumination—to produce precise albedo, and accurate hand illumination and shadow regions. Our approach surpasses state-of-the-art methods in texture reconstruction and, to the best of our knowledge, is the first to account for hand-object interactions in object texture reconstruction.
