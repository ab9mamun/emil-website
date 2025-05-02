---
title: "AttenGluco: Multimodal Transformer-Based Blood Glucose Forecasting on AI-READI Dataset"

abstract: "Diabetes is a chronic metabolic disorder characterized by persistently high blood glucose levels (BGLs), leading to severe complications such as cardiovascular disease, neuropathy, and retinopathy. Predicting BGLs enables patients to maintain glucose levels within a safe range and allows caregivers to take proactive measures through lifestyle modifications. Continuous Glucose Monitoring (CGM) systems provide real-time tracking, offering a valuable tool for monitoring BGLs. However, accurately forecasting BGLs remains challenging due to fluctuations due to physical activity, diet, and other factors. Recent deep learning models show promise in improving BGL prediction. Nonetheless, forecasting BGLs accurately from multimodal, irregularly sampled data over long prediction horizons remains a challenging research problem. In this paper, we propose AttenGluco1 , a multimodal Transformerbased framework for long-term blood glucose prediction. AttenGluco employs cross-attention to effectively integrate CGM and activity data, addressing challenges in fusing data with different sampling rates. Moreover, it employs multi-scale attention to capture long-term dependencies in temporal data, enhancing forecasting accuracy. To evaluate the performance of AttenGluco, we conduct forecasting experiments on the recently released AIREADI dataset, analyzing its predictive accuracy across different subject cohorts including healthy individuals, people with prediabetes, and those with type 2 diabetes. Furthermore, we investigate its performance improvements and forgetting behavior as new cohorts are introduced. Our evaluations show that AttenGluco improves all error metrics, such as root mean square error (RMSE), mean absolute error (MAE), and correlation, compared to the multimodal LSTM model, which is widely used in state-of-the-art blood glucose prediction. AttenGluco outperforms this baseline model by about 10% and 15% in terms of RMSE and MAE, respectively."
slides: ""
url_pdf: "https://arxiv.org/pdf/2502.09919"
publication_types:
  - "1"
authors:
  - Ebrahim Farahmand
  - Reza Rahimi Azghan
  - Nooshin Taheri Chatrudi
  - Eric Kim
  - Gautham Krishna Gudur
  - Edison Thomaz
  - Giulia Pedrielli
  - Pavan Turaga
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
summary: "We introduces a novel Transformer-based framework, AttenGluco, designed to improve long-term blood glucose level forecasting using multimodal data—including CGM and activity signals. By integrating cross-attention and multi-scale attention mechanisms, the model effectively fuses time-series data with different sampling rates and captures long-term dependencies, outperforming a multimodal LSTM baseline by up to 12% in RMSE across multiple cohorts (healthy, prediabetes, and type 2 diabetes) using the AI-READI dataset."
url_dataset: null
url_project: null
publication_short: ""
url_source: null
url_video: null
projects: ["Expand-AI"]
date: 2025-04-09T16:01:00-07:00
url_slides: null
publishDate: 2025-05-02T14:40:00-07:00
url_poster: null
url_code: "https://github.com/rzarhmi/AttenGluco"
---
