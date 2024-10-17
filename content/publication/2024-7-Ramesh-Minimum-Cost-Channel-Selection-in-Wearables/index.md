---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Minimum-Cost Channel Selection in Wearables"
authors: [Ramesh Kumar Sah, Nooshin Taheri Chatrudi, Stephanie Marita Carpenter, Hassan Ghasemzadeh]
date: 2024-07-31T08:01:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2024-07-31T08:01:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE-EMBS International Conference on Body Sensor Networks: NextGen Health: Sensor Innovation, AI, and Social Responsibility (BSN'24)"
publication_short: "IEEE BSN 2024"

abstract: "Sensor channel selection is an important optimization problem in resource-constrained wearable systems with the goal of identifying an optimal set of input sensors for efficient machine learning. We introduce a framework for this optimization problem, mathematically formulate the minimum-cost channel selection (MCCS), and propose two novel algorithms to solve the problem. Branch and bound channel selection finds a globally optimal channel subset and the greedy channel selection finds the best intermediate subset based on our proposed penalty function. These proposed channel selection algorithms are conditioned with both performance and the cost of the channel subset. We evaluate both algorithms on two publicly available time series datasets for activity recognition and mental task classification. Branch and bound channel selection achieve a cost saving between 92.6% and 95.7%, and the greedy approach reduces the cost between 51.8% and 91.4%, for performance thresholds of 50% and 70%."

# Summary. An optional shortened abstract.
summary: "We introduce a framework for the channel selection problem, mathematically formulate the minimum-cost channel selection (MCCS), and propose two novel algorithms to solve the MCCS problem."

tags: ["featured"]
categories: []
featured: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: "papers/BSN_Channel_Selection_Final_Camera_Ready_Version.pdf"
url_code: 
url_dataset:
url_poster:
url_project:
url_slides: 
url_source:
url_video: 

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: ["Edge-AI"]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
