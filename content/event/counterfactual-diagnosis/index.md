---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Counterfactual diagnosis"
event: EMIL Summer'23 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  "inability to recognize counterrfactual diagnosis from associative diagnosis can lead to disastrous outcomes."
abstract: "Machine learning promises to revolutionize clinical decision making and diagnosis. In medical diagnosis a doctor aims to explain a patient’s symptoms by determining the diseases causing them. However, existing diagnostic algorithms are purely associative, identifying diseases that are strongly correlated with a patients symptoms and medical history. We show that this inability to disentangle correlation from causation can result in sub-optimal or dangerous diagnoses. To overcome this, we reformulate diagnosis as a counterfactual inference task and derive new counterfactual diagnostic algorithms. We show that this approach is closer to the diagnostic reasoning of clinicians and significantly improves the accuracy and safety of the resulting diagnoses. We compare our counterfactual algorithm to the standard Bayesian diagnostic algorithm and a cohort of 44 doctors using a test set of clinical vignettes. While the Bayesian algorithm achieves an accuracy comparable to the average doctor, placing in the top 48% of doctors in our cohort, our counterfactual algorithm places in the top 25% of doctors, achieving expert clinical accuracy. This improvement is achieved simply by changing how we query our model, without requiring any additional model improvements. Our results show that counterfactual reasoning is a vital missing ingredient for applying machine learning to medical diagnosis."
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2023-11-22T13:30:00-07:00
date_end: 2023-11-22T15:00:00-07:00
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
url_pdf: "https://arxiv.org/pdf/1910.06772.pdf"
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
