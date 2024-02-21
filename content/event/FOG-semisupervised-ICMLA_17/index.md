---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Real-Time Patient Adaptivity for Freezing of Gait Classification Through Semi-Supervised Neural Networks"
event: EMIL Spring'24 Seminars
event_url:
location: Health Futures Center, ASU
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  This presentation presents semi-supervised neural network for freezing of gait classification.
abstract: "Freezing of gait (FoG) is a sudden and episodic inability to generate effective stepping among Parkinson’s disease patients. It poses a risk for falls and deteriorates a patient’s quality of life. Aid is sought after by the implementation of wearable systems that detect FoG and provide biofeedback cues in real-time. Detection is predominantly attempted with patientindependent classifiers which have difficulties to account for some patient’s inimitable walking styles. Such gait peculiarities can be addressed with patient-adaptive classifiers. However, the patient-specific adaptations proposed thus far are retrospective and require a patient’s labeled data. We propose to provide patient adaptivity in real-time through semi-supervised neural networks which exploit the stream of unlabeled data generated during usage. Using supervised learning, a patient-independent neural network is designed to serve as a base model. Upon a new patient’s utilization of the system, the base model’s parameters are adapted in real-time through unsupervised learning from the generated stream of unlabeled data. On average, patient adaptivity augmented sensitivity by 4.58% for the price of 0.59% in specificity. Moreover, it accounted for inimitable walking styles of patients that had been inadequately classified by the patientindependent base model. For such patients, sensitivity increased up to 42.01%. The overall patient-adaptive classifier resulted in 95.90% and 93.05% in sensitivity and specificity, respectively."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-02-20T15:00:00-07:00
date_end: 2024-02-20T15:40:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-02-20T18:50:20-07:00

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
url_pdf: "https://ieeexplore.ieee.org/abstract/document/8260746"
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