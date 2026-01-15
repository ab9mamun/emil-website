---
title: "Stress Monitoring in Free-Living Environments"

abstract: "Stress monitoring is an important area of research with significant implications for individuals' physical and mental health. We present a data-driven approach for stress detection based on convolutional neural networks while addressing the problems of the best sensor channel and the lack of knowledge about stress episodes. Our work is the first to present an analysis of stress-related sensor data collected in real-world conditions from individuals diagnosed with Alcohol Use Disorder (AUD) and undergoing treatment to abstain from alcohol. We developed polynomial-time sensor channel selection algorithms to determine the best sensor modality for a machine learning task. We model the time variation in stress labels expressed by the participants as the subjective effects of stress. We addressed the subjective nature of stress by determining the optimal input length around stress events with an iterative search algorithm. We found the skin conductance modality to be most indicative of stress, and the segment length of 60 seconds around user-reported stress labels resulted in top stress detection performance. We used both majority undersampling and minority oversampling to balance our dataset. With majority undersampling, the binary stress classification model achieved an average accuracy of 99% and an f1-score of 0.99 on the training and test sets after 5-fold cross-validation. With minority oversampling, the performance on the test set dropped to an average accuracy of 76.25% and an f1-score of 0.68, highlighting the challenges of working with real-world datasets."

summary: "This study presents a CNN-based method for detecting stress from wearable sensor data collected in real-world conditions from people with Alcohol Use Disorder. It introduces algorithms to choose the most informative sensor channel and to handle the subjective timing of self-reported stress by optimizing the time window around reported events."

location: Online (Zoom)
date: '2025-12-17T12:00:00-07:00'
date_end: '2025-12-17T12:30:00-07:00'
all_day: false
links:
  - url: https://ieeexplore.ieee.org/document/10255120
    name: "Paper"
  - url: Stress_monitoring.pdf
    name: "slides"
event: EMIL Fall'25 Seminars
event_url: ""
publishDate: '2025-12-17T13:01:00-07:00'
draft: false
featured: false
authors:
  - nooshin-taheri-chatrudi
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
