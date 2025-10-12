---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Pilot Stress Detection Through Physiological Signals Using a Transformer-Based Deep Learning Model"
event: EMIL Fall'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  Pilot stress detection is a challenging task and it plays a vital role in improving flight performance and avoiding catastrophic accidents. Many deep learning models have been adopted for stress recognition. However, these models tend to ignore the dependencies between multimodal physiological signals, which can boost the model performance potentially. A transformer-based deep learning framework, which can obtain the position information of multimodal signals by combining a transformer network with a traditional convolutional neural network (CNN), is proposed for detecting pilot stress. The 14 pilots’ physiological data, including electrocardiography (ECG), electromyography (EMG), electrodermal (EDA), respiration (RESP), and skin temperature (SKT), under different stress states are collected for training and validation, and evaluated among different state-of-the-art models. The results show that the proposed model achieves an accuracy of 93.28%, 88.75%, and 84.85% for two-, three-, and four-class classification tasks, respectively, showing faster integration and promising performance.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-08-14T12:30:00-07:00
date_end: 2025-08-14T13:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-10-08T13:40:20-07:00

authors: [Yuhan Li; Ke Li; Jiaao Chen; Shaofan Wang; Haochang Lu; Dongsheng Wen]
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
url_slides: UniCast.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2508.11954"
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