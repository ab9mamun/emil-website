---
title: "Gated Integration of Low-Rank Adaptation for Continual Learning of Large Language Models"
abstract: "Continual learning (CL), which requires the model to learn multiple tasks sequentially, is crucial for large language models (LLMs). Recently, low-rank adaptation (LoRA), one of the most representative parameter-efficient fine-tuning (PEFT) methods, has gained increasing attention in CL of LLMs. However, most existing CL methods based on LoRA typically expand a new LoRA branch to learn each new task and force the new and old LoRA branches to influence old tasks equally, potentially leading to forgetting. In this work, we propose a new method, called gated integration of low-rank adaptation (GainLoRA), for CL of LLMs. GainLoRA expands a new LoRA branch for each new task and introduces gating modules to integrate the new and old LoRA branches. Furthermore, GainLoRA leverages the new gating module to minimize the influence from the new LoRA branch to old tasks, effectively mitigating forgetting and improving the model’s overall performance. Experimental results on CL benchmarks demonstrate that GainLoRA outperforms existing state-of-the-art methods"

summary: "GainLoRA is a continual learning method for large language models that builds on LoRA by adding a small input-dependent gating mechanism for each task-specific LoRA branch, so instead of always combining all learned branches equally, the model learns how much each branch should contribute for a given input. The key goal is to reduce forgetting in the realistic setting where tasks arrive sequentially, task identity is unknown at test time, and no old data are replayed. Its main insight is that the newest LoRA branch should have little or no effect on inputs from older tasks, so the paper designs the gate to stay near zero on old-task inputs through special initialization and update constraints, while still allowing strong activation for the current task. The authors evaluate the method on continual instruction-learning and long-sequence benchmarks using models like T5-Large, T5-XL, Llama-2, and Llama-3, and report consistently better average performance and lower forgetting than prior LoRA-based continual learning methods such as O-LoRA and InfLoRA. In short, the paper’s contribution is a smarter way to combine task-specific LoRA adapters, making LoRA-based continual learning more selective, more stable, and substantially less prone to interference across tasks."

location: Online (Zoom)
date: 2026-04-008T12:00:00-07:00
date_end: 2026-04-008T12:30:00-07:00
all_day: false
links:
  - url: https://arxiv.org/pdf/2505.15424
    name: "Paper"
  - url: press.pptx
    name: "slides"
event: EMIL Spring'26 Seminars
event_url: " "
publishDate: 2026-04-008T12:45:00-07:00
draft: false
featured: false
authors:
  - reza-rahimi-azghan
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
