---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "AutoEncoder based Detection of Insulin Pump Faults in Type 1 Diabetes Treatment"
event: EMIL Summer'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: This paper proposes a novel approach for detecting insulin pump faults (IPFs) by combining the ability of a long short term memory (LSTM) autoencoder to extract features with the strength of random forest to distinguish between anomalous and normal patterns.
abstract: Individuals with type 1 diabetes (T1D) require life long insulin replacement to compensate for deficient endogenous insulin secretion, which would otherwise result in abnormal blood glucose levels. In recent years, significant investments have been made to improve T1D management, leading to the widespread adoption of accurate technology such as continuous glucose monitoring (CGM) sensors and automated insulin delivery systems. However, malfunctions in these devices, particularly pump systems, can cause undesirable interruptions of insulin delivery posing significant safety risks if not promptly addressed. Due to the low frequency of these episodes, developing accurate algorithms to identify insulin pump faults remains a challenge. To address these issues, this paper proposes a novel approach for detecting insulin pump faults (IPFs) by combining the ability of a long short-term memory (LSTM) autoencoder to extract features, with the strength of random forest to distinguish between anomalous and normal patterns. This method was developed and evaluated using data from 100 subjects, simulated over 90 days with the UVa/Padova T1D Simulator, an FDA-approved nonlinear computer simulator of T1D physiology. In the test set, the proposed algorithm identified the 93% of the total faults, while raising 2 false alarms in 3 months on average. These findings suggest that deep learning algorithms can enhance the safety and reliability of insulin pump systems, contributing to more effective therapeutic technologies.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-07-23T12:00:00-07:00
date_end: 2025-07-23T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-07-23T19:45:00-07:00

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
url_pdf: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10803083
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
