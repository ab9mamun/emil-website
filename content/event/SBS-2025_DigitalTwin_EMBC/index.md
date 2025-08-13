---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Digital-twin based optimization of bolus insulin dosing in pediatric type 1 diabetes: an in silico feasibility study"
event: EMIL Summer'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  This paper proposes DT-based MIB optimization framework to assist clinicians during routine visits with pediatric T1D patients by optimizing insulin therapy on a biweekly basis

abstract: "Type 1 diabetes (T1D) is a chronic condition affecting pancreatic insulin production, thus requiring lifelong exogenous insulin therapy to maintain blood glucose within a safe range. While continuous glucose monitoring (CGM) and other technological advancements have improved its management, clinicians still struggle to achieve good glycemic control in pediatric patients due to their evolving physiology and metabolic variability, which necessitate frequent therapy adjustments. To address this challenge, this work present a therapy optimization algorithm leveraging digital twins (DTs) to biweekly adapt the state-of-art meal insulin bolus (MIB) formula proposed by Noaro et al., ensuring its personalization based on patients’ changing metabolic dynamics estimated by DTs. The algorithm has been testes in a 24-week in silico trial involving five pediatric patients from the Tidepool Big Data Donation project, comprising 724 daily CGM traces. Biweekly optimization was performed using a derivative-free algorithm to minimize the glycemia risk index (GRI), an overall risk metric for the patient, by adjusting MIBs via personalized modulation parameters. The proposed approach demonstrated an increasing trend of the time spent in the euglycemic range (+0.63% every two weeks), and a decreasing trend of the time spent in hyperglycemia (-0.18% every two weeks) and of GRI (-0.64 every two weeks). These findings highlight the potential of the proposed approach to improve glucose control over time, thus to support clinicians in providing tailored, frequent datadriven therapy adjustments for pediatric patients, addressing the unique demands of this population."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-07-23T12:00:00-07:00
date_end: 2025-07-23T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-07-23T12:00:00-07:00

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
url_slides: 10-DigitalTwin_EMBC.pptx

url_code:
url_pdf: 
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