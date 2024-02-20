---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Rep-Net: Efficient On-Device Learning via Feature Reprogramming"
event: EMIL Spring'23 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  REP-Net is a counter to traditional transfer learning for On-board model training with more focus on memory efficiency. 
abstract: Transfer learning, where the goal is to transfer the welltrained deep learning models from a primary source task to a new task, is a crucial learning scheme for on-device machine learning, due to the fact that IoT/edge devices collect and then process massive data in our daily life. However, due to the tiny memory constraint in IoT/edge devices, such on-device learning requires ultra-small training memory footprint, bringing new challenges for memory-efficient learning. Many existing works solve this problem by reducing the number of trainable parameters. However, this doesn’t directly translate to memory saving since the major bottleneck is the activations, not parameters. To develop memory-efficient on-device transfer learning, in this work, we are the first to approach the concept of transfer learning from a new perspective of intermediate feature reprogramming of a pre-trained model (i.e., backbone). To perform this lightweight and memory-efficient reprogramming, we propose to train a tiny Reprogramming Network (Rep-Net) directly from the new task input data, while freezing the backbone model. The proposed Rep-Net model interchanges the features with the backbone model using an activation connector at regular intervals to mutually benefit both the backbone model and Rep-Net model features. Through extensive experiments, we validate each design specs of the proposed Rep-Net model in achieving highly memory-efficient on-device reprogramming. Our experiments establish the superior performance (i.e., low training memory and high accuracy) of Rep-Net compared to SOTA on-device transfer learning schemes across multiple benchmarks.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2023-04-06T14:00:00-07:00
date_end: 2023-04-06T14:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2023-04-06T18:50:20-07:00

authors: [asiful-arefeen]
tags: []

# Is this a featured event? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your event's folder or a URL.
url_slides: REP-NET.pptx

url_code:
url_pdf: "https://openaccess.thecvf.com/content/CVPR2022/papers/Yang_Rep-Net_Efficient_On-Device_Learning_via_Feature_Reprogramming_CVPR_2022_paper.pdf"
url_video:

# Markdown Slides (optional).
#   Associate this event with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---