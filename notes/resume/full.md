# Alakh Aggarwal

**Research Engineer | 3D Computer Vision | Generative AI | Ph.D.**

Dallas, TX | +1 (214) 606-4870 | alakh1997@gmail.com | [alakhaggarwal.com](https://alakhaggarwal.com)

[linkedin.com/in/alakh-aggarwal](https://www.linkedin.com/in/alakh-aggarwal/) | [github.com/alakhag](https://github.com/alakhag) | [scholar.google.com/citations?user=X9XBBCcAAAAJ](https://scholar.google.com/citations?user=X9XBBCcAAAAJ)

## Summary

Research engineer with a Ph.D. in Computer Science, specializing in 3D reconstruction, neural scene representations, and generative AI. CVM 2025 Best Paper Award winner (\~200 citations) who owns R&D at Digi-Clone, building the 3D body estimation, garment registration, and cloth simulation pipelines for an NSF SBIR Phase I-funded virtual try-on product.

## Work Experience

**Senior Research Engineer**, Digi-Clone Ltd Co, Remote (Atlanta, GA) | Sep 2025 – Present

- Own all R&D for a 3D virtual try-on product as the company's **sole research engineer**, leading the R&D funded by the company's **NSF SBIR Phase I award**; built the technical MVP and planning Phase II R&D.
- Built an image-based 3D shape estimation service that fits a parametric body model (MHR) from just two photos and tape measurements.
- Built **semi-automatic garment registration** that places sewing-pattern panels onto a 3D body surface, applied across 15 garments with no hand-tuned placement rules.
- Built cloth draping simulation and body morphing for size-graded garments; draping validated on **15 garments** across women's and men's lines: every draped seam closes within 8.6 mm, **13 of 15 have zero body penetration** (at most 2 vertices otherwise), and mean fabric stretch stays under 1.2×.
- Formulated SDF-based energy minimization in PyTorch to register deformable meshes to target surfaces, addressing lateral misalignment from nearest-surface fitting.
- Designed the company-wide evaluation framework for the SBIR Phase I report, covering output quality, system health, and business and user impact.

**Graduate Research Assistant**, The University of Texas at Dallas, Dallas, TX | Aug 2019 – Oct 2025

- Dissertation: *Learning Complex Occlusion-Aware 3D Representations from Human-Object Interactions.* Advisor: Dr. Xiaohu Guo, Computer Graphics and Animation Lab.
- Created **TexHOI**, which reconstructs the geometry and appearance of previously unseen objects from monocular video of hand-object interaction, handling heavy occlusion by the hand; won the **CVM 2025 Best Paper Award** (IEEE TVCG).
- Built NeRF and **3D Gaussian Splatting** reconstruction pipelines on COLMAP Structure-from-Motion camera poses, modeling complex lighting and reflections to recover object properties under uncontrolled illumination.
- Significantly reduced rendering compute cost by implementing Spherical Gaussians with visibility estimation in CUDA C++.
- Applied latent diffusion models to recover missing and degraded visual data: deblurring, inpainting occluded regions, and synthesizing unseen views.
- Built Layered-Garment Net, which infers multiple intersection-free 3D garment layers from a single image using implicit SDFs (ACCV 2022).

**Research Intern**, Samsung Research Institute, Bangalore, India | May 2018 – Jul 2018

- Built a pose-invariant lip-reading system combining Active Appearance Models for features with GMM-HMMs for sequence modeling, improving speech recognition in noisy environments.
- Cleaned and curated the lip-reading dataset, and optimized the pipeline in C++ and OpenCV for low-latency on-device deployment.

**Research Fellow**, IIT Gandhinagar, Gandhinagar, India | May 2017 – Jul 2017

- Fine-tuned pretrained CNN object detectors (Faster R-CNN) entirely on synthetic data, **doubling mAP** on real-world evaluation sets and closing the Sim2Real gap; the paper has 100+ citations (NCVPRIPG 2017).
- Built an automated synthetic data pipeline in Python and the Blender API to generate large-scale labeled 3D datasets.

## Education

- **Ph.D., Computer Science**, The University of Texas at Dallas, Dallas, TX | Aug 2019 – Oct 2025 | GPA 4.0
- **B.Tech (Hons.), Computer Science and Engineering**, IIT (BHU) Varanasi | Jul 2015 – Jun 2019 | CPI 9.13/10
- Undergraduate research: GAN-based face de-identification (IEEE IEMTRONICS 2020) and aerial change detection (IEMGraph 2018).

## Skills

- **3D Reconstruction:** 3D Gaussian Splatting, NeRF, Structure-from-Motion (COLMAP), monocular and multi-view reconstruction, signed distance fields, inverse rendering, Spherical Gaussians
- **3D Perception & Geometry:** Occlusion-aware scene understanding, object pose and shape estimation, parametric body models (MHR), registration and model fitting, multi-view geometry
- **Generative AI:** Latent diffusion models, GANs, generative image and video APIs (Gemini, Veo), LLM agents with tool calling (MCP)
- **Learning & Evaluation:** Deep learning, object detection, Sim2Real and domain adaptation, synthetic data generation, metric design and model evaluation
- **Optimization & Simulation:** Energy minimization, differentiable optimization in PyTorch, physics-based cloth simulation, real-time rendering
- **Programming:** Python, C++, CUDA C, SQL, Java
- **Frameworks & Tools:** PyTorch, TensorFlow, OpenCV, OpenGL, FastAPI, PostgreSQL (Supabase), Unreal Engine, Unity, Blender, CLO3D, Style3D, MeshLab

## Publications

- TexHOI: Reconstructing Textures of 3D Unknown Objects in Monocular Hand-Object Interaction Scenes. *IEEE TVCG*, 2025 (CVM 2025 Best Paper Award).
- Layered-Garment Net: Generating Multiple Implicit Garment Layers from a Single Image. *ACCV*, 2022.
- EPD-Net: A GAN-based Architecture for Face De-identification from Images. *IEEE IEMTRONICS*, 2020.
- Broad Neural Network for Change Detection in Aerial Images. *IEMGraph 2018*, Springer AICS, 2020.
- Transfer Learning by Finetuning Pretrained CNNs Entirely with Synthetic Images. *NCVPRIPG 2017*, Springer CCIS, 2018.

## Selected Projects

**Autonomous Underwater Vehicle: Vision-Based Navigation** | Fall 2017 – Fall 2019

- Built a traditional computer vision pipeline that extracted features from onboard fisheye cameras for target localization and navigation prediction.
- Deployed it on the real vehicle, integrated with PID-controlled motors.

## Awards & Honors

- Best Paper Award, Computational Visual Media (CVM) 2025
- Betty and Gifford Johnson Travel Award, The University of Texas at Dallas, 2025
- Champion, Technex Robosoccer, IIT (BHU) Varanasi, 2016
