---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "LLM-Guided Counterfactual Data Generation for Fairer AI"
event: EMIL Fall'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  This paper introduces a technique to produce synthetic counterfactual images to train a model free of bias.
abstract: With the widespread adoption of Deep Learning-based models in practical applications, concerns about their fairness have become increasingly prominent. Existing research indicates that both the model itself and the datasets on which they are trained can contribute to unfair decisions. In this paper, we address the data-related aspect of the problem, aiming to enhance the data to guide the model towards greater trustworthiness. Due to their uncontrolled curation and limited understanding of fairness drivers, real-world datasets pose challenges in eliminating unfairness. Recent findings highlight the potential of Foundation Models in generating substantial datasets. We leverage these foundation models in conjunction with state-of-the-art explainability and fairness platforms to generate counterfactual examples. These examples are used to augment the existing dataset, resulting in a more fair learning model. Our experiments were conducted on the CelebA and UTKface datasets, where we assessed the quality of generated counterfactual data using various bias-related metrics. We observed improvements in bias mitigation across several protected attributes in the fine-tuned model when utilizing counterfactual data.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-08-28T12:00:00-07:00
date_end: 2024-08-28T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-08-28T18:50:20-07:00

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
url_slides: LLM_guided_CFs.pptx

url_code:
url_pdf: "https://openreview.net/forum?id=GHb3qK0V3b"
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