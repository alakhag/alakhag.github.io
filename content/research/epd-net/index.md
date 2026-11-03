---
title: "EPD-Net"
summary: "IEEE IEMTRONICS 2020. A GAN that hides who is in a face image while keeping expression and other non-identifying information."
date: 2020-09-09
aliases:
  - "/publication/2019-DeID/"
---
**EPD-Net: A GAN-based Architecture for Face De-identification from Images**\
**Alakh Aggarwal**, Rishika Rathore, Pratik Chattopadhyay, Lipo Wang\
*IEEE International IOT, Electronics and Mechatronics Conference* (IEMTRONICS), 2020.

<div class="not-prose" style="display:flex;flex-wrap:wrap;gap:.75rem;margin:1.25rem 0">
{{< button href="https://ieeexplore.ieee.org/abstract/document/9216358" target="_blank" >}}Paper{{< /button >}}
{{< button href="https://personal.ntu.edu.sg/elpwang/PDF_web/2020_face_de_id_conf.pdf" target="_blank" >}}PDF{{< /button >}}
</div>

A GAN that hides who is in a face image while keeping the expression and other non-identifying information, for sharing surveillance footage without exposing identities.

## Results

{{< figure src="fig3-results.png" alt="Five face images from the RaFD dataset and their de-identified versions" caption="Top: faces from the RaFD dataset. Bottom: EPD-Net's de-identified outputs, which change who the person appears to be while keeping the expression. (Fig. 3 in the paper.)" >}}

## Method

{{< figure src="fig2-architecture.png" alt="EPD-Net architecture: U-Net generator and PatchGAN discriminator with SSIM loss, plus identity and emotion verificators" caption="A structure-preserving GAN (U-Net generator, PatchGAN discriminator with SSIM loss) trained against two verifiers: one pushes identity away from the input, the other keeps the emotion. (Fig. 2 in the paper.)" >}}

## Abstract

Nowadays huge amount of crowd data captured by surveillance cameras gets shared publicly in the form of images or videos through television or the internet. Although many of these videos are meant to provide public security, they also lead to a widespread concern towards privacy protection, since a lot of personal information about subjects gets revealed through this video/image data. Hence, "de-identifying" people (i.e., obscuring identity information) captured by the surveillance cameras is of utmost importance for providing privacy along with security. Traditional identity obfuscation techniques such as blurring, warping, and filtering lead to the loss of vital non-biometric information. More recent k-same-based as well as generative model-based de-identification techniques eliminate the above problem to a certain extent. Still, the visual quality of the generated images produced by these methods is not realistic. Also, these approaches are unable to maintain structural integrity and cannot preserve the required non-biometric information at a high resolution. As an improvement, in this paper, we propose a new network termed as EPD-Net and train it with suitable loss functions to maximize the emotion similarity and minimize the identity similarity. Experimental results verify the effectiveness of our approach and its superiority over other popular face de-identification techniques.

## Citation

```bibtex
@inproceedings{aggarwal2020epdnet,
  title     = {EPD-Net: A GAN-based Architecture for Face De-identification from Images},
  author    = {Aggarwal, Alakh and Rathore, Rishika and Chattopadhyay, Pratik and Wang, Lipo},
  booktitle = {2020 IEEE International IOT, Electronics and Mechatronics Conference (IEMTRONICS)},
  pages     = {1--7},
  year      = {2020}
}
```
