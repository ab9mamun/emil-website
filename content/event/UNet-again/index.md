---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "U-Net: Convolutional Networks for Biomedical Image Segmentation"
event:
event_url:
location:
address:
  street:
  city:
  region:
  postcode:
  country:
summary: In this paper, the authors present a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more efficiently.
abstract: "There is large consent that successful training of deep networks requires many thousand annotated training samples. In this paper, we present a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more efficiently. The architecture consists of a contracting path to capture context and a symmetric expanding path that enables precise localization. We show that such a network can be trained end-to-end from very few images and outperforms the prior best method (a sliding-window convolutional network) on the ISBI challenge for segmentation of neuronal structures in electron microscopic stacks. Using the same network trained on transmitted light microscopy images (phase contrast and DIC) we won the ISBI cell tracking challenge 2015 in these categories by a large margin. Moreover, the network is fast. Segmentation of a 512x512 image takes less than a second on a recent GPU. The full implementation (based on Caffe) and the trained networks are available at https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-03-05T15:00:00-08:00
date_end: 2024-03-05T15:45:20-08:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2024-03-11T19:34:20-08:00

authors: [abdullah-mamun]
tags: []

# Is this a featured talk? (true/false)
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

# Optional filename of your slides within your talk's folder or a URL.
#url_slides: slides.pptx

url_code:
url_pdf: https://arxiv.org/abs/1505.04597
url_video:

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
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
