---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Computational Framework for Sequential Diet Recommendation: Integrating Linear Optimization and Clinical Domain Knowledge"
event: EMIL Fall'22 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: Optimizes change in consumed nutrients while driving users to their desired diet.
abstract: With rapid growth in unhealthy diet behaviors, implementing strategies that improve healthy eating is becoming increasingly important. One approach to improve diet behavior is to continuously monitor dietary intake (e.g., calorie intake) and provide educational, motivational, and dietary recommendation feedback. Although technologies based on wearable sensors, mobile applications, and light-weight cameras exist to gather diet-related information such as food type and eating time, there remains a gap in research on how to use such information to close the loop and provide feedback to the user to improve healthy diet. We address this knowledge gap by introducing a diet behavior change framework that generates real-time diet recommendations based on a user’s food intake and considering user’s deviation from the suggested diet routine. We formulate the problem of optimal diet recommendation as a sequential decision making problem and design a greedy algorithm that provides diet recommendations such that the amount of change in user’s dietary habits is minimized while ensuring that the user’s diet goal is achieved within a given time-frame. This novel approach is inspired by the Social Cognitive Theory, which emphasizes behavioral monitoring and small incremental goals as being important to behavior change. Our optimization algorithm integrates data from a user’s past dietary intake as well as the USDA nutrition dataset to identify optimal diet changes. We demonstrate the feasibility of our optimization algorithms for diet behavior change using real-data collected in two study cohorts with a combined N=10 healthy participants who recorded their diet for up to 21 days.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2022-11-14T11:00:00-07:00
date_end: 2022-11-14T12:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2022-11-14T12:50:20-07:00

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
url_slides: diet.pptx

url_code:
url_pdf: "https://drive.google.com/file/d/1-9-ZvlrbSpoxNDhRJevXPMQOtEP7vZlg/view"
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
