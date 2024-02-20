---
abstract: We present an electrocardiogram (ECG) -based emotion recognition system using self-supervised learning. Our proposed architecture consists of two main networks, a signal transformation recognition network and an emotion recognition network. First, unlabelled data are used to successfully train the former network to detect specific pre-determined signal transformations in the self-supervised learning step. Next, the weights of the convolutional layers of this network are transferred to the emotion recognition network, and two dense layers are trained in order to classify arousal and valence scores. We show that our self-supervised approach helps the model learn the ECG feature manifold required for emotion recognition, performing equal or better than the fully-supervised version of the model. Our proposed method outperforms the state-of-the-art in ECG-based emotion recognition with two publicly available datasets, SWELL and AMIGOS. Further analysis highlights the advantage of our self-supervised approach in requiring significantly less data to achieve acceptable results.
slides: ""
url_pdf: https://arxiv.org/pdf/1910.07497.pdf
summary: Emotion classification using self-supervised learning and six signal transformations as pretext tasks.
title: "Self-Supervised Learning for ECG-Based Emotion Recognition"
location: Online (Zoom)
date: 2021-04-26T15:00:00-07:00
date_end: 2021-04-26T15:30:00-07:00
all_day: false
event: "EPSL Spring'21 Seminars "
event_url: " "
featured: false
authors:
  - ramesh-sah
url_video: null
url_slides: https://docs.google.com/presentation/d/1ssWA5alpJ6CQ_oQq2ZnNPBIqikRihguX-Ctoo0FCHAo/edit?usp=sharing
address:
  ? street
  ? city
  ? region
  ? postcode
  ? country
publishDate: 2021-04-26T22:00:00.000Z
tags: []
projects: []
image:
  filename: featured.png
  caption: ""
  focal_point: Smart
  preview_only: false
url_code: null
---
