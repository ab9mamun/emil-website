---
title: "Reinforcement Learning for Solving the Vehicle Routing Problem"
abstract: "We present an end-to-end framework for solving the Vehicle Routing Problem (VRP) using reinforcement learning. In this approach, we train a single policy model that finds near-optimal solutions for a broad range of problem instances of similar size, only by observing the reward signals and following feasibility rules. We consider a parameterized stochastic policy, and by applying a policy gradient algorithm to optimize its parameters, the trained model produces the solution as a sequence of consecutive actions in real time, without the need to re-train for every new problem instance. On capacitated VRP, our approach outperforms classical heuristics and Google's OR-Tools on medium-sized instances in solution quality with comparable computation time (after training). We demonstrate how our approach can handle problems with split delivery and explore the effect of such deliveries on the solution quality. Our proposed framework can be applied to other variants of the VRP such as the stochastic VRP, and has the potential to be applied more generally to combinatorial optimization problems."

summary: "A reinforcement learning approach to solve the vehicle routing problem."
location: Online (Zoom)
date: 2022-11-23T12:00:00.000Z
date_end: 2022-11-23T12:30:00.000Z
all_day: false
links:
  - url: https://proceedings.neurips.cc/paper/2018/file/9fb4651c05b2ed70fba5afe0b039a550-Paper.pdf
    name: "PDF"
  - url: slides.pdf
    name: "slides"
event: EMIL Fall'22 Seminars
event_url: " "
publishDate: 2022-11-23T20:56:00.000Z
draft: false
featured: false
authors:
  - abdullah-mamun
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
