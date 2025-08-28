---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "LEAD: Localized Explanations with Adversarial Decision Boundary Characterization for Interpretable Disease Prediction"
event: EMIL Summer'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: LEAD is an explainable AI approach that perturbs synthetic critical samples to generate consistent, sparse and robust explanations for disease classification.
abstract: Understanding the reasoning behind a model's decision-making process is highly sought after in safety-critical domains like digital health where predicting the onset of a disease or occurrence of an adverse outcome if desirable. Gaining insights into what drives a model to a specific decision enhances interpretability, trust, and acceptance. Furthermore, model's decision making process helps end-users (i.e., patients, caregivers, clinicians) make appropriate decisions to prevent an impending adverse clinical outcome. This paper introduces LEAD, a novel method for generating localized feature explanations by perturbing adversarial critical samples near the sample to be explained. By focusing on neighboring critical samples along the decision boundary—rather than on the test sample directly—LEAD reduces the impact of noise or irrelevant features on feature importance estimation. Additionally, leveraging these borderline instances enhances robustness against adversarial attacks. Our extensive experiments on two datasets with physiological signal sensing features showcase the effectiveness of LEAD with at least 6% improved fidelity, 7% improved consistency, high sparsity, and competitive robustness, compared to those of the competing explainable AI techniques.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-05-28T12:00:00-07:00
date_end: 2025-05-28T12:25:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-05-28T16:40:20-07:00

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
url_slides: LEAD EMBC 2025.pptx

url_code:
url_pdf: "https://drive.google.com/file/d/1rOHJCB4C_7bM7M1ZdDH35HR8Q_bxx8XX/view?usp=sharing"
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