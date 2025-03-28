---
title: "DeepFood: Food Image Analysis and Dietary
Assessment via Deep Model"
abstract: "Food image classification is challenging for real-world applications since existing methods require static datasets for training and are not capable of learning from sequentially available new food images. Online continual learning aims to learn new classes from data stream by using each new data only once without forgetting the previously learned knowledge. However, none of the existing works target food image analysis, which is more difficult to learn incrementally due to its high intra-class variation with the unbalanced and unpredictable characteristics of future food class distribution. In this paper, we address these issues by introducing (1) a novel clustering based exemplar selection algorithm to store the most representative data belonging to each learned food for knowledge replay, and (2) an effective online learning regime using balanced training batch along with the knowledge distillation on augmented exemplars to maintain the model performance on all learned classes. Our method is evaluated on a challenging large scale food image database, Food-1K1 , by varying the number of newly added food classes. Our results show significant improvements compared with existing state-of-the-art online continual learning methods, showing great potential to achieve lifelong learning for food image classification in real world."

summary: "The paper proposes an online continual learning method for food image classification, using clustering-based exemplar selection and balanced training with knowledge distillation. It outperforms existing methods on the Food-1K dataset."

location: Online (Zoom)
date: 2025-03-20T12:00:00.000Z
date_end: 2025-03-20T12:30:00.000Z
all_day: false
links:
  - url: https://arxiv.org/pdf/2108.06781
    name: "Paper"
  - url: pres.pptx
    name: "slides"
event: EMIL Spring'25 Seminars
event_url: " "
publishDate: 2025-03-28T14:45:00.000Z
draft: false
featured: false
authors:
  - reza-rahimi-azghan
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
