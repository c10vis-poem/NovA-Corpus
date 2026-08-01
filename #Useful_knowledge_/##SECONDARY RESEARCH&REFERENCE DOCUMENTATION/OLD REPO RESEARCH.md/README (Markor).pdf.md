# README (Markor)

OmniNeural — World’s First NPU-aware Multimodal Model
(Mobile Version)
Overview
OmniNeural is the first fully multimodal model designed specifically for Neural Processing Units (NPUs). It
natively understands text, images, and audio, and runs across PCs, mobile devices, automobile, IoT, and
robotics.
Demos
📱 Mobile Phone NPU - Demo on Samsung S25 Ultra
The first-ever fully local, multimodal, and conversational AI assistant that hears you and sees what you see,
running natively on Snapdragon NPU for long battery life and low latency.
Key Features
0:00 / 1:44

Multimodal Intelligence – Processes text, image, and audio in a unified model for richer reasoning and
perception.
NPU-Optimized Architecture – Uses ReLU ops, sparse tensors, convolutional layers, and static graph
execution for maximum throughput — 20% faster than non-NPU-aware models .
Hardware-Aware Attention – Attention patterns tuned for NPU, lowering compute and memory demand
.
Native Static Graph – Supports variable-length multimodal inputs with stable, predictable latency .
Performance Gains – 9× faster audio processing and 3.5× faster image processing on NPUs compared
to baseline encoders .
Privacy-First Inference – All computation stays local: private, offline-capable, and cost-efficient.
Performance / Benchmarks
Human Evaluation (vs baselines)
Vision: Wins/ties in ~75% of prompts against Apple Foundation, Gemma-3n-E4B, Qwen2.5-Omni-3B.
Audio: Clear lead over baselines, much better than Gemma3n and Apple foundation model.
Text: Matches or outperforms leading multimodal baselines.
Nexa Attention Speedups
9× faster audio encoding (vs Whisper encoder).
3.5× faster image encoding (vs SigLIP encoder).
Architecture Overview

OmniNeural’s design is tightly coupled with NPU hardware:
NPU-friendly ops (ReLU > GELU/SILU).
Sparse + small tensor multiplications for efficiency.
Convolutional layers favored over linear for better NPU parallelization.
Hardware-aware attention patterns to cut compute cost.
Static graph execution for predictable latency.
Production Use Cases
PC & Mobile – On-device AI agents combine voice, vision, and text for natural, accurate responses.
Examples: Summarize slides into an email (PC)*, *extract action items from chat (mobile).
Benefits: Private, offline, battery-efficient.
Automotive – In-car assistants handle voice control, cabin safety, and environment awareness.
Examples: Detects risks (child unbuckled, pet left, loose objects) and road conditions (fog,
construction).
Benefits: Decisions run locally in milliseconds.
IoT & Robotics – Multimodal sensing for factories, AR/VR, drones, and robots.
Examples: Defect detection, technician overlays, hazard spotting mid-flight, natural robot
interaction.
Benefits: Works without network connectivity.
How to use

Note this version is for mobile only (Android). See documentation for how to use:
Quickstart
Links & Community
Discord
Discord Join
Join
Follow
Follow @nexa ai
@nexa ai
Website
Website nexa.ai
nexa.ai
Issues / Feedback: Use the HF Discussions tab or submit an issue in our discord or nexa-sdk github.
Roadmap & updates: Follow us on X and Discord.
If you want to see more NPU-first, multimodal releases on HF, please give our model a like ❤️.
Limitation
The current model is mainly optimized for English. We will optimize other language as the next step.
Citation
License
This model is released under the Creative Commons Attribution–NonCommercial 4.0 (CC BY-NC 4.0) license.
Non-commercial use, modification, and redistribution are permitted with attribution.
For commercial licensing, please contact dev@nexa.ai.
@misc{
      title={OmniNeural: World’s First NPU-aware Multimodal Model}, 
      author={Nexa AI},
      year={2025},
      url={https://huggingface.co/NexaAI/OmniNeural-4B}, 
}

## Extracted images

(pulled from the source doc by `.migrate/extract_images.py` -- Markdown conversion drops these; see `README (Markor).pdf_images/`)

- ![embedded raster](README (Markor).pdf_images/image-0004.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0006.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0014.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0021.jpg) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0028.jpg) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0043.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0044.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0045.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0046.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0053.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0054.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0065.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0066.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0068.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0069.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0075.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0076.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0077.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0078.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0084.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0085.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0086.png) -- embedded raster
- ![embedded raster](README (Markor).pdf_images/image-0087.png) -- embedded raster
- ![page 1 render (44 vector ops)](README (Markor).pdf_images/page-1-diagram.png) -- page 1 render (44 vector ops)
- ![page 2 render (46 vector ops)](README (Markor).pdf_images/page-2-diagram.png) -- page 2 render (46 vector ops)
- ![page 3 render (52 vector ops)](README (Markor).pdf_images/page-3-diagram.png) -- page 3 render (52 vector ops)
- ![page 4 render (56 vector ops)](README (Markor).pdf_images/page-4-diagram.png) -- page 4 render (56 vector ops)
