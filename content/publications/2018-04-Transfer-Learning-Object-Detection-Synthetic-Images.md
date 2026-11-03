---
title: "Transfer Learning by Finetuning Pretrained CNNs Entirely with Synthetic Images"
collection: publications
permalink: /publication/2018-04-Transfer-Learning-Object-Detection-Synthetic-Images
excerpt: 'This paper discusses our approach of transferring the learned object detection features trained entirely on Synthetic Images and tested on Real Images, which show significant performance improvements, along with easily generatable huge data for Deep Neural Networks.'
date: 2018-04-26
venue: 'Proceeding of the National Conference on Computer Vision, Pattern Recognition, Image Processing, and Graphics NCVPRIPG 2017 in CCIS, vol 841 Series of Springer, Singapore'
link: 'https://link.springer.com/chapter/10.1007/978-981-13-0020-2_45'
paperurl: 'https://link.springer.com/content/pdf/10.1007/978-981-13-0020-2_45.pdf?pdf=inline%20link'
citation: 'Rajpura P. et al. (2018) Transfer Learning by Finetuning Pretrained CNNs Entirely with Synthetic Images. In: Rameshan R., Arora C., Dutta Roy S. (eds) Computer Vision, Pattern Recognition, Image Processing, and Graphics. NCVPRIPG 2017. Communications in Computer and Information Science, vol 841. Springer, Singapore'
---

# Abstract

We show that finetuning pretrained CNNs entirely on synthetic images is an effective strategy to achieve transfer learning. We apply this strategy for detecting packaged food products clustered in refrigerator scenes. A CNN pretrained on the COCO dataset and fine-tuned with our 4000 synthetic images achieves mean average precision (mAP @ 0.5-IOU) of 52.59 on a test set of real images (150 distinct products as objects of interest and 25 distractor objects) in comparison to a value of 24.15 achieved without such finetuning. The synthetic images were rendered with freely available 3D models with variations in parameters like color, texture and viewpoint without a high emphasis on photorealism. We analyze factors like training data set size, cue variances, 3D model dictionary size and network architecture for their influence on the transfer learning performance. Additionally, training strategies like fine-tuning with selected layers and early stopping which affect transfer learning from synthetic scenes to real scenes were explored. This approach is promising in scenarios where limited training data is available.
