---
title: "Masked Autoencoders Are Scalable Vision Learners"
abstract: "This paper shows that masked autoencoders (MAE) are scalable self-supervised learners for computer vision. Our MAE approach is simple: we mask random patches of the input image and reconstruct the missing pixels. It is based on two core designs. First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that reconstructs the original image from the latent representation and mask tokens. Second, we find that masking a high proportion of the input image, e.g., 75%, yields a nontrivial and meaningful self-supervisory task. Coupling these two designs enables us to train large models efficiently and effectively: we accelerate training (by 3x or more) and improve accuracy. Our scalable approach allows for learning high-capacity models that generalize well: e.g., a vanilla ViT-Huge model achieves the best accuracy (87.8%) among methods that use only ImageNet-1K data. Transfer performance in downstream tasks outperforms supervised pre-training and shows promising scaling behavior."
summary: "This paper shows that masked autoencoders (MAE) are scalable self-supervised learners for computer vision."
location: Online (Zoom)
date: 2023-01-11T12:00:00.000Z
date_end: 2023-01-11T12:30:00.000Z
all_day: false
links:
  - url: https://openaccess.thecvf.com/content/CVPR2022/papers/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper.pdf
    name: "PDF"
event: EMIL Spring'23 Seminars
event_url: " "
publishDate: 2023-01-11T20:56:00.000Z
draft: false
featured: false
authors:
  - abdullah-mamun
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
