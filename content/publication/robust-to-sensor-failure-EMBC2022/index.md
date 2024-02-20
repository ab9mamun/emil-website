---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Designing Deep Neural Networks Robust to Sensor Failure in Mobile
Health Environments"
authors: [Abdullah Mamun, Iman Mirzadeh, Hassan Ghasemzadeh]
date: 2022-03-31T01:22:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2022-03-31T01:22:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Engineering in Medicine and Biology Conference (EMBC), 2022"
publication_short: ""

abstract: "Missing data is a very common challenge in health monitoring systems and one reason for that is that they are largely dependent on different types of sensors. A critical characteristic of the sensor-based prediction systems is their dependency on hardware, which is prone to physical limitations that add another layer of complexity to the algorithmic component of the system. For instance, it might not be realistic to assume that the prediction model has access to all sensors at all times. This can happen in the real-world setup if one or more sensors on a device malfunction or temporarily have to be disabled due to power limitations. The consequence of such a scenario is that the model faces “missing input data” from those unavailable sensors at the deployment time, and as a result, the quality of prediction can degrade significantly. While the missing input data is a very well-known problem, to the best of our knowledge, no study has been done to efficiently minimize the performance drop when one or more sensors may be unavailable for a significant amount of time. The sensor failure problem investigated in this paper can be viewed as a spatial missing data problem, which has not been explored to date. In this work, we show that the naive known methods of dealing with missing input data such as zero-filling or mean-filling are not suitable for senors-based prediction and we propose an algorithm that can reconstruct the missing input data for unavailable sensors. Moreover, we show that on the MobiAct, MotionSense, and MHEALTH activity classification benchmarks, our proposed method can outperform the baselines by large accuracy margins of 8.2%, 15.1%, and 11.6%, respectively."

# Summary. An optional shortened abstract.
summary: "We propose an algorithm that can reconstruct the missing input data for unavailable sensors."

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

url_pdf: https://drive.google.com/file/d/1YRJXUPZrER2jHfG7Ru6D6wbw67FbVzOk/view?usp=sharing
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
projects: ["Computational-Autonomy"]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
