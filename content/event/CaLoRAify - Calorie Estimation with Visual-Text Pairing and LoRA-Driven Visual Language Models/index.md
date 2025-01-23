---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "CaLoRAify - Calorie Estimation with Visual-Text Pairing and LoRA-Driven Visual Language Models"
event: EMIL Spring'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: This presentation discusses a novel VLM framework aligning ingredient recognition and calorie estimation via training with visual text pairs.
abstract: The obesity phenomenon, known as the heavy issue, is a leading cause of preventable chronic diseases worldwide. Traditional calorie estimation tools often rely on specific data formats or complex pipelines, limiting their practicality in real-world scenarios. Recently, vision-language models (VLMs) have excelled in understanding real-world contexts and enabling conversational interactions, making them ideal for downstream tasks such as ingredient analysis. However, applying VLMs to calorie estimation requires domain-specific data and alignment strategies. To this end, we curated CalData, a 330K image-text pair dataset tailored for ingredient recognition and calorie estimation, combining a large-scale recipe dataset with detailed nutritional instructions for robust vision-language training. Built upon this dataset, we present CaLoRAify, a novel VLM framework aligning ingredient recognition and calorie estimation via training with visual-text pairs. During inference, users only need a single monocular food image to estimate calories while retaining the flexibility of agent-based conversational interaction. With Low-rank Adaptation (LoRA) and Retrieve-augmented Generation (RAG) techniques, our system enhances the performance of foundational VLMs in the vertical domain of calorie estimation.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-01-08T12:00:00-07:00
date_end: 2025-01-08T13:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-01-10T20:40:00-07:00

authors: [saman-khamesian]
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
url_pdf: "https://arxiv.org/abs/2412.09936"
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
