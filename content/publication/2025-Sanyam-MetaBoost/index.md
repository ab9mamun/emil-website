---
title: "Enhancing Metabolic Syndrome Prediction with Hybrid Data Balancing and Counterfactuals"

abstract: "Metabolic Syndrome (MetS) is a cluster of interrelated risk factors that significantly increases the risk of cardiovascular diseases and type 2 diabetes. Despite its global prevalence, accurate prediction of MetS remains challenging due to issues such as class imbalance, data scarcity, and methodological inconsistencies in existing studies. In this paper, we address these challenges by systematically evaluating and optimizing machine learning (ML) models for MetS prediction, leveraging advanced data balancing techniques and counterfactual analysis. Multiple ML models, including XGBoost, Random Forest, TabNet, etc., were trained and compared under various data balancing techniques such as random oversampling (ROS), SMOTE, ADASYN, and CTGAN. Additionally, we introduce MetaBoost, a novel hybrid framework that integrates SMOTE, ADASYN, and CTGAN, optimizing synthetic data generation through weighted averaging and iterative weight tuning to enhance the model's performance (achieving up to a 1.87% accuracy improvement over individual balancing techniques). A comprehensive counterfactual analysis is conducted to quantify the feature-level changes required to shift individuals from high-risk to low-risk categories. The results indicate that blood glucose (50.3%) and triglycerides (46.7%) were the most frequently modified features, highlighting their clinical significance in MetS risk reduction. Additionally, probabilistic analysis shows elevated blood glucose (85.5% likelihood) and triglycerides (74.9% posterior probability) as the strongest predictors. This study not only advances the methodological rigor of MetS prediction but also provides actionable insights for clinicians and researchers, highlighting the potential of ML in mitigating the public health burden of metabolic syndrome."

slides: ""
url_pdf: "https://arxiv.org/pdf/2504.06987"
publication_types:
  - "1"
authors:
  - Sanyam Paresh Shah
  - Abdullah Mamun
  - Shovito Barua Soumma
  - Hassan Ghasemzadeh
doi: 
publication: "The 47th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), July 14–17, 2025, Copenhagen, Denmark."
featured: true
tags: ["featured"]
categories: ""
image:
  caption: ""
  focal_point: ""
  preview_only: false
summary: "We introduce MetaBoost, a novel hybrid framework that integrates SMOTE, ADASYN, and CTGAN, optimizing synthetic data generation through weighted averaging and iterative weight tuning to enhance the model's performance (achieving a 1.87% accuracy improvement over individual balancing techniques)."
url_dataset: https://www.kaggle.com/datasets/antimoni/metabolic-syndrome
url_project: null
publication_short: ""
url_source: null
url_video: https://www.youtube.com/watch?v=mIZog_q-bh4
projects: ["Metabolic-Health"]
date: 2025-04-09T16:01:00-07:00
url_slides: slides.pdf
publishDate: 2025-04-09T16:01:00-07:00
url_poster: null
url_code: https://github.com/asusanyamshah/MetaBoost
---
