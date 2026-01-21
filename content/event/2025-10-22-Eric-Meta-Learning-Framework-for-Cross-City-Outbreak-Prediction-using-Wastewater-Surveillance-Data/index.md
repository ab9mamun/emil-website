---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Meta-Learning for County-Level COVID-19 Prevalence Prediction from Wastewater Surveillance Data"
event: EMIL Fall'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "The presentation proposes a meta-learning framework for cross-city outbreak prediction using wastewater-based epidemiology (WBE) data. The core objective is to develop a transferable model that can learn general outbreak patterns across multiple cities and rapidly adapt to new cities with limited local data. Focusing initially on COVID-19 due to data availability and standardized markers, the approach leverages meta-learning to address heterogeneity in data collection practices and temporal inconsistencies across regions. The proposed pipeline involves aggregating multi-city wastewater surveillance datasets, training a meta-learning model on shared trends, and evaluating performance by adapting the model to a held-out city and forecasting future disease activity. Key challenges discussed include inconsistent WBE measurements, missing or mislabeled data, and the difficulty of generalization across surveillance sites. The presentation argues that meta-learning directly targets these limitations and offers a realistic path toward scalable, early-warning outbreak prediction systems using wastewater data."
abstract: "This presentation outlines a research proposal for a meta-learning framework designed to predict infectious disease outbreaks across cities using wastewater-based epidemiology (WBE) data. The task is to train a model that captures generalizable outbreak dynamics from multiple cities and can be efficiently adapted to new locations with minimal data. The initial scope focuses on COVID-19, leveraging well-established and continuously updated datasets such as the CDC National Wastewater Surveillance System, EU Sewage Sentinel, and NORMAN-SCORE. Meta-learning is motivated as a solution to persistent challenges in WBE, including site-specific measurement differences, limited data availability, and poor cross-city generalization. The proposed methodology includes multi-city training, city-level adaptation, and comparison against city-specific baseline models to assess forecasting accuracy. The presentation highlights both feasibility and realism concerns, emphasizing that while data incompleteness remains a limiting factor, meta-learning provides a principled approach to improving robustness and transferability in wastewater-driven outbreak prediction."

# Talk start and end times.
# End time can optionally be hidden by prefixing the line with `#`.
date: 2025-10-22T12:00:00-07:00
date_end: 2025-10-22T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2026-01-21T11:00:00-07:00

authors: [eric-kim]
tags: []

# Is this a featured talk? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: Smart
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your talk's folder or a URL.
url_slides: slides.pptx
url_code:
url_pdf: 
url_video:

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: "slides"

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

