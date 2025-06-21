---
title: "Integration of Clinical Criteria into the Training of Deep Models: Application to Glucose Prediction for Diabetic People"
abstract: "Traditional neural network training methods in healthcare often overlook clinical requirements, resulting in models that may achieve high accuracy but lack clinical relevance. This study tackles that limitation in the context of glucose prediction for individuals with diabetes. The authors introduce a novel training methodology that balances statistical accuracy with clinical constraints established by health authorities. By progressively shifting focus from pure prediction accuracy to clinical acceptability, the proposed approach employs a custom loss function designed specifically for glucose forecasting. Evaluations on datasets from both type-1 and type-2 diabetes patients demonstrate that the method significantly improves clinical validity. Notably, the framework identifies models that not only maintain high predictive accuracy but also satisfy crucial clinical standards."
summary: "This presentation introduced a framework that incorporates clinical safety directly into the training of deep learning models for glucose prediction in diabetic patients. Instead of optimizing solely for accuracy, the approach uses a specialized loss function (gcMSE) that penalizes clinically risky errors more heavily. The authors also proposed the PICA algorithm, which gradually shifts training toward meeting clinical standards. Tested on type-1 and type-2 diabetes datasets, the method showed improved safety and reliability, especially in critical glycemic ranges like hypoglycemia."
location: Arizona State University
date: 2025-06-23T12:00:00.000Z
date_end: 2025-06-23T12:30:00.000Z
all_day: false
links:
  - url: slides.pdf
    name: "Paper"
  - url: slides.pptx
    name: "slides"
event: EMIL Spring'25 Seminars
event_url: " "
publishDate: 2025-06-23T20:00:00.000Z
draft: false
featured: false
authors:
  - pegah-khorasani
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
