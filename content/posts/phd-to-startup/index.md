---
title: "From Ph.D. to Startup: What Changed When I Stopped Writing Papers"
date: 2026-11-24
url: /posts/phd-to-startup/
summary: "I started a startup job a month before defending my Ph.D. Here's what changed: who decides the problem, what 'done' means, who checks the work, and which research habits turned out to matter."
tags:
    - career
    - research
---

I started a job at a startup in September 2025, a month before I defended my Ph.D. For a few weeks I was doing both: practicing a defense talk about occlusion-aware 3D reconstruction in the evenings, and during the day trying to make 3D work for people who would never read a paper.

A year in, these are the things that changed the most, and the things that didn't.

The first lesson came quickly. In a Ph.D., you start from an idea you find exciting and then look for the problem it solves best. At a startup it runs the other way. The business decides what problem matters, and research serves that. A clever idea that doesn't move the company toward its goals isn't useful, however good it would look in a paper.

## 1. "Done" means something different

In a Ph.D., a project is done when the method beats the baselines on a benchmark and the paper is accepted. The test set is fixed, and everyone in the field agrees on the metric.

In a product, nothing is fixed. The input is whatever a real person sends you, the metric is whether it looks right to them, and done means it works the hundredth time, not only the best time. A method that scores 2 points higher on average but fails badly on one input in twenty is worse, not better.

## 2. Research review isn't built in anymore

In a Ph.D., review is built in. Your advisor pushes back, labmates poke holes in your idea at group meeting, and reviewers tell you (sometimes harshly) what's missing.

At a small startup, the people around you judge whether something works for the product, not whether the research behind it holds up. If you make a wrong call about which approach to try, it often shows up only when it fails. So I've had to build the research review in myself: writing down what I expect before I run something, keeping small test sets of the hardest cases, and explaining my choices in plain words to a non-researcher. If I can't explain why I picked an approach, I usually haven't thought it through.

## 3. The clock runs differently

A paper can take a year on one idea. That depth is the point: you go after one question until you understand it completely.

At a startup the question is rarely "what's the best possible method?" It's "what's the simplest thing that's good enough to ship, and what will we learn from shipping it?" I spend much more time choosing what *not* to build. Some of the most useful work I've done this year was deciding to stop pursuing something.

## 4. What carried over

Not everything changed. Some Ph.D. habits turned out to be the most valuable things I brought:

- **Reading papers quickly.** When a problem comes up, there's usually a paper that's already worked on something close. Knowing how to find it and get the core idea in 30 minutes saves weeks. (I'll write a separate post on how I do that.)
- **Debugging math, not just code.** When a 3D pipeline gives wrong results, the bug is often a coordinate frame, a sign, or a wrong assumption about the camera, the same things I'm covering in the [Foundations tutorials](/posts/pinhole-camera/).
- **Writing clearly.** A Ph.D. is mostly practice in explaining hard ideas. That turns out to matter as much when the reader is a cofounder, a customer or a grant reviewer.
- **Research discipline.** This is the one I'd keep if I could keep only one. You state a hypothesis, change one thing at a time, compare against a baseline, and don't trust a result you can't reproduce. Under startup pressure it's tempting to tweak five things at once and ship whatever looks best. The discipline is what tells you *why* something worked, so you can rely on it next time.

## 5. What I'd tell someone finishing a Ph.D.

- Don't assume research only happens in academic labs. Industry needs researchers just as much, and sometimes more. Someone has to turn a hard problem into something that works, and that job is research.
- Your thesis topic matters less than you think; the way you learned to work matters more.
- Find out early what "done" means for the people you're building for, and test against that, not a benchmark.
- If you have few researchers around you, set up your own review: hard test cases, written predictions, and someone you explain your choices to.
- Keep a foot in research. I'm writing these posts partly to keep doing that.

---

*Previously: [Homogeneous coordinates](/posts/homogeneous-coordinates/). Next week: Foundations of 3D Vision, Part 3: intrinsics and extrinsics.*
