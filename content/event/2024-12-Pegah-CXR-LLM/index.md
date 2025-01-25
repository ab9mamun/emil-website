---
title: "CXR-LLAVA: a multimodal large language model for interpreting chest X-ray images"
abstract: "Purpose: This study aimed to develop an open-source multimodal large language model (CXRLLAVA) for interpreting chest X-ray images (CXRs), leveraging recent advances in large language models (LLMs) to potentially replicate the image interpretation skills of human radiologists Materials and Methods: For training, we collected 592,580 publicly available CXRs, of which 374,881 had labels for certain radiographic abnormalities (Dataset 1) and 217,699 provided free-text radiology reports (Dataset 2). After pre-training a vision transformer with Dataset 1, we integrated it with an LLM influenced by the LLAVA network. Then, the model was fine-tuned, primarily using Dataset 2. The model’s diagnostic performance for major pathological findings was evaluated, along with the acceptability of radiologic reports by human radiologists, to gauge its potential for autonomous reporting. Results: The model demonstrated impressive performance in test sets, achieving an average F1 score of 0.81 for six major pathological findings in the MIMIC internal test set and 0.62 for seven major pathological findings in the external test set. The model's F1 scores surpassed those of GPT-4-vision and Gemini-Pro-Vision in both test sets. In human radiologist evaluations of the external test set, the model achieved a 72.7% success rate in autonomous reporting, slightly below the 84.0% rate of ground truth reports. Conclusion: This study highlights the significant potential of multimodal LLMs for CXR interpretation, while also acknowledging the performance limitations. Despite these challenges, we believe that making our model open-source will catalyze further research, expanding its effectiveness and applicability in various clinical contexts."

summary: "The study presents CXR-LLAVA, an open-source multimodal large language model designed to interpret chest X-rays (CXRs) and generate radiology reports, aiming to alleviate the workload of radiologists and enhance diagnostic accuracy. The model combines a Vision Transformer (ViT-L/16) for image encoding with the LLAMA-2 language model for text generation. "

location: Online (Zoom)
date: 2024-12-18T12:00:00.000Z
date_end: 2024-12-18T12:30:00.000Z
all_day: false
links:
  - url: CXR-LLM.pdf
    name: "Paper"
  - url: pres.pptx
    name: "slides"
event: EMIL Spring'25 Seminars
event_url: " "
publishDate: 2025-01-22T20:15:00.000Z
draft: false
featured: false
authors:
  - pegah-khorasani
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
