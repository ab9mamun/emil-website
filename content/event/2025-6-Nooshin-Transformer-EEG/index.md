---
title: "A Transformer-Based Approach Combining Deep Learning Network and Spatial-Temporal Information for Raw EEG Classification"

abstract: "The attention mechanism of the Transformer has the advantage of extracting feature correlation in the long-sequence data and visualizing the model. As time-series data, the spatial and temporal dependencies of the EEG signals between the time points and the different channels contain important information for accurate classification. So far, Transformer-based approaches have not been widely explored in motor-imagery EEG classification and visualization, especially lacking general models based on cross-individual validation. Taking advantage of the Transformer model and the spatial-temporal characteristics of the EEG signals, we designed Transformer-based models for classifications of motor imagery EEG based on the PhysioNet dataset. With 3s EEG data, our models obtained the best classification accuracy of 83.31%, 74.44%, and 64.22% on two-, three-, and four-class motor-imagery tasks in cross-individual validation, which outperformed other state-of-the-art models by 0.88%, 2.11%, and 1.06%. The inclusion of the positional embedding modules in the Transformer could improve the EEG classification performance. Furthermore, the visualization results of attention weights provided insights into the working mechanism of the Transformer-based networks during motor imagery tasks. The topography of the attention weights revealed a pattern of event-related desynchronization (ERD) which was consistent with the results from the spectral analysis of Mu and beta rhythm over the sensorimotor areas. Together, our deep learning methods not only provide novel and powerful tools for classifying and understanding EEG data but also have broad applications for brain-computer interface (BCI) systems."

summary: "This study proposes Transformer-based models for motor imagery EEG classification, leveraging their ability to capture spatial-temporal dependencies and visualize attention patterns. Using 3-second EEG data from the PhysioNet dataset with cross-individual validation, the models outperformed existing methods. Positional embeddings improved accuracy, and attention visualizations revealed neural patterns consistent with event-related desynchronization, highlighting the models’ potential for brain-computer interface applications."

location: Online (Zoom)
date: '2025-06-25T12:00:00-07:00'
date_end: '2025-06-25T12:30:00-07:00'
all_day: false
links:
  - url: https://ieeexplore.ieee.org/abstract/document/9845479
    name: "Paper"
  - url: transformer_EEG.pdf
    name: "slides"
event: EMIL Spring'25 Seminars
event_url: ""

draft: false
featured: false
authors:
  - Nooshin-Taheri
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
