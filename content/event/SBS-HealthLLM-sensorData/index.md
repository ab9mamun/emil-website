---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Health-LLM: Large Language Models for Health Prediction via Wearable Sensor Data"
event: EMIL Spring'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  This paper proposes Health-LLM, a framework in the healthcare domain that aims to bridge the gap between pre-trained knowledge in current LLMs and consumer health problems.
abstract: "Large language models (LLMs) are capable of many natural language tasks, yet they are far from perfect. In health applications, grounding and interpreting domain-specific and non-linguistic data is crucial. This paper investigates the capacity of LLMs to make inferences about health based on contextual information (e.g. user demographics, health knowledge) and physiological data (e.g. resting heart rate, sleep minutes). We present a comprehensive evaluation of 12 state-of-the-art LLMs with prompting and fine-tuning techniques on four public health datasets (PMData, LifeSnaps, GLOBEM and AW_FB). Our experiments cover 10 consumer health prediction tasks in mental health, activity, metabolic, and sleep assessment. Our fine-tuned model, HealthAlpaca exhibits comparable performance to much larger models (GPT-3.5, GPT-4 and Gemini-Pro), achieving the best performance in 8 out of 10 tasks. Ablation studies highlight the effectiveness of context enhancement strategies. Notably, we observe that our context enhancement can yield up to 23.8% improvement in performance. While constructing contextually rich prompts (combining user context, health knowledge and temporal information) exhibits synergistic improvement, the inclusion of health knowledge context in prompts significantly enhances overall performance."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-07-17T12:00:00-07:00
date_end: 2024-07-17T12:40:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-07-17T16:50:20-07:00

authors: [shovito-barua-soumma]
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
url_slides: slides.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2401.06866"
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