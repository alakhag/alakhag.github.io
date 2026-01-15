---
layout: archive
title: "Resume"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<hr>

## Education
* Ph.D in 3D Vision, University of Texas at Dallas, 2025 (Supervisor: [Dr. Xiaohu Guo](https://personal.utdallas.edu/~xguo/))
* B.Tech. (Hons.) AI/CV Stream, CSE Department, IIT (BHU) Varanasi, India, 2019

<hr>

## Work experience
* Present: Research Engineer
  * Digi-Clone
  * Duties included: Technical MVP, Cloth Simulation and Draping

* Summer 2017: Research Assistant
  * IIT Gandhinagar
  * Duties included: Synthetic data generation, Object Localization, Improving the performance of Faster RCNN
  * Supervisor: [Dr. Ravi Hegde](https://www.iitgn.ac.in/faculty/electrical/ravi.htm)

* Summer 2018: Research Intern
  * Samsung (Research & Development) Institute Bangalore
  * Duties included: Cleaning Lip-Reading Dataset, Accurate Lip-Reading from Mobile Devices
  * Supervisor: [Dr. Shankar Venkatesan](https://scholar.google.com/citations?user=HFm0RpIAAAAJ&hl=en)
<hr>

<div class="one_section">
  <h2 style="padding: 1em;"><u>Publications</u></h2>
  <ul>{% for post in site.publications reversed %}{% include archive-single-cv.html %}{% endfor %}</ul>
<br>
</div>

<hr>
  
<div class="one_section">
  <h2 style="padding: 1em;"><u>Teaching</u></h2>
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
<br>
</div>

<hr>

<div class="one_section">
  <h2 style="padding: 1em;"><u>Talks</u></h2>
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
<br>
</div>
