---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Towards Unifying Evaluation of Counterfactual Explanations: Leveraging Large Language Models for Human-Centric Assessments"
event: EMIL Spring'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  Since evaluation of counterfactual explanations is a difficult task, his paper tries to automate the process by fine-tuning large language models (LLMs) on human ratings for counterfactuals.
abstract: As machine learning models evolve, maintaining trans- parency demands more human-centric explainable AI tech- niques. Counterfactual explanations, with roots in human rea- soning, identify the minimal input changes needed to ob- tain a given output and, hence, are crucial for supporting decision-making. Despite their importance, the evaluation of these explanations often lacks grounding in user studies and remains fragmented, with existing metrics not fully captur- ing human perspectives. To address this challenge, we de- veloped a diverse set of 30 counterfactual scenarios and col- lected ratings across 8 evaluation metrics from 206 respon- dents. Subsequently, we fine-tuned different Large Language Models (LLMs) to predict average or individual human judg- ment across these metrics. Our methodology allowed LLMs to achieve an accuracy of up to 63% in zero-shot evaluations and 85% (over a 3-classes prediction) with fine-tuning across all metrics. The fine-tuned models predicting human ratings offer better comparability and scalability in evaluating differ- ent counterfactual explanation frameworks.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-01-15T12:30:00-07:00
date_end: 2025-01-15T12:55:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-01-15T18:50:20-07:00

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
url_slides: CountEval.pptx

url_code:
url_pdf: "https://arxiv.org/pdf/2410.21131"
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