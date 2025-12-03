---
title: "Learn more, but bother less: parameter efficient continual learning"
abstract: "Large Language Models (LLMs) have demonstrated profound capabilities due to their extensive pre-training on diverse corpora. However, LLMs often struggle with catastrophic forgetting when engaged in sequential task learning. In this paper, we propose a novel parameter-efficient approach for continual learning in LLMs, which empirically investigates knowledge transfer from previously learned tasks to new tasks through low-rank matrix parameters, enhancing the learning of new tasks without significant interference. Our method employs sensitivity-based analysis of low-rank matrix parameters to identify knowledge-specific parameters between sequential tasks, which are used to initialize the low-rank matrix parameters in new tasks. To maintain orthogonality and minimize forgetting, we further involve the gradient projection technique that keeps the low-rank subspaces of each new task orthogonal to those of previous tasks. Our experimental results on continual learning benchmarks validate the efficacy of our proposed method, which outperforms existing state-of-the-art methods in reducing forgetting, enhancing task performance, and preserving the model’s ability to generalize to unseen tasks."

summary: "LB-CL tackles continual learning for LLMs through a two-stage approach using SVD-based low-rank adapters. First, it calculates sensitivity scores to identify important parameters from previous tasks and uses them to initialize new tasks via weighted combination. Second, during training, it employs orthogonal gradient projection to ensure new tasks learn in directions perpendicular to old task subspaces, preventing interference. This balances forward knowledge transfer (through smart initialization) with forgetting prevention (through orthogonal training). Experiments show LB-CL outperforms previous state-of-the-art O-LoRA, achieving 76.7% versus 75.4% average accuracy on standard benchmarks."

location: Online (Zoom)
date: 2025-12-03T12:00:00-07:00
date_end: 2025-12-03T12:30:00-07:00
all_day: false
links:
  - url: https://openreview.net/pdf?id=ZxtaNh5UYB
    name: "Paper"
  - url: pres.pdf
    name: "slides"
event: EMIL Spring'25 Seminars
event_url: " "
publishDate: 2025-12-03T12:45:00-07:00
draft: false
featured: false
authors:
  - reza-rahimi-azghan
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
