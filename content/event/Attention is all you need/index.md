---
title: "Attention is all you need"
abstract: "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data."
summary: "The paper addresses the limitations of recurrent neural networks (RNNs) in sequence transduction tasks, specifically their sequential nature hindering parallelization and efficiency, especially with long sequences. The authors aim to overcome these limitations and propose a novel architecture that can learn long-range dependencies more effectively."
location: Online (Zoom)
date: 2024-10-09T12:00:00.000Z
date_end: 2024-10-09T13:00:00.000Z
all_day: false
links:
  - url: https://arxiv.org/pdf/1706.03762
    name: "PDF"
event: EMIL Fall'24 Seminars
event_url:
publishDate: 2024-10-09T20:56:00.000Z
draft: false
featured: false
authors:
  - reza-rahimi-azghan
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
