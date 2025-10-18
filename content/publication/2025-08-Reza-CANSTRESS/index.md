---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "CAN-STRESS: A Real-World Multimodal Dataset for Understanding Cannabis Use, Stress, and Physiological Responses"
authors: [Reza Rahimi Azghan, Nicholas C. Glodosky, Ramesh Kumar Sah, Michael J. Cleveland, Carrie Cuttler, Ryan J. McLaughlin, Hassan Ghasemzadeh]
date: 2025-09-16T08:01:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2025-09-16T08:01:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE-EMBS International Conference on Body Sensor Networks"
publication_short: "BSN"

abstract: "Coping with stress is one of the most frequently cited reasons for chronic cannabis use. Therefore, it is hypothesized that cannabis users exhibit distinct physiological stress responses compared to non-users, and that these differences may be especially pronounced during moments of cannabis consumption. However, there is a scarcity of publicly available datasets that allow such hypotheses to be tested under real-world conditions. This paper introduces a dataset named CAN-STRESS, collected using Empatica E4 wristbands. The dataset includes multimodal physiological measurements (such as skin conductance, heart rate,and skin temperature) from 82 participants (39 cannabis users and 43 non-users) as they went about their daily routines. In addition to sensor data, participants provided self-reported survey responses that included perceived stress ratings and timestamps of key daily events such as cannabis use, physical activity, and sleep. To demonstrate the utility of the dataset for downstream applications, we present a preliminary machine learning task aimed at classifying cannabis users versus non-users based on physiological features. Our model achieves a classification accuracy of approximately 96% and an f1-score of around 98%. An analysis of feature importance using SHAP values revealed that electrodermal activity and heart rate metrics were the most influential predictors, consistent with their established roles in stress detection. We publicly release the CAN-STRESS dataset, which we believe serves as a reliable and rich resource for studying the physiological correlates of cannabis use and stress in naturalistic settings. "

# Summary. An optional shortened abstract.
summary: "The CAN-STRESS dataset provides multimodal physiological and self-reported data from 82 participants (39 cannabis users and 43 non-users) collected in real-world conditions using Empatica E4 wristbands. Preliminary analysis shows machine learning models can distinguish users from non-users with high accuracy, with electrodermal activity and heart rate emerging as key predictors."

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

url_pdf: https://drive.google.com/file/d/1iP0gJA7QOWK1z6n_KSMLR0lriC5G93YE/view?usp=sharing
url_code:
url_dataset: https://zenodo.org/records/14842061
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
projects: [mental-health]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
