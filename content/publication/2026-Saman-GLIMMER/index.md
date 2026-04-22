---
title: "Glycemic-Aware and Architecture-Agnostic Training Framework for Blood Glucose Forecasting in Type 1 Diabetes"
abstract: "Managing Type 1 Diabetes (T1D) demands constant vigilance as individuals strive to regulate their blood glucose levels and avoid dysglycemia, including hyperglycemia and hypoglycemia. Despite advances in automated insulin delivery (AID) systems, achieving optimal glycemic control remains challenging. These systems integrate data from wearable devices such as insulin pumps and continuous glucose monitors (CGMs), helping reduce variability and improve time in range. However, they often fail to prevent dysglycemia due to limitations in prediction algorithms that cannot accurately anticipate glycemic excursions. This limitation highlights the need for more advanced glucose forecasting methods. To address this need, we introduce GLIMMER (Glucose Level Indicator Model with Modified Error Rate), a modular and architecture-agnostic training framework for glucose forecasting. GLIMMER combines structured preprocessing, a region-aware loss formulation, and genetic algorithm-based weight optimization to emphasize prediction accuracy in dysglycemic regions. We evaluate GLIMMER using two datasets: the publicly available OhioT1DM dataset and a newly collected AZT1D dataset consisting of data from 25 individuals with T1D. Our analyses demonstrate that GLIMMER consistently improves forecasting performance across baseline architectures, reducing RMSE and MAE by up to 24.6% and 29.6%, respectively. Additionally, GLIMMER achieves a recall of 98.4% and an F1-score of 86.8% for dysglycemia prediction, highlighting strong performance in clinically high-risk regions. Compared with state-of-the-art models containing millions of parameters, such as TimesNet (18.7M), BG-BERT (2.1M), and Gluformer (11.2M), GLIMMER attains comparable accuracy while using only 10K parameters, demonstrating its efficiency as a lightweight and architecture-agnostic solution for glycemic forecasting."

slides: ""
url_pdf: "https://arxiv.org/abs/2502.14183"
publication_types:
  - "1"
authors:
  - Saman Khamesian
  - Asiful Arefeen
  - Maria Adela Grando
  - Bithika M. Thompson
  - Hassan Ghasemzadeh
doi: 
publication: "BMC Artificial Intelligence - April 2026"
featured: false
tags: ["featured"]
categories: ""
image:
  caption: ""
  focal_point: ""
  preview_only: false
summary: "This work focuses on improving blood glucose prediction by incorporating glycemic-aware training strategies that better capture hypo- and hyperglycemic events."
url_dataset: ""
url_project: null
publication_short: ""
url_source: null
url_video: null
projects: ""
date: 2026-04-21T16:01:00-07:00
url_slides: null
publishDate: 2025-04-21T16:01:00-07:00
url_poster: null
url_code: "https://github.com/SamanKhamesian/GLIMMER"
---
