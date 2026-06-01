---
title: "Counterfactual Modeling with Fine-Tuned LLMs for Health Intervention Design and Sensor Data Augmentation"
abstract: "Counterfactual explanations (CFEs) provide human-centric interpretability by identifying the minimal, actionable changes required to alter a machine learning model's prediction. Therefore, CFs can be used as (i) interventions for abnormality prevention and (ii) augmented data for training robust models. we conduct a comprehensive evaluation of CF generation using large language models (LLMs), including GPT-4 (zero-shot and few-shot) and two open-source models-BioMistral-7B and LLaMA-3.1-8B-in both pretrained and fine-tuned configurations. Using the multimodal AI-READI clinical dataset, we assess CFs across three dimensions: intervention quality, feature diversity, and augmentation effectiveness. Fine-tuned LLMs, particularly LLaMA-3.1-8B, produce CFs with high plausibility (up to 99%), strong validity (up to 0.99), and realistic, behaviorally modifiable feature adjustments. When used for data augmentation under controlled label-scarcity settings, LLM-generated CFs substantially restore classifier performance, yielding an average  20% F1 recovery across three scarcity scenarios. Compared with optimization-based baselines such as DiCE, CFNOW, and NICE, LLMs offer a flexible, model-agnostic approach that generates more clinically plausible, behaviorally actionable and semantically coherent counterfactuals. Overall, this work demonstrates the promise of LLM-driven counterfactuals for both interpretable intervention design and data-efficient model training in sensor-based digital health."
slides: ""
url_pdf: "https://ieeexplore.ieee.org/document/11537391"
publication_types:
  - "2"
authors: [Shovito Barua Soumma, Asiful Arefeen, Stephanie M. Carpenter, Melanie Hingle, Hassan Ghasemzadeh]
doi: "10.1109/OJEMB.2026.3697994"
publication: "IEEE Open Journal of Engineering in Medicine and Biology (OJEMB) - May 2026"
featured: false
tags: ["featured"]
categories: ""
image:
  caption: ""
  focal_point: ""
  preview_only: false
summary: "Proposed a novel framework for generating CFs using finetuned large language models (LLMs), with a focus on structured sensor-derived datasets in health and physiological monitoring"
url_dataset: null
url_project: null
publication_short: ""
url_source: null
url_video: null
projects: ["Metabolic-Health", "Expand-AI"]
date: 2026-05-31T16:30:00-07:00
url_slides: null
publishDate: 2026-05-31T16:30:00-07:00
url_poster: null
url_code: null
---
