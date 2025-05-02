---
title: "A Time Series is Worth 64 Words: Long-term Forecasting with Transformers"
abstract: "We propose an efficient design of Transformer-based models for multivariate time series forecasting and self-supervised representation learning. It is based on two key components: (i) segmentation of time series into subseries-level patches which are served as input tokens to Transformer; (ii) channel-independence where each channel contains a single univariate time series that shares the same embedding and Transformer weights across all the series. Patching design naturally has three-fold benefit: local semantic information is retained in the embedding; computation and memory usage of the attention maps are quadratically reduced given the same look-back window; and the model can attend longer history. Our channel-independent patch time series Transformer (PatchTST) can improve the long-term forecasting accuracy significantly when compared with that of SOTA Transformer-based models. We also apply our model to self-supervised pretraining tasks and attain excellent fine-tuning performance, which outperforms supervised training on large datasets. Transferring of masked pre-trained representation on one dataset to others also produces SOTA forecasting accuracy"
summary: "The paper proposes PatchTST, a Transformer-based model that enhances long-term time series forecasting through two key innovations: patching of subseries-level time steps and channel-independence, where each univariate time series is processed independently with shared model weights. These techniques significantly improve both computational efficiency and forecasting accuracy, achieving state-of-the-art performance in supervised and self-supervised settings across multiple benchmark datasets."
location: Online (Zoom)
date: 2025-05-01T12:00:00.000Z
date_end: 2025-05-01T12:30:00.000Z
all_day: false
links:
  - url: https://arxiv.org/pdf/2211.14730
    name: "Paper"
  - url: A TIME SERIES IS WORTH 64 WORDS.pptx
    name: "slides"
event: EMIL Spring'25 Seminars
event_url: " "
publishDate: 2025-05-02T14:00:00.000Z
draft: false
featured: false
authors:
  - Ebrahim Farahmand
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
