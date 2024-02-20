---
title: "Channel Pruning via Automatic Structure Search"
abstract: "Channel pruning is among the predominant approaches to compress deep neural networks. To this end, most existing pruning methods focus on selecting channels (filters) by importance/optimization or regularization based on rule-of-thumb designs, which defects in sub-optimal pruning. In this paper, we propose a new channel pruning method based on artificial bee colony algorithm (ABC), dubbed as ABCPruner, which aims to efficiently find optimal pruned structure, i.e., channel number in each layer, rather than selecting \"important\" channels as previous works did. To solve the intractably huge combinations of pruned structure for deep networks, we first propose to shrink the combinations where the preserved channels are limited to a specific space, thus the combinations of pruned structure can be significantly reduced. And then, we formulate the search of optimal pruned structure as an optimization problem and integrate the ABC algorithm to solve it in an automatic manner to lessen human interference. ABCPruner has been demonstrated to be more effective, which also enables the fine-tuning to be conducted efficiently in an end-to-end manner. The source codes can be available at https: //github.com/lmbxmu/ABCPruner."
summary: "This paper proposes a new channel pruning method based on artificial bee colony algorithm (ABC), dubbed as ABCPruner, which aims to efficiently find optimal pruned structure."
location: Online (Zoom)
date: 2022-10-26T12:00:00.000Z
date_end: 2022-10-26T12:30:00.000Z
all_day: false
links:
  - url: https://www.ijcai.org/proceedings/2020/94
    name: "Paper"
  - url: slides.pdf
    name: "slides"
event: EMIL Fall'22 Seminars
event_url: " "
publishDate: 2022-10-26T20:56:00.000Z
draft: false
featured: false
authors:
  - chia-cheng-kuo
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
---
