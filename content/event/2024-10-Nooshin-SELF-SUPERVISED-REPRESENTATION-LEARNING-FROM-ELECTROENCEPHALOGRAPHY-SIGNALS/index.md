---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Minimum-Cost Channel Selection in Wearables"
event: EMIL Fall'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: In this work, we introduce a framework for this optimization problem, mathematically formulate the minimum cost channel selection (MCCS), and propose two novel algorithms to solve the MCCS problem.
abstract: "Sensor channel selection is an important optimization problem in resource-constrained wearable systems with the goal of identifying an optimal set of input sensors for efficient machine learning. We introduce a framework for this optimization problem, mathematically formulate the minimum cost channel selection (MCCS), and propose two novel algorithms to solve the MCCS problem. Branch and bound channel selection finds a globally optimal channel subset and the greedy channel selection finds the best intermediate subset based on our proposed penalty function. These proposed channel selection algorithms are conditioned with both performance and the cost of the channel subset. We evaluate both algorithms on two publicly available time series datasets for activity recognition and mental task classification. Branch and bound channel selection achieves a cost saving between 92.6% and 94.8%, and the greedy approach reduces the cost between 51.8% and 89.6% for performance thresholds of 50% and 70%."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-10-02T12:00:00-07:00
date_end: 2024-10-02T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2024-10-02T19:34:20-07:00

authors: [nooshin-taheri-chatrudi]
tags: []

# Is this a featured talk? (true/false)
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

# Optional filename of your slides within your talk's folder or a URL.
url_slides: channel_selection.pdf

url_code:
url_pdf: "https://ghasemzadeh.com/papers/BSN_Channel_Selection_Final_Camera_Ready_Version.pdf"
url_video:

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
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
