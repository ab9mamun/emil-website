---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
event: EMIL Fall'26 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:

summary: "Reflexion is a framework that enables language agents to learn from trial-and-error through verbal feedback rather than model weight updates. The agent reflects on feedback from previous attempts, stores these reflections in episodic memory, and uses them to improve future decision-making, reasoning, and programming tasks."

abstract: "Large language models (LLMs) have been increasingly used to interact with external environments such as games, compilers, and APIs as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error because traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. Reflexion introduces a framework that reinforces language agents not by updating model weights, but through linguistic feedback. Reflexion agents verbally reflect on task feedback signals and maintain their reflective text in an episodic memory buffer to improve decision-making in subsequent trials. The framework can incorporate different types and sources of feedback, including scalar values, free-form language, external feedback, and internally simulated feedback. Experiments across sequential decision-making, reasoning, and programming tasks demonstrate substantial improvements over baseline agents. Reflexion achieves 91% pass@1 accuracy on the HumanEval coding benchmark and also improves performance on ALFWorld and HotPotQA. The results demonstrate how verbal self-reflection and persistent memory can allow language agents to learn from previous failures without model fine-tuning."

# Talk start and end times.
# End time can optionally be hidden by prefixing the line with `#`.
date: 2026-09-23T12:00:00-07:00
date_end: 2026-09-23T12:50:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2026-09-25T11:00:00-07:00

authors: [Pegah Khorasani]
tags: []

# Is this a featured event? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ""
  focal_point: ""
  preview_only: false

url_slides: slides.pdf

url_code: https://github.com/noahshinn024/reflexion
url_pdf: https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf
url_video:

slides: ""

projects: []
---