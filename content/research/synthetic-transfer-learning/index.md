---
title: "Transfer Learning with Synthetic Images"
summary: "NCVPRIPG 2017, Springer, 100+ citations. Fine-tuning an object detector only on rendered images more than doubled its accuracy on real photos."
date: 2018-04-26
aliases:
  - "/publication/2018-04-Transfer-Learning-Object-Detection-Synthetic-Images/"
---
**Transfer Learning by Finetuning Pretrained CNNs Entirely with Synthetic Images**\
Param S. Rajpura, **Alakh Aggarwal**, Manik Goyal, Sanchit Gupta, Jonti Talukdar, Hristo Bojinov, Ravi S. Hegde\
*NCVPRIPG 2017*, Springer CCIS vol. 841, 2018. 100+ citations.

<div class="not-prose" style="display:flex;flex-wrap:wrap;gap:.75rem;margin:1.25rem 0">
{{< button href="https://link.springer.com/chapter/10.1007/978-981-13-0020-2_45" target="_blank" >}}Paper{{< /button >}}
{{< button href="https://arxiv.org/abs/1706.06782" target="_blank" >}}arXiv{{< /button >}}
</div>

Fine-tuning a pretrained object detector only on rendered images of grocery products more than doubled its accuracy on real refrigerator photos (mAP 24.15 → 52.59).

## Method

{{< figure src="fig1-overview.png" alt="Pipeline: 3D object and refrigerator models rendered in Blender into annotated scenes, used to fine-tune a CNN that then detects objects in real photos" caption="3D models of products and a refrigerator are rendered into annotated scenes, and a pretrained detector is fine-tuned on them alone. (Fig. 1 in the paper.)" >}}

{{< figure src="fig2-training-data.png" alt="ShapeNet product models, rendered refrigerator scenes, and real refrigerator photos" caption="(a) Some of the 3D product models. (b) Rendered training scenes with varied textures, materials, packing and camera angles; photorealism was not the goal. (c) Real refrigerator photos used for testing. (Fig. 2 in the paper.)" >}}

## Results

{{< figure src="fig8-detections.png" alt="Detections on real refrigerator photos across three rows" caption="Detections on real photos. Top row: every object of interest is found. Middle row: some objects are missed. Bottom row: the detector reports objects that are not there. (Fig. 8 in the paper.)" >}}

## Abstract

We show that finetuning pretrained CNNs entirely on synthetic images is an effective strategy to achieve transfer learning. We apply this strategy for detecting packaged food products clustered in refrigerator scenes. A CNN pretrained on the COCO dataset and fine-tuned with our 4000 synthetic images achieves mean average precision (mAP @ 0.5-IOU) of 52.59 on a test set of real images (150 distinct products as objects of interest and 25 distractor objects) in comparison to a value of 24.15 achieved without such finetuning. The synthetic images were rendered with freely available 3D models with variations in parameters like color, texture and viewpoint without a high emphasis on photorealism. We analyze factors like training data set size, cue variances, 3D model dictionary size and network architecture for their influence on the transfer learning performance. Additionally, training strategies like fine-tuning with selected layers and early stopping which affect transfer learning from synthetic scenes to real scenes were explored. This approach is promising in scenarios where limited training data is available.

## Citation

```bibtex
@inproceedings{rajpura2018transfer,
  title     = {Transfer Learning by Finetuning Pretrained CNNs Entirely with Synthetic Images},
  author    = {Rajpura, Param S. and Aggarwal, Alakh and Goyal, Manik and Gupta, Sanchit and Talukdar, Jonti and Bojinov, Hristo and Hegde, Ravi S.},
  booktitle = {Computer Vision, Pattern Recognition, Image Processing, and Graphics (NCVPRIPG 2017)},
  series    = {Communications in Computer and Information Science},
  volume    = {841},
  pages     = {517--528},
  publisher = {Springer},
  year      = {2018},
  doi       = {10.1007/978-981-13-0020-2_45}
}
```
