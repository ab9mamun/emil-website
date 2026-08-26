---
title: "Latent-LoRA: Compact Latent-Space Adapters with Gradient-Free Routing for Continual Learning"
abstract: "Large language models generalize well to individual tasks but lack an inherent mechanism for learning them sequentially, leading to catastrophic forgetting. To mitigate this, LoRA-based continual learning methods allocate a separate low-rank adapter per task, yet existing approaches either require task identity at inference or sum all adapters indiscriminately, letting irrelevant branches distort the output. Recent gating-based solutions route inputs to the correct adapter but introduce trainable parameters that themselves need protection against forgetting. In this work, we observe that pooled token embeddings from a frozen LLM embedding layer already separate task distributions throughout the learning sequence. A Gaussian mixture model fitted on these embeddings, without any gradient-based training, is sufficient for task-agnostic adapter selection at test time. This eliminates the need for a learned gating module. On the adapter side, constraining each task’s parameters to the principal subspace of the pretrained weights via SVD yields a compact latent-space parameterization. Within this subspace, orthogonal regularization directly controls inter-task interference. The resulting system, Latent-LoRA, is replay-free, requires no trainable routing component, and uses substantially fewer parameters per task. Experiments across five model scales and two established continual learning benchmarks show state-of-the-art performance with near-zero forgetting."

summary: "Latent-LoRA does continual learning for LLMs in the task-agnostic, replay-free setting by splitting the problem into two pieces that each avoid the usual trap. On the adapter side, it takes the rank-r truncated SVD of each pretrained weight once and freezes all three factors, so a task's entire update is a small r×r matrix inside that subspace — which cuts per-task parameters by 16–80× and, more importantly, makes cross-task interference reduce exactly to a quadratic form in those tiny matrices, so orthogonally regularizing them gives a genuine uniform bound (Proposition 1) rather than the partial control O-LoRA's penalty provides. On the routing side, it observes that pooled embeddings from the frozen embedding layer already separate tasks, so a Gaussian mixture fitted with K-means and a pooled covariance — no gradients anywhere — is enough to produce a posterior over tasks and softly blend the stored adapters. Because the router has no trainable parameters, it can't forget, which removes the second continual-learning mechanism that gated methods like GainLoRA need to protect their gates. Across two benchmarks, four task orderings, and five model scales up to 13B, it gets the best average performance and drives forgetting to roughly zero."

location: Online (Zoom)
date: 2026-08-26T12:00:00-07:00
date_end: 2026-08-26T12:30:00-07:00
all_day: false
links:
  - url: https://arxiv.org/pdf/2607.23837
    name: "Paper"
  - url: press.pptx
    name: "slides"
event: EMIL Spring'26 Seminars
event_url: " "
publishDate: 2026-08-26T12:45:00-07:00
draft: false
featured: false
authors:
  - reza-rahimi-azghan
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
