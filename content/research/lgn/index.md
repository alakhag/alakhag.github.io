---
title: "Layered-Garment Net"
summary: "ACCV 2022, with Samsung Research America. From one photo of a person, rebuilds each layer of clothing as separate 3D surfaces that never pass through each other."
date: 2022-12-04
aliases:
  - "/publication/2022-LGN/"
---
**Layered-Garment Net: Generating Multiple Implicit Garment Layers from a Single Image**\
**Alakh Aggarwal**, Jikai Wang, Steven Hogue, Saifeng Ni, Madhukar Budagavi, Xiaohu Guo\
*Asian Conference on Computer Vision* (ACCV), 2022. With Samsung Research America.

<div class="not-prose" style="display:flex;flex-wrap:wrap;gap:.75rem;margin:1.25rem 0">
{{< button href="https://openaccess.thecvf.com/content/ACCV2022/html/Aggarwal_Layered-Garment_Net_Generating_Multiple_Implicit_Garment_Layers_from_a_Single_ACCV_2022_paper.html" target="_blank" >}}Paper{{< /button >}}
{{< button href="https://openaccess.thecvf.com/content/ACCV2022/papers/Aggarwal_Layered-Garment_Net_Generating_Multiple_Implicit_Garment_Layers_from_a_Single_ACCV_2022_paper.pdf" target="_blank" >}}PDF{{< /button >}}
{{< button href="https://github.com/alakhag/lgn" target="_blank" >}}Code{{< /button >}}
{{< button href="https://youtu.be/p5t40mSCwZU" target="_blank" >}}Talk{{< /button >}}
</div>

From one photo of a person, it rebuilds each layer of clothing (a shirt under a jacket, over trousers) as separate 3D surfaces that never pass through each other.

## Talk

{{< youtubeLite id="p5t40mSCwZU" >}}

## Method

{{< figure src="method.jpg" alt="LGN pipeline: garment segmentation, masks, pixel-aligned implicit SDF and garment indication field networks, and layer-wise reconstruction" caption="From a single image, LGN predicts a signed distance field for each garment layer plus a garment indication field that keeps outer layers covering inner ones without intersecting." >}}

## Results

{{< figure src="comparison.jpg" alt="Two input photos with reconstructions by BCNet, SMPLicit and LGN" caption="Compared with BCNet and SMPLicit, LGN keeps the inner shirt under the jacket without the layers passing through each other. BCNet cannot model a jacket over a shirt." >}}

{{< figure src="multiview.jpg" alt="Three input photos and multi-view reconstructions by LGN, SMPLicit and BCNet" caption="Multi-view reconstructions on three people: LGN (left), SMPLicit (middle), BCNet (right)." >}}

## Abstract

Recent research works have focused on generating human models and garments from their 2D images. However, state-of-the-art researches focus either on only a single layer of the garment on a human model or on generating multiple garment layers without any guarantee of the intersection-free geometric relationship between them. In reality, people wear multiple layers of garments in their daily life, where an inner layer of garment could be partially covered by an outer one. In this paper, we try to address this multi-layer modeling problem and propose the Layered-Garment Net (LGN) that is capable of generating intersection-free multiple layers of garments defined by implicit function fields over the body surface, given the person's near front-view image. With a special design of garment indication fields (GIF), we can enforce an implicit covering relationship between the signed distance fields (SDF) of different layers to avoid self-intersections among different garment surfaces and the human body. Experiments demonstrate the strength of our proposed LGN framework in generating multi-layer garments as compared to state-of-the-art methods. To the best of our knowledge, LGN is the first research work to generate intersection-free multiple layers of garments on the human body from a single image.

## Citation

```bibtex
@inproceedings{aggarwal2022lgn,
  title     = {Layered-Garment Net: Generating Multiple Implicit Garment Layers from a Single Image},
  author    = {Aggarwal, Alakh and Wang, Jikai and Hogue, Steven and Ni, Saifeng and Budagavi, Madhukar and Guo, Xiaohu},
  booktitle = {Proceedings of the Asian Conference on Computer Vision (ACCV)},
  pages     = {3000--3017},
  year      = {2022}
}
```
