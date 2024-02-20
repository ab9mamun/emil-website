---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Personalized Modeling and Detection of Moments of Cannabis Use in Free-Living Environments"
authors: [Reza Rahimi Azghan, Nicholas C. Glodosky, Ramesh Kumar Sah, Carrie Cuttler, Ryan McLaughlin, Michael J. Cleveland, Hassan Ghasemzadeh]
date: 2023-07-31T08:01:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2023-07-31T08:01:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE-EMBS International Conference on Body Sensor Networks: Sensor and Systems for Digital Health (BSN'23)"
publication_short: "IEEE BSN 2023"

abstract: "Coping with stress is reportedly one of the main reasons for chronic cannabis use. Developing a real-time system that offers cannabis users alternative methods to cope with stress is of interest in medical applications. To develop such a system, it is necessary to design a reliable mechanism for identifying cannabis use sessions in uncontrolled environments using physiological markers captured with wearable sensors. Therefore, the primary objective of this study is to design a system that can identify sessions of cannabis consumption by utilizing one of the most significant biomarkers of stress, Electrodermal Activity (EDA). We conducted a user study to collect physiological sensor data in real-life setting. We then model the cannabis use detection as a supervised learning problem and train a neural network model. To improve the performance of the proposed model for a specific subject, transfer learning techniques were used to retrain the base model on the new user data. Trained model achieved average f1-score of 0.68 and accuracy of 71.58% on the test data from Leave One Subject Out (LOSO) analysis. After applying transfer learning, the retrained model achieved average f1-score of 0.8 and accuracy of 83.61% when detecting the cannabis consumption period for the same subjects"

# Summary. An optional shortened abstract.
summary: "We use an MLP model to identify and detect moments of cannabis use. We later use transfer learning to further enhance model accuracy."

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

url_pdf: https://drive.google.com/file/d/1B1wnLnU2F08Anbw3Zdu8YfSqI54EsOxz/view?usp=drive_link
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
projects: ["Mental-Health"]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
