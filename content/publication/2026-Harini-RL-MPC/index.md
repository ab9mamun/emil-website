---
title: "Contextual Bandit-based MPC Tuning for Optimized Personalization of Physical Activity Behavioral Interventions"
abstract: "“Just-in-Time” adaptive interventions (JITAIs) can provide daily step goals and financial incentives (e.g., reward points) to enable participants to reach healthy levels of physical activity. However, personalization and optimization remain challenging because participant responses vary over time and between individuals. Recent JITAI efforts have benefited from control-oriented strategies using system identification and Model Predictive Control (MPC), with YourMove (NCT05598996) providing an illustrative example. MPC offers a structured decision framework for selecting feasible goal trajectories from theory-guided dynamic behavioral models, but its closed-loop performance depends on tuning choices that trade off tracking speed, smoothness, constraint satisfaction, and other criteria, making manual selection difficult. A contextual multi-armed bandit formulation can instead use a reward function to select MPC tuning parameters that best align the controller with the intervention outcomes of interest, conditioned on observed participant context. This paper presents a simulation-based proof of concept in which a TD3-based agent is used as an outer-loop tuner that learns the optimal MPC tuning parameters, while MPC produces feasible responses that satisfy intervention constraints. Results demonstrate improved closed-loop behavior tracking and increased self-efficacy relative to a fixed-tuning MPC baseline, and multi-seed training indicates reproducible convergence to high-reward tuning policies. Both novel and practical insights on the synergism of machine learning and control engineering are outcomes of this research."

slides: ""
url_pdf: "https://drive.google.com/file/d/1oVeHSudfInSHAEi8FOtTNrtWb24PWlBA/view?usp=sharing"
publication_types:
  - "1"
authors:
  - Sri Harini Balaji
  - Saman Khamesian
  - Di Yang Shi
  - Stephanie M. Carpenter
  - Hassan Ghasemzadeh
  - W. Bradley Knox
  - Jennie Si
  - Daniel E. Rivera
doi: 
publication: "6th Modeling, Estimation and Control Conference (MECC) 2026 - October 25-28, 2026 - Phoenix, Arizona, USA."
featured: false
tags: ["featured"]
categories: ""
image:
  caption: ""
  focal_point: ""
  preview_only: false
summary: "We present a contextual bandit–based reinforcement learning framework for data-driven tuning of Model Predictive Control (MPC) for personalized physical activity interventions. A TD3-based agent learns MPC tuning parameters that improve step-goal tracking and self-efficacy while preserving the feasibility and constraint-handling capabilities of MPC."
url_dataset: ""
url_project: null
publication_short: ""
url_source: null
url_video: null
projects: [Expand-AI]
date: 2026-04-21T16:01:00-07:00
url_slides: null
publishDate: 2025-04-21T16:01:00-07:00
url_poster: null
url_code: ""
---
