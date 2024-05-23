---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Contrastive Representation Learning for Electroencephalogram Classification"
event: EMIL Summer'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "This paper presents a framework for learning representations from EEG signals via contrastive learning."
abstract: "Interpreting and labeling human electroencephalogram (EEG) is a challenging task requiring years of medical training. We present a framework for learning representations from EEG signals via contrastive learning. By recombining channels from multi-channel recordings, we increase the number of samples quadratically per recording. We train a channel-wise feature extractor by extending the SimCLR framework to time-series data. We introduce a set of augmentations for EEG and study their efficacy on different classification tasks. We demonstrate that the learned features improve EEG classification and significantly reduce the amount of labeled data needed on three separate tasks: (1) Emotion Recognition (SEED), (2) Normal/Abnormal EEG classification (TUH), and (3) Sleep-stage scoring (SleepEDF). Our models show improved performance over previously reported supervised models on SEED and SleepEDF and self-supervised models on all three tasks."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-05-21T15:00:00-07:00
date_end: 2024-05-21T15:45:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-05-21T16:50:20-07:00

authors: [nooshin-taheri]
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
url_slides: slides.pdf

url_code:
url_pdf: "http://proceedings.mlr.press/v136/mohsenvand20a/mohsenvand20a.pdf"
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