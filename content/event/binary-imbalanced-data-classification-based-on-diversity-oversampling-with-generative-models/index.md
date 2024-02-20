---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Binary imbalanced data classification based on diversity oversampling by generative models"
event: EMIL Spring'24 Seminars
event_url:
location: Health Futures Center, ASU
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "This paper proposes two binary imbalanced data classification methods with extreme learning machine autoencoders and generative models. Their methods outperform SMOTE and similar data balancing tools on most benchmark datasets."
abstract: "In many practical applications, the data are class imbalanced. Accordingly, it is very meaningful and valuable to investigate the classification of imbalanced data. In the framework of binary imbalanced data classification, the synthetic minority oversampling technique (SMOTE) is the best-known oversampling method. However, for each positive sample, SMOTE generates only k synthetic samples on the lines between the positive sample and its k-nearest neighbors, resulting in three drawbacks: (1) SMOTE cannot effectively extend the training field of positive samples; (2) the generated positive samples lack diversity; (3) SMOTE does not accurately approximate the probability distribution of the positive samples. Therefore, two binary imbalanced data classification methods named BIDC1 and BIDC2 based on diversity oversampling by generative models are proposed. The BIDC1 and BIDC2 conduct diversity oversampling using extreme learning machine autoencoder and generative adversarial network, respectively. Extensive experiments on 26 data sets are conducted to compare the two methods with 14 state-of-the-art methods using five metrics: F-measure, G-means, AUC-area, MMD-score, and Silhouette-score. The experimental results demonstrate that the two methods outperform the other 14 methods."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-01-09T15:45:00-07:00
date_end: 2024-01-09T17:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-01-09T16:50:20-07:00

authors: [abdullah-mamun]
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
url_pdf: "https://www.sciencedirect.com/science/article/pii/S0020025521011804"
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