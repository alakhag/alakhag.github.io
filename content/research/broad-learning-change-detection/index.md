---
title: "Broad Neural Network for Change Detection"
summary: "IEMGraph 2018, Springer. My part: a Broad Learning System that keeps adding its own enhancement layers until accuracy stops improving, applied to finding changed pixels in aerial images."
date: 2019-07-17
aliases:
  - "/publication/2019-07-17-Broad-Neural-Network-Change-Detection/"
---
**Broad Neural Network for Change Detection in Aerial Images**\
Shailesh Shrivastava, **Alakh Aggarwal**, Pratik Chattopadhyay\
*Emerging Technology in Modelling and Graphics* (IEMGraph 2018), Springer AISC vol. 937, 2020.

<div class="not-prose" style="display:flex;flex-wrap:wrap;gap:.75rem;margin:1.25rem 0">
{{< button href="https://link.springer.com/chapter/10.1007/978-981-13-7403-6_31" target="_blank" >}}Paper{{< /button >}}
{{< button href="https://arxiv.org/abs/1903.00087" target="_blank" >}}arXiv{{< /button >}}
</div>

**My part was the classifier:** a Broad Learning System that keeps adding layers of enhancement nodes, each compressed with a sparse autoencoder, and stops once the cross-validated F-score stops improving. My co-author Shailesh Shrivastava applied it to detecting which pixels changed between two aerial images of the same place, where it beat a multilayer perceptron on F-score.

## Method

{{< figure src="architecture.png" alt="Broad Learning architecture: input layer, enhancement nodes added recursively, all concatenated into the output layer" caption="The Broad Learning System: new layers of enhancement nodes are added one at a time, then the input and all enhancement layers are concatenated and connected to the output by a single weight matrix W. (Fig. 2 in the paper.)" >}}

## Results

{{< figure src="results.jpg" alt="Two aerial images of the same place, the ground-truth change mask, and the predicted change map" caption="Top: two aerial images of the same place taken at different times. Bottom: the ground-truth change mask (left) and the map predicted by the Broad Learning classifier (right), with a 10:1 class imbalance. (Fig. 3 in the paper.)" >}}

## Abstract

A change detection system takes as input two images of a region captured at two different times and predicts which pixels in the region have undergone change over the time period. Since pixel-based analysis can be erroneous due to noise, illumination difference and other factors, contextual information is usually used to determine the class of a pixel (changed or not). This contextual information is taken into account by considering a pixel of the difference image along with its neighborhood. With the help of ground truth information, the labeled patterns are generated. Finally, Broad Learning classifier is used to get prediction about the class of each pixel. Results show that Broad Learning can classify the data set with a significantly higher F-score than that of Multilayer Perceptron. Performance comparison has also been made with other popular classifiers, namely Multilayer Perceptron and Random Forest.

## Citation

```bibtex
@inproceedings{shrivastava2020broad,
  title     = {Broad Neural Network for Change Detection in Aerial Images},
  author    = {Shrivastava, Shailesh and Aggarwal, Alakh and Chattopadhyay, Pratik},
  booktitle = {Emerging Technology in Modelling and Graphics},
  series    = {Advances in Intelligent Systems and Computing},
  volume    = {937},
  publisher = {Springer},
  year      = {2020},
  doi       = {10.1007/978-981-13-7403-6_31}
}
```
