---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Boosting Lying Posture Classification with Transfer Learning"
event: EMIL Summer'22 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: Enhancement of accuracy for wrist-worn sensor based lying posture classification via transfer learning 
abstract: Automatic lying posture tracking is an important factor in human health monitoring. The increasing popularity of the wrist-based trackers provides the means for unobtrusive, affordable, and long-term monitoring with minimized privacy concerns for the end-users and promising results in detecting the type of physical activity, step counting, and sleep quality assessment. However, there is limited research on development of accurate and efficient lying posture tracking models using wrist-based sensor. Our experiments demonstrate a major drop in the accuracy of the lying posture tracking using wrist-based accelerometer sensor due to the unpredictable noise from arbitrary wrist movements and rotations while sleeping. In this paper, we develop a deep transfer learning method that improves performance of lying posture tracking using noisy data from wrist sensor by transferring the knowledge from an initial setting which contains both clean and noisy data. The proposed solution develops an optimal mapping model from the noisy data to the clean data in the initial setting using LSTM sequence regression, and reconstruct clean synthesized data in another setting where no noisy sensor data is available. This increases the lying posture tracking F1-Score by $24.9\%$ for `left-wrist' and by $18.1\%$ for `right-wrist' sensors comparing to the case without mapping.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2022-06-10T12:00:00-07:00
date_end: 2022-06-10T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2022-06-10T16:07:03-07:00

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
url_slides: BLPC.pptx

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
