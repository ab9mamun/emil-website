---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Contrastive learning based self-supervised time-series analysis"
event: EMIL Spring'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  "This paper proposes a new self-supervised learning based approach for industrial time-series analysis which uses data-augmentation techniques"
abstract: "Deep learning architectures usually require large scale labeled datasets for achieving good performance on general classification tasks including computer vision and natural language processing. Recent techniques of self-supervised learning have opened up new a research frontier where deep learning architectures can learn general features from unlabeled data. The task of self-supervised learning is usually accomplished with some sort of data augmentation through which the deep neural networks can extract relevant information. This paper presents a novel approach for self-supervised learning based time-series analysis based on the SimCLR contrastive learning. We present novel data augmentation techniques, focusing especially on time-series data, and study their effect on the prediction task. We provide comparison with several fault classification approaches on benchmark Tennessee Eastman dataset and report an improvement to 81.43% in the final accuracy using our contrastive learning approach. Furthermore we report a new benchmark of 80.80%, 81.05% and 81.43% for self-supervised training on Tennesee Eastman where a classifier is only trained with 5%, 10% or 50% percent of the available training data. Hence, we can conclude that the contrastive approach is very successful in time-series problems also, and further suitable for usage with partially labeled time-series datasets."
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-01-16T13:30:00-07:00
date_end: 2024-01-16T15:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2022-06-14T17:50:20-07:00

authors: [reza-rahimi-azghan]
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
url_slides: pres.pptx

url_code:
url_pdf: "https://www.sciencedirect.com/science/article/abs/pii/S1568494621011558"
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
