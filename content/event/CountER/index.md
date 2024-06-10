---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Counterfactual Explainable Recommendation"
event: EMIL Summer'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  CountER tells us under what conditions a chosen item would not be recommended to a person anymore. 
abstract: By providing explanations for users and system designers to facilitate better understanding and decision making, explainable recommendation has been an important research problem. In this paper, we propose Counterfactual Explainable Recommendation (CountER which takes the insights of counterfactual reasoning from causal inference for explainable recommendation. CountER is able to formulate the complexity and the strength of explanations, and it adopts a counterfactual learning framework to seek simple (low complexity) and effective (high strength) explanations for the model decision. Technically, for each item recommended to each user, CountER formulates a joint optimization problem to generate minimal changes on the item aspects so as to create a counterfactual item, such that the recommendation decision on the counterfactual item is reversed. These altered aspects constitute the explanation of why the original item is recommended. The counterfactual explanation helps both the users for better understanding and the system designers for better model debugging. Another contribution of the work is the evaluation of explainable recommendation, which has been a challenging task. Fortunately, counterfactual explanations are very suitable for standard quantitative evaluation. To measure the explanation quality, we design two types of evaluation metrics, one from user’s perspective (i.e. why the user likes the item), and theother from model’s perspective (i.e. why the item is recommended by the model). We apply our counterfactual learning algorithm on a black-box recommender system and evaluate the generated explanations on five real-world datasets. Results show that our model generates more accurate and effective explanations than state-of-the-art explainable recommendation models. 

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-05-28T15:00:00-07:00
date_end: 2024-05-28T15:40:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-05-28T18:50:20-07:00

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
url_slides: CountER.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2108.10539"
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