---
title: "Stress Detection using Context-Aware Sensor Fusion from Wearable Devices"

abstract: "Wearable medical technology has become increasingly popular in recent years. One function of wearable health devices is stress detection, which relies on sensor inputs to determine a patient’s mental state. This continuous, real-time monitoring can provide healthcare professionals with vital physiological data and enhance the quality of patient care. Current methods of stress detection lack: 1) robustness—wearable health sensors contain high levels of measurement noise that degrades performance and 2) adaptation—static architectures fail to adapt to changing contexts in sensing conditions. We propose to address these deficiencies with SELF-CARE, a generalized selective sensor fusion method of stress detection that employs novel techniques of context identification and ensemble machine learning. SELF-CARE uses a learning-based classifier to process sensor features and model the environmental variations in sensing conditions known as the noise context. SELF-CARE uses noise context to selectively fuse different sensor combinations across an ensemble of models to perform robust stress classification. Our findings suggest that for wrist-worn devices, sensors that measure motion are most suitable to understand noise context, while for chest-worn devices, the most suitable sensors are those that detect muscle contraction. We demonstrate SELF-CARE’s state-of-the-art performance on the WESAD data set. Using wrist-based sensors, SELF-CARE achieves 86.34% and 94.12% accuracy for the 3-class and 2-class stress classification problems, respectively. For chest-based wearable sensors, SELF-CARE achieves 86.19% (3-class) and 93.68% (2-class) classification accuracy. This work demonstrates the benefits of utilizing selective, context-aware sensor fusion in mobile health sensing that can be applied broadly to Internet of Things applications."

summary: "This study introduces SELF-CARE, a context-aware sensor fusion framework for stress detection using wearable devices. It addresses key limitations of existing methods—poor robustness and lack of adaptability—by modeling environmental noise and dynamically selecting sensor combinations through ensemble learning. SELF-CARE leverages motion sensors (for wrist devices) and muscle-contraction sensors (for chest devices) to understand noise context, achieving strong performance on the WESAD dataset."

location: Online (Zoom)
date: '2025-10-8T12:00:00-07:00'
date_end: '2025-10-8T12:30:00-07:00'
all_day: false
links:
  - url: https://ieeexplore.ieee.org/document/10097874
    name: "Paper"
  - url: Stress_Detection.pdf
    name: "slides"
event: EMIL Fall'25 Seminars
event_url: ""
publishDate: '2025-10-13T13:01:00-07:00'
draft: false
featured: false
authors:
  - Nooshin-Taheri
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
