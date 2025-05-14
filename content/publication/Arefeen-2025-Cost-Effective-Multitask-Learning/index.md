---
title: "Cost-Effective Multitask Active Learning in Wearable Sensor Systems"
abstract: "Multitask learning models provide benefits by reducing model complexity and improving accuracy by concurrently learning multiple tasks with shared representations. Leveraging inductive knowledge transfer, these models mitigate the risk of overfitting on any specific task, leading to enhanced overall performance. However, supervised multitask learning models, like many neural networks, require substantial amounts of labeled data. Given the cost associated with data labeling, there is a need for an efficient label acquisition mechanism, known as multitask active learning (MTAL). In wearable sensor systems, success of MTAL largely hinges on its query strategies because active learning in such settings involves interaction with end-users (e.g., patients) for annotation. However, these strategies have not been studied in mobile health settings and wearable systems to date. While strategies like one-sided sampling, alternating sampling, and rank-combination based sampling have been proposed in the past, their applicability in mobile sensor settings - a domain constrained by label deficit - remains largely unexplored. This study investigates the MTAL querying approaches and addresses crucial questions related to the choice of sampling methods and the effectiveness of multitask learning in mobile health applications. Utilizing two datasets on activity recognition and emotion classification, our findings reveal that rank-based sampling outperforms other techniques, particularly in tasks with high correlation. However, sole reliance on informativeness for sample selection may introduce biases into models. To address this issue, we also propose a Clustered Stratified Sampling (CSS) method in tandem with the multitask active learning query process. CSS identifies clustered mini-batches of samples, optimizing budget utilization and maximizing performance. When employed alongside rank-based query selection, our proposed CSS algorithm demonstrates up to 9% improvement in accuracy over traditional querying approaches for a 2000-query budget."
slides: ""
url_pdf: "https://drive.google.com/file/d/1gpQwMlqvj6YRLRrVwQL8bV7rL5_Kx_mn/view?usp=sharing"
publication_types:
  - "2"
authors:
  - Asiful Arefeen
  - Hassan Ghasemzadeh
doi: 
publication: "Sensors"
featured: false
tags: ["featured"]
categories: ""
image:
  caption: ""
  focal_point: ""
  preview_only: false
summary: "This method reduces the labeling cost to train an efficient multi-task neural network by adding an additional clustering step in the multi-task active learning loop, within the sampling process"
url_dataset: "https://data.mendeley.com/datasets/45f952y38r/5"
url_project: null
publication_short: ""
url_source: null
url_video: null
projects: ""
date: 2025-02-25T01:22:35-07:00
url_slides: null
publishDate: 2025-02-25T01:22:35-07:00
url_poster: null
url_code: null
---
