---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Blood Glucose Prediction With VMD and LSTM Optimized by Improved Particle Swarm Optimization"
event: EMIL Summer'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: In this work, the authors proposed a VMD-IPSO-LSTM model combining Variational Mode Decomposition and improved Particle Swarm Optimization with LSTM to enhance short-term blood glucose prediction accuracy.
abstract: "The time series of blood glucose concentration in diabetics are time-varying, nonlinear and nonstationary. To improve the accuracy of blood glucose prediction, a short-term blood glucose prediction model (VMD-IPSO-LSTM) combining variational modal decomposition (VDM) and improved Particle swarm optimization optimizing Long short-term memory network (IPSO-LSTM) was proposed. Firstly, the time series of blood glucose concentration of patients was decomposed by using VMD method to obtain the intrinsic modal functions (IMF) of blood glucose components in different frequency bands, so as to reduce the nonstationarity of blood glucose time series. Then a prediction model was established for each blood glucose component IMF by using the long and short time memory network. Since the number of neurons, learning rate and time window length of LSTM are difficult to determine, the improved PSO algorithm is used to optimize these parameters. The optimized LSTM network was used to predict each IMF, and finally the predicted subsequence was superimposed to obtain the final prediction result. The data of 56 patients were selected as experimental data from 451 patients with diabetes mellitus. The experimental results showed that the proposed VMD-IPSO-LSTM model could achieve high prediction accuracy at 30min, 45min and 60min in advance. When predicted 60 minutes in advance, compared with the LSTM, VMD-LSTM and VMDPSO-LSTM methods, the RMSE of proposed method decreased by 15.565,3.402,1.215 and the MAPE of proposed method decreased by 11.284%,2.024%, 0.834%, and the percentage of predicted values falling into the A zone increased by 23.5%,6.1% and 2.8% in the Clarke error grid, respectively. The improved accuracy of blood glucose prediction and longer prediction time can provide sufficient time for physicians and patients to control blood glucose concentrations and improve the effectiveness of diabetes treatment"
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-11-31T12:00:00-07:00
date_end: 2024-11-31T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate:  2025-03-28T14:28:20-07:00

authors: [Ebrahim-Farahmand]
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
url_slides: self_supervised_from_EEG.pdf

url_code:
url_pdf: https://arxiv.org/pdf/1911.05419
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
