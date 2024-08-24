---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Learning Representations from EEG with Deep Recurrent-Convolutional Neural Networks"
event: EMIL Spring'24 Seminars
event_url:
location: Health Futures Center, ASU
address:
  street:
  city:
  region:
  postcode:
  country:
summary: This paper proposes a novel approach for learning such representations from multi-channel EEG time-series, and demonstrate its advantages in the context of mental load classification task.
abstract: One of the challenges in modeling cognitive events from electroencephalogram (EEG) data is finding representations that are invariant to inter- and intra-subject differences, as well as to inherent noise associated with such data. Herein, we propose a novel approach for learning such representations from multi-channel EEG time-series, and demonstrate its advantages in the context of mental load classification task. First, we transform EEG activities into a sequence of topology-preserving multi-spectral images, as opposed to standard EEG analysis techniques that ignore such spatial information. Next, we train a deep recurrent-convolutional network inspired by state-of-the-art video classification to learn robust representations from the sequence of images. The proposed approach is designed to preserve the spatial, spectral, and temporal structure of EEG which leads to finding features that are less sensitive to variations and distortions within each dimension. Empirical evaluation on the cognitive load classification task demonstrated significant improvements in classification accuracy over current state-of-the-art approaches in this field.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-02-27T15:00:00-07:00
date_end: 2024-02-27T16:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-01-02T16:50:20-07:00

authors: [nooshin-taheri-chatrudi]
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
url_slides: slides.pptx

url_code:
url_pdf: "https://arxiv.org/pdf/1511.06448.pdf"
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
