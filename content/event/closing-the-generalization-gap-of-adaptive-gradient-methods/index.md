---
title: "Closing the Generalization Gap of Adaptive Gradient Methods in Training Deep Neural Networks"
abstract: "Adaptive gradient methods, which adopt historical gradient information to automatically adjust the learning rate, despite the nice property of fast convergence, have been observed to generalize worse than stochastic gradient descent (SGD) with momentum in training deep neural networks. This leaves how to close the generalization gap of adaptive gradient methods an open problem. In this work, we show that adaptive gradient methods such as Adam, Amsgrad, are sometimes \"over adapted\". We design a new algorithm, called Partially adaptive momentum estimation method, which unifies the Adam/Amsgrad with SGD by introducing a partial adaptive parameter p, to achieve the best from both worlds. We also prove the convergence rate of our proposed algorithm to a stationary point in the stochastic nonconvex optimization setting. Experiments on standard benchmarks show that our proposed algorithm can maintain fast convergence rate as Adam/Amsgrad while generalizing as well as SGD in training deep neural networks. These results would suggest practitioners pick up adaptive gradient methods once again for faster training of deep neural networks."

summary: "This paper addresses the generalization gap on large neural networks with adaptive gradient-based optimizers and proposes a partially adaptive solution to overcome the problem."
location: Online (Zoom)
date: 2022-10-05T12:00:00.000Z
date_end: 2022-10-05T12:30:00.000Z
all_day: false
links:
  - url: https://www.ijcai.org/proceedings/2020/452
    name: "paper"

event: EMIL Fall'22 Seminars
event_url: " "
publishDate: 2022-10-05T20:56:00.000Z
draft: false
featured: false
authors:
  - abdullah-mamun
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
