---
slides: ""
url_pdf: ""
summary:

authors: [EPSL]
url_video: ""
date: 2023-05-01T23:58:08-08:00
external_link: ""
url_slides: ""
title: "Expand AI"
tags: []
image:
  caption: ""
  focal_point: ""
  preview_only: false
categories: []
url_code: ""
---

Pervasive Systems Integrate computing capabilities into everyday objects such as phones, wearables, cars, assistive robots, homes, and workplaces. These systems must be able to work in highly dynamic environments and interact directly with humans. They are also constrained in resources. The need for robust, interactive, and embedded pervasive systems motivated us to start the ExpandAI project. Our goal in this project is to (i) design robust machine learning algorithms that address distribution shifts in the data due to dynamic changes in the system status over time; (ii) design interactive machine learning techniques that incorporate human input and prior domain knowledge for improved model performance and personalized decision making; and (iii) develop embedded machine learning methods for deploying the models on embedded devices with stringent constrained resources.

Overall, this project is broken into three tasks:

# Pervasive Continual Learning
We will research methods that enable pervasive systems to learn incrementally and sequentially, accumulating expertise and building upon previously acquired knowledge while mitigating catastrophic forgetting. Recognizing the lack of rigorous prior work on pervasive continual learning, we propose a holistic approach that includes studying distribution shifts, developing methods for out-of-distribution generalization, designing techniques to deal with noisy labels, designing algorithms for continual learning.


Continual learning develops methods capable of acquiring new knowledge and adapting to evolving data distributions over time. Such systems learn incrementally and sequentially, allowing them to accumulate expertise and build upon previously acquired knowledge. This is particularly crucial in real-world applications where data is dynamic, and tasks may change or expand, such as in distributed pervasive systems. However, research on pervasive continual learning is in its infancy. Building on prior work by PIs Pedrielli, Thomaz, Ghasemzadeh, and Turaga on wearable computing, continual learning, transfer learning, and optimization, we propose a holistic approach to designing continual learning solutions for pervasive systems by studying distribution shifts in pervasive systems and developing methods for out-of-distribution generalization, designing algorithms for continual learning in federated settings, and developing benchmarks to study and evaluate continual learning in pervasive systems.

#  Aligned Reinforcement Learning for Behavior Change
AI systems that seek behavior change should act in alignment with their users’ interests. However, no best practices exist to design reinforcement learning (RL) problems that are aligned with stakeholders interests. To create personalized behavior change systems, we will investigate methods of reward function design and develop novel methodologies to specify a personalized RL problem in a partially observable domain. We propose to define an expressive reward function representation that permits personalization by each user’s expressed preferences. In deployed systems, a reward-conditioned policy and Bayesian inference of the reward function will efficiently align each system with its user’s preferences.

Human behavior decisively influences chronic health conditions that account for two-thirds of deaths globally, including heart disease, stroke, diabetes, cancer, and obesity. Interventions to change physical activity, diet, or other behavior are crucial in preventing and managing these chronic conditions. Pervasive systems provide a unique opportunity to apply just-in-time adaptive intervention. This style of intervention leverages continuous monitoring of the user to maintain up-to-date contextual understanding. When this context recommends a intervention, it can be delivered immediately and with effective parameters (e.g., intervention type and content). Monitored context includes information about the user’s behavior and health status, such as activity, stress level, glucose level, calorie intake, and physiological health. Existing behavioral theories are too “one size fits all” to provide personalized decision policies for just-in-time adaptive intervention. Examples include universal recommendations that adults consume at least 5 servings of fruits and vegetables per day and exercise 150 minutes per week. Therefore, there has been much interest in how to best use data collected with pervasive systems to inform the design of adaptive interventions. Reinforcement learning (RL) holds promise as a general framework for lasting behavior change, since RL algorithms use immediate context and can adjust for the longer-term effects of each action.

# Robust robot perception and decision-making:
We will investigate context-aware robot navigation leveraging (i) competence-aware perception; (ii) geometry and shape-aware generative modeling; and (iii) preference- and uncertainty-aware decision-making. We will study uncertainty quantification and domain adaptation methods, and how they are impacted by models and backbones that highlight shape vs texture on targets. We will also design imitation learning and reinforcement learning-based approaches to learn from human data and preferences.

This project theme focuses on the problem of perception and decision-making for context-aware navigation of urban-scale assistive robots (e.g., last-mile delivery). Robots deployed in such unstructured real-world settings will inevitably encounter complex scenarios not seen before in training time. While existing solutions have shown impressive ability at being autonomous under “nominal” circumstances when provided with ample previous experiences and sufficient annotations specific to the scenario, they are unable to handle complex scenarios involving multiple agents and contextual costs, and in adverse perceptual conditions (e.g., low light and inclement weather). Decision making in uncertain environments depends on several factors including 1) the perceptual uncertainty of the robot; 2) the accuracy of the robot’s actions; and 3) the legibility of the robot’s actions to other vehicles such as cars and bicycles. The proposed research builds on the prior work of the PIs, to design methods for robust perception and decision-making in naturalistic settings.

##### *This material is based upon work supported by the U.S. National Science Foundation (NSF) under Award Number 2402650. Any opinions, findings and conclusions or recommendations expressed in this material do not necessarily reflect the views of the U.S. National Science Foundation.*

<div class="container">
<div class="row justify-content-center people-widget">
<div class="col-md-12 section-heading"><h1>Team</h1></div>
<div class="col-12 col-sm-auto people-person"><a href="https://search.asu.edu/profile/4018242"><img class="avatar avatar-circle" src="/people/hassan.jpg" alt="Avatar"></a><div class="portrait-title"><h2><a href="https://search.asu.edu/profile/4018242">Hassan Ghasemzadeh</a></h2></div></div>
</div>
</div>

![](PIs.png)
