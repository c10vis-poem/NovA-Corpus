# c10vis-poem／ai-hub-merovingian-models-: Qualcomm® AI Hub Models is our collection of state-of-the-art machine learning models optimized for performance (latency, memory etc.) and ready to deploy on Qualcomm® devices.

Watch
0
Qualcomm® AI Hub Models is our collection of state-of-the-art machine learning models optimized for performance (latency, memory etc.) and
ready to deploy on Qualcomm® devices.
BSD 3-Clause "New" or "Revised" License
aihub.qualcomm.com/models
Code of conduct
Contributing
0 stars
0 forks
0 watching
2 branches
0 tags
Activity
Public repository · Forked from qualcomm/ai-hub-models
Your main branch isn't protected
Protect this branch from force pushing or deletion, or require status checks before merging. View
documentation.
Dismiss
Protect this branch
2 Branches
0 Tags
Go to file
Go to file
Add file
Code
This branch is 2 commits ahead of qualcomm/ai-hub-models:main .
Contribute
Sync fork
c10vis-poem Merge branch 'qualcomm:main' into main
d14476c · now
.breeze
Add scorecard regression analysis agent (#…
last month
.claude
[Auto] Weekly triage KB update — 2026-07-2…
2 days ago
.github
Merge branch 'qualcomm:main' into main
now
cli
Add qai-hub-models install command (#407…
10 hours ago
proto
[TETRAAI-352] add vocab.txt in the export b…
2 weeks ago
scripts
Manifest pip commands: replace flag string…
2 days ago
src
[Automated] Sync lm_driver from AIMET dev…
4 hours ago
tutorials
Fix broken links in Llama 3 quantization tuto…
5 days ago
.gitattributes
v0.28.0
last year
.gitignore
Add qwen3_0_6b QAIRT/Genie variant (Spin…
5 days ago
.pre-commit-config.yaml
Sync GenAI Lab Driver Code (#3307)
2 months ago
.pre-commit-license-header.txt
v0.33.0
last year
.pre-commit-line-ending-check.yaml
v0.24.0
last year
.shellcheckrc
v0.5.0
2 years ago
CLAUDE.md
Replace Write permissions in Claude setting…
2 weeks ago
CODE-OF-CONDUCT.md
v0.47.0
5 months ago
c10vis-poem
ai-hub-merovingian-models-
Code
Pull requests
1
Agents
Actions
Projects
Wiki
Security and quality
Insights
Settings
Fork
0
m
T

CONTRIBUTING.md
Merge info.yaml + code-gen.yaml into single…
last week
LICENSE
v0.33.0
last year
README.md
Publish Qwen 3 VL 8B (#4015)
2 weeks ago
ruff.toml
Remove remaining "models.common / com…
last month
release
release v0.59.0
v0.59.0
tag
tag v0.59.0
v0.59.0
pypi
pypi v0.59.0
v0.59.0
python
python 3.10 (Recommended), 3.11, 3.12, 3.13
3.10 (Recommended), 3.11, 3.12, 3.13
The Qualcomm® AI Hub Models are a collection of state-of-the-art machine learning models optimized for deployment on Qualcomm®
devices.
List of Models by Category
On-Device Performance Data
Device-Native Sample Apps
See supported: On-Device Runtimes, Hardware Targets & Precision, Chipsets, Devices
Use our lightweight command-line interface to browse and download from the collection of Qualcomm® AI Hub Models.
The CLI also offers a Python API.
See the CLI README for full usage instructions.
The package is available via pip:
Some models (e.g. YOLOv7) require additional dependencies. View the model README (at qai_hub_models/models/model_id) for
installation instructions.
Qualcomm® AI Hub Models
NEW: Quick Start with the AI Hub Models CLI
pip install qai_hub_models_cli # (the CLI is also available with the qai-hub-models package)
qai-hub-models models                                                # browse the catalog
qai-hub-models info mobilenet_v2                                     # model details + download options
qai-hub-models fetch mobilenet_v2 --runtime tflite --precision float # download a deployable asset
# ... and more
Setup
1. Install Python Package
# NOTE for Snapdragon X Elite and Snapdragon X2 Elite users:
# Only AMDx64 (64-bit) Python is supported on Windows.
# Installation will fail when using Windows ARM64 Python.
pip install qai_hub_models
README
Code of conduct
Contributing
License

Many features of AI Hub Models (such as model compilation, on-device profiling, etc.) require access to Qualcomm® AI Hub Workbench:
Create a Qualcomm® ID, and use it to login to Qualcomm® AI Hub Workbench.
Configure your API token: qai-hub configure --api_token API_TOKEN
All models in our directory can be compiled and profiled on a hosted Qualcomm® device:
Using Qualcomm® AI Hub Workbench, the export script will:
1. Compile the model for the chosen device and target runtime (see: Compiling Models on AI Hub Workbench).
2. If applicable, Quantize the model (see: Quantization on AI Hub Workbench)
3. Profile the compiled model on a real device in the cloud (see: Profiling Models on AI Hub Workbench).
4. Run inference with a sample input data on a real device in the cloud, and compare on-device model output with PyTorch output
(see: Running Inference on AI Hub Workbench)
5. Download the compiled model to disk.
Most models in our directory contain CLI demos that run the model end-to-end:
End-to-end demos:
1. Preprocess human-readable input into model input
2. Run model inference
3. Postprocess model output to a human-readable format
Many end-to-end demos use AI Hub Workbench to run inference on a real cloud-hosted device (with --eval-mode on-device ). All end-
to-end demos can also run locally via PyTorch (with --eval-mode fp ).
Native applications that can run our models (with pre- and post-processing) on physical devices are published in the AI Hub Apps
repository.
Python applications are defined for all models (from qai_hub_models.models.<model_name> import App). These apps wrap model
inference with pre- and post-processing steps written using torch & numpy. These apps are optimized to be an easy-to-follow example,
rather than to minimize prediction time.
2. Configure AI Hub Workbench Access
Getting Started
Export and Run A Model on a Physical Device
pip install "qai_hub_models[yolov7]"
qai-hub-models export yolov7 --target-runtime tflite --precision float --device "Samsung Galaxy S25 (Family)"
End-To-End Model Demos
pip install "qai_hub_models[yolov7]"
# Predict and draw bounding boxes on the provided image
python -m qai_hub_models.models.yolov7.demo [--image ...] [--eval-mode {fp,on-device}] [--help]
Sample Applications

Runtime
Supported OS
Qualcomm AI Engine Direct
Android, Linux, Windows
LiteRT (TensorFlow Lite)
Android, Linux
ONNX
Android, Linux, Windows
Device Compute Unit
Supported Precision
CPU
FP32, INT16, INT8
GPU
FP32, FP16
NPU (includes Hexagon DSP, HTP)
FP16*, INT16, INT8
*Some older chipsets do not support fp16 inference on their NPU.
Snapdragon 8 Elite Gen 5, 8 Elite, 8 Gen 3, 8 Gen 2, and 8 Gen 1 Mobile Platforms
Snapdragon X2 Elite, Snapdragon X Elite Compute Platforms
SA7255P, SA8295P, and SA8775P Automotive Platforms
QCS 6490, QCS 8250, QCS 9075, and QCS 8550 IoT Platforms
QCS8450 XR Platform
and many more.
Samsung Galaxy S21, S22, S23, S24, and S25 Series
Xiaomi 12, 13, 15, and 17
Snapdragon X Elite CRD and Snapdragon X2 Elite CRD (Compute Reference Device)
Qualcomm RB3 Gen 2, RB5 Gen 2, IQ-8, IQ-9
and many more.
Model
README
Image Classification
Beit
qai_hub_models.models.beit
ConvNext-Base
qai_hub_models.models.convnext_base
ConvNext-Tiny
qai_hub_models.models.convnext_tiny
DLA-102-X
qai_hub_models.models.dla102x
Model Support Data
On-Device Runtimes
Device Hardware & Precision
Chipsets
Devices
Model Directory
Computer Vision

Model
README
DenseNet-121
qai_hub_models.models.densenet121
EfficientFormer
qai_hub_models.models.efficientformer
EfficientNet-B0
qai_hub_models.models.efficientnet_b0
EfficientNet-B4
qai_hub_models.models.efficientnet_b4
EfficientNet-Lite4
qai_hub_models.models.efficientnet_lite4
EfficientNet-V2-s
qai_hub_models.models.efficientnet_v2_s
EfficientViT-b2-cls
qai_hub_models.models.efficientvit_b2_cls
EfficientViT-l2-cls
qai_hub_models.models.efficientvit_l2_cls
GPUNet
qai_hub_models.models.gpunet
GoogLeNet
qai_hub_models.models.googlenet
Inception-v3
qai_hub_models.models.inception_v3
InternImage
qai_hub_models.models.internimage
LeViT
qai_hub_models.models.levit
MNASNet05
qai_hub_models.models.mnasnet05
Mobile-VIT
qai_hub_models.models.mobile_vit
MobileNet-v2
qai_hub_models.models.mobilenet_v2
MobileNet-v3-Large
qai_hub_models.models.mobilenet_v3_large
MobileNet-v3-Small
qai_hub_models.models.mobilenet_v3_small
NASNet
qai_hub_models.models.nasnet
RegNet
qai_hub_models.models.regnet
RegNet-Y-800MF
qai_hub_models.models.regnet_y_800mf
ResNeXt101
qai_hub_models.models.resnext101
ResNeXt50
qai_hub_models.models.resnext50
ResNet101
qai_hub_models.models.resnet101
ResNet18
qai_hub_models.models.resnet18
ResNet50
qai_hub_models.models.resnet50
Sequencer2D
qai_hub_models.models.sequencer2d
Shufflenet-v2
qai_hub_models.models.shufflenet_v2
SqueezeNet-1.1
qai_hub_models.models.squeezenet1_1
Swin-Base
qai_hub_models.models.swin_base
Swin-Small
qai_hub_models.models.swin_small
Swin-Tiny
qai_hub_models.models.swin_tiny
SwinV2-Base
qai_hub_models.models.swinv2_base
VIT
qai_hub_models.models.vit
WideResNet50
qai_hub_models.models.wideresnet50
Image Editing

Model
README
AOT-GAN
qai_hub_models.models.aotgan
DDColor
qai_hub_models.models.ddcolor
DnCNN
qai_hub_models.models.dncnn
LaMa-Dilated
qai_hub_models.models.lama_dilated
NAFNet-DeBlur
qai_hub_models.models.nafnet_deblur
NAFNet-DeNoise
qai_hub_models.models.nafnet_denoise
Super Resolution
ESRGAN
qai_hub_models.models.esrgan
NAFSSR
qai_hub_models.models.nafssr
QuickSRNetLarge
qai_hub_models.models.quicksrnetlarge
QuickSRNetMedium
qai_hub_models.models.quicksrnetmedium
QuickSRNetSmall
qai_hub_models.models.quicksrnetsmall
Real-ESRGAN-General-x4v3
qai_hub_models.models.real_esrgan_general_x4v3
Real-ESRGAN-x4plus
qai_hub_models.models.real_esrgan_x4plus
SESR-M5
qai_hub_models.models.sesr_m5
XLSR
qai_hub_models.models.xlsr
Semantic Segmentation
DDRNet23-Slim
qai_hub_models.models.ddrnet23_slim
DeepLabV3-Plus-MobileNet
qai_hub_models.models.deeplabv3_plus_mobilenet
DeepLabXception
qai_hub_models.models.deeplab_xception
EdgeTAM
qai_hub_models.models.edgetam
FCN-ResNet50
qai_hub_models.models.fcn_resnet50
FFNet-122NS-LowRes
qai_hub_models.models.ffnet_122ns_lowres
FFNet-40S
qai_hub_models.models.ffnet_40s
FFNet-54S
qai_hub_models.models.ffnet_54s
FFNet-78S
qai_hub_models.models.ffnet_78s
FFNet-78S-LowRes
qai_hub_models.models.ffnet_78s_lowres
FastSam-S
qai_hub_models.models.fastsam_s
FastSam-X
qai_hub_models.models.fastsam_x
HRNet-W48-OCR
qai_hub_models.models.hrnet_w48_ocr
Mask2Former
qai_hub_models.models.mask2former
MaskRCNN
qai_hub_models.models.maskrcnn
MediaPipe-Selfie-Segmentation
qai_hub_models.models.mediapipe_selfie
MobileSam
qai_hub_models.models.mobilesam
PSPNet
qai_hub_models.models.pspnet

Model
README
PidNet
qai_hub_models.models.pidnet
PointNet
qai_hub_models.models.pointnet
SINet
qai_hub_models.models.sinet
SalsaNext
qai_hub_models.models.salsanext
Segformer-Base
qai_hub_models.models.segformer_base
Segment-Anything-Model-2
qai_hub_models.models.sam2
Segment-Anything-Model-3
qai_hub_models.models.sam3
Unet-Segmentation
qai_hub_models.models.unet_segmentation
YOLO26-Segmentation
qai_hub_models.models.yolo26_seg
YOLOE-Segmentation
qai_hub_models.models.yoloe_seg
YOLOv11-Segmentation
qai_hub_models.models.yolov11_seg
YOLOv8-Segmentation
qai_hub_models.models.yolov8_seg
Video Classification
ResNet-2Plus1D
qai_hub_models.models.resnet_2plus1d
ResNet-3D
qai_hub_models.models.resnet_3d
ResNet-Mixed-Convolution
qai_hub_models.models.resnet_mixed
Video-MAE
qai_hub_models.models.video_mae
Video Generation
First-Order-Motion-Model
qai_hub_models.models.fomm
Video Object Tracking
Track-Anything
qai_hub_models.models.track_anything
Object Detection
3D-Deep-BOX
qai_hub_models.models.deepbox
CavaFace
qai_hub_models.models.cavaface
CenterNet-2D
qai_hub_models.models.centernet_2d
Conditional-DETR-ResNet50
qai_hub_models.models.conditional_detr_resnet50
DETR-ResNet101
qai_hub_models.models.detr_resnet101
DETR-ResNet101-DC5
qai_hub_models.models.detr_resnet101_dc5
DETR-ResNet50
qai_hub_models.models.detr_resnet50
DETR-ResNet50-DC5
qai_hub_models.models.detr_resnet50_dc5
Detectron2-Detection
qai_hub_models.models.detectron2_detection
Facial-Attribute-Detection
qai_hub_models.models.face_attrib_net
HRNetFace
qai_hub_models.models.hrnet_face
Lightweight-Face-Detection
qai_hub_models.models.face_det_lite
MediaPipe-Face-Detection
qai_hub_models.models.mediapipe_face

Model
README
MediaPipe-Hand-Detection
qai_hub_models.models.mediapipe_hand
MediaPipe-Hand-Gesture-Recognition
qai_hub_models.models.mediapipe_hand_gesture
PPE-Detection
qai_hub_models.models.gear_guard_net
Person-Foot-Detection
qai_hub_models.models.foot_track_net
RF-DETR
qai_hub_models.models.rf_detr
RTMDet
qai_hub_models.models.rtmdet
ResNet34-SSD
qai_hub_models.models.resnet34_ssd1200
YOLO-WORLD
qai_hub_models.models.yolo_world
YOLO26-Detection
qai_hub_models.models.yolo26_det
YOLOv10-Detection
qai_hub_models.models.yolov10_det
YOLOv11-Detection
qai_hub_models.models.yolov11_det
YOLOv8-Detection
qai_hub_models.models.yolov8_det
YOLOv8-OBB
qai_hub_models.models.yolov8_obb
YOLOv9-Detection
qai_hub_models.models.yolov9_det
Yolo-R
qai_hub_models.models.yolor
Yolo-X
qai_hub_models.models.yolox
Yolo-v3
qai_hub_models.models.yolov3
Yolo-v5
qai_hub_models.models.yolov5
Yolo-v6
qai_hub_models.models.yolov6
Yolo-v7
qai_hub_models.models.yolov7
Pose Estimation
CenterNet-Pose
qai_hub_models.models.centernet_pose
Facial-Landmark-Detection
qai_hub_models.models.facemap_3dmm
HRNetPose
qai_hub_models.models.hrnet_pose
LiteHRNet
qai_hub_models.models.litehrnet
MediaPipe-Pose-Estimation
qai_hub_models.models.mediapipe_pose
Posenet-Mobilenet
qai_hub_models.models.posenet_mobilenet
RTMPose-Body2d
qai_hub_models.models.rtmpose_body2d
SixDRepNet
qai_hub_models.models.sixd_repnet
YOLO26-Pose
qai_hub_models.models.yolo26_pose
YOLOv11-Pose
qai_hub_models.models.yolov11_pose
Gaze Estimation
EyeGaze
qai_hub_models.models.eyegaze
Depth Estimation
CREStereo
qai_hub_models.models.crestereo

Model
README
Depth-Anything
qai_hub_models.models.depth_anything
Depth-Anything-V2
qai_hub_models.models.depth_anything_v2
Depth-Anything-V3
qai_hub_models.models.depth_anything_v3
Midas-V2
qai_hub_models.models.midas
StereoNet
qai_hub_models.models.stereonet
Driver Assistance
BEVDet
qai_hub_models.models.bevdet
BEVFusion
qai_hub_models.models.bevfusion_det
CVT
qai_hub_models.models.cvt
CenterNet-3D
qai_hub_models.models.centernet_3d
CenterPoint
qai_hub_models.models.centerpoint
GKT
qai_hub_models.models.gkt
RangeNet-Plus-Plus
qai_hub_models.models.rangenet_plus_plus
StateTransformer
qai_hub_models.models.statetransformer
Robotics
ACT
qai_hub_models.models.act
Model
README
EasyOCR
qai_hub_models.models.easyocr
GR00TN1.5
qai_hub_models.models.grootn15
MiniLM-v2
qai_hub_models.models.minilm_v2
Nomic-Embed-Text
qai_hub_models.models.nomic_embed_text
OpenAI-Clip
qai_hub_models.models.openai_clip
OpusMT-En-Es
qai_hub_models.models.opus_mt_en_es
OpusMT-En-Zh
qai_hub_models.models.opus_mt_en_zh
OpusMT-Es-En
qai_hub_models.models.opus_mt_es_en
OpusMT-Zh-En
qai_hub_models.models.opus_mt_zh_en
Pi0.5
qai_hub_models.models.pi05
TrOCR
qai_hub_models.models.trocr
Model
README
Speech Recognition
Distil-Whisper
qai_hub_models.models.distil_whisper
Multimodal
Audio

Model
README
Whisper-Base
qai_hub_models.models.whisper_base
Whisper-Large-V3-Turbo
qai_hub_models.models.whisper_large_v3_turbo
Whisper-Medium
qai_hub_models.models.whisper_medium
Whisper-Small
qai_hub_models.models.whisper_small
Whisper-Small-Quantized
qai_hub_models.models.whisper_small_quantized
Whisper-Tiny
qai_hub_models.models.whisper_tiny
Zipformer
qai_hub_models.models.zipformer
Audio Classification
YamNet
qai_hub_models.models.yamnet
Audio Generation
MeloTTS-EN
qai_hub_models.models.melotts_en
MeloTTS-ES
qai_hub_models.models.melotts_es
MeloTTS-ZH
qai_hub_models.models.melotts_zh
PiperTTS-DE
qai_hub_models.models.pipertts_de
PiperTTS-EN
qai_hub_models.models.pipertts_en
PiperTTS-IT
qai_hub_models.models.pipertts_it
Model
README
Image Generation
ControlNet-Canny
qai_hub_models.models.controlnet_canny
Stable-Diffusion-v1.5
qai_hub_models.models.stable_diffusion_v1_5
Stable-Diffusion-v2.1
qai_hub_models.models.stable_diffusion_v2_1
Text Generation
Albert-Base-V2-Hf
qai_hub_models.models.albert_base_v2_hf
Bert-Base-Uncased-Hf
qai_hub_models.models.bert_base_uncased_hf
Distil-Bert-Base-Uncased-Hf
qai_hub_models.models.distil_bert_base_uncased_hf
Electra-Bert-Base-Discrim-Google
qai_hub_models.models.electra_bert_base_discrim_google
Falcon3-7B-Instruct
qai_hub_models.models.falcon_v3_7b_instruct
GPT-OSS-20B
qai_hub_models.models.gpt_oss_20b
Gemma-4-E2B-it
qai_hub_models.models.gemma_4_e2b_it
Gemma-4-E4B-it
qai_hub_models.models.gemma_4_e4b_it
Granite-4.0-Micro
qai_hub_models.models.granite_4_0_micro
IBM-Granite-v3.1-8B-Instruct
qai_hub_models.models.ibm_granite_v3_1_8b_instruct
IndusQ-1.1B
qai_hub_models.models.indus_1b
Generative AI

Model
README
JAIS-6p7b-Chat
qai_hub_models.models.jais_6p7b_chat
Llama-SEA-LION-v3.5-8B-R
qai_hub_models.models.llama_v3_1_sea_lion_3_5_8b_r
Llama-v3-8B-Instruct
qai_hub_models.models.llama_v3_8b_instruct
Llama-v3-ELYZA-JP-8B
qai_hub_models.models.llama_v3_elyza_jp_8b
Llama-v3.1-8B-Instruct
qai_hub_models.models.llama_v3_1_8b_instruct
Llama-v3.2-1B-Instruct
qai_hub_models.models.llama_v3_2_1b_instruct
Llama-v3.2-3B-Instruct
qai_hub_models.models.llama_v3_2_3b_instruct
Llama-v3.2-3B-Instruct-SSD
qai_hub_models.models.llama_v3_2_3b_instruct_ssd
Llama3-TAIDE-LX-8B-Chat-Alpha1
qai_hub_models.models.llama_v3_taide_8b_chat
Ministral-3-3B-Instruct-2512
qai_hub_models.models.ministral_3_3b_instruct_2512
Mistral-7B-Instruct-v0.3
qai_hub_models.models.mistral_7b_instruct_v0_3
Mobile-Bert-Uncased-Google
qai_hub_models.models.mobile_bert_uncased_google
PLaMo-1B
qai_hub_models.models.plamo_1b
Phi-3.5-Mini-Instruct
qai_hub_models.models.phi_3_5_mini_instruct
Phi-4-Mini-Instruct
qai_hub_models.models.phi_4_mini_instruct
Qwen2-7B-Instruct
qai_hub_models.models.qwen2_7b_instruct
Qwen2.5-VL-7B-Instruct
qai_hub_models.models.qwen2_5_vl_7b_instruct
Qwen3-0.6B
qai_hub_models.models.qwen3_0_6b
Qwen3-1.7B
qai_hub_models.models.qwen3_1_7b
Qwen3-4B
qai_hub_models.models.qwen3_4b
Qwen3-4B-Instruct-2507
qai_hub_models.models.qwen3_4b_instruct_2507
Qwen3-8B
qai_hub_models.models.qwen3_8b
Qwen3-VL-2B-Instruct
qai_hub_models.models.qwen3_vl_2b_instruct
Qwen3-VL-4B-Instruct
qai_hub_models.models.qwen3_vl_4b_instruct
Qwen3-VL-8B-Instruct
qai_hub_models.models.qwen3_vl_8b_instruct
Qwen3.5-0.8B
qai_hub_models.models.qwen3_5_0_8b
Qwen3 5-2B
qai hub models models qwen3 5 2b
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
No contributors

Languages
Python 98.9%
Other 1.1%
