# Get started with Unsloth Studio - Unsloth Documentation

1
New
🦥Introducing Unsloth Studio
Get started with Unsloth
Studio
A guide for getting started with the fine-tuning studio, data
recipes, model exporting, and chat.
Unsloth Studio is a local, browser-based GUI for fine-tuning LLMs
without writing any code. It wraps the training pipeline in a clean
interface that handles model loading, dataset formatting,
hyperparameter configuration, and live training monitoring.
Unsloth
Data Recipe
Export
Chat
First, launch Unsloth Studio using either a local install or a cloud
option. Follow the install instructions for your setup, or use our free
Colab notebook. For a local setup, run:
Setup Unsloth Studio
unsloth studio -H 0.0.0.0 -p 8888
Copy
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.
Accept
Reject

2
Open your browser of choice go
to http://127.0.0.1:8888 . You will
need to create a new password.
Launch Unsloth securely with
HTTPS and Cloudflare. Unsloth
now provides a secure way to
launch Unsloth over HTTPS
through a free Cloudflare
tunnel. Use the below (works in
Windows, Mac & Linux):
Unsloth Studio Chat lets you run models 100% offline on your
computer. Run model formats like GGUF and safetensors from
Hugging Face or from your local files.
• Download + Run any model like GGUFs, fine-tuned adapters,
safetensors etc.
• Compare different model outputs side-by-side
• Upload documents, images, and audio in your prompts
• Tune inference settings like: temperature, top-p, top-k and
system prompt
unsloth studio --secure
 Chat - Quickstart
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

3
You can read our detailed tutorial / guide about running models
with Unsloth Studio here:
Studio Chat
Before using the API, you need to load the model you want to use in
Unsloth. Open the Select model dropdown in the top-left corner of
the chat page.
Model Loading Guide
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

4
On a different page? Use the left sidebar and click New Chat to
return to the chat page.
Use the search bar to find the
model you want to load into
Unsloth.
Browse recommended models,
search Hugging Face models
directly, or set a custom model
directory.
Locally trained and exported
models can be loaded from the
`Fine-tuned` tab.
Select Model
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

5
Model repos contain multiple
quantizations. Select the
quantization most suitable for
your available RAM / VRAM.
In this guide we'll use 
unsloth/gemma-4-26B-A4B-it-
GGUF and select the
recommended UD-Q4_K_XL
variant
Search for the model you want
to use, then click it to begin
downloading and loading it.
After selecting a model variant,
Unsloth will begin downloading
and loading the model into
memory.
Once loading is complete you
will see the following
confirmation:
The model is loaded and ready to use. You can now chat with the
model directly in Unsloth or connect it to tools such as Claude
Code and Codex.
GGUF Selection
Downloading the model
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

6
Unsloth Studio homepage has 4 main areas: Model, Dataset, 
Parameters, and Training/Config
• Easy setup for models and data from Hugging Face or local files
• Flexible training choices like QLoRA, LoRA, or full fine-tuning,
with defaults filled in
• Helpful config tools for splits, column mapping,
hyperparameters and YAML configs
• Great training visibility with live progress, GPU stats, charts,
startup status
 Unsloth - Quickstart
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

7
Select the modality that matches your use-case:
Three methods are available, toggled with a pill selector:
1. Select model and method
Model Type
Type
Use case
Text
Chat, instruction following,
completion
Vision
Image + text (VLMs)
Audio
Speech / audio understanding
Embeddings
Sentence embeddings, retrieval
Training Method
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

8
Type any Hugging Face model name or search the Hub directly
from the combobox. Local models stored in 
~/.unsloth/studio/models and your Hugging Face cache also appear
in the list.
GGUF format models are excluded from training - they are inference
only.
When you pick a model the Unsloth automatically fetches its
configuration from the backend and pre-fills sensible defaults for all
hyperparameters.
HuggingFace Token
Paste your Hugging Face access token here if the model is gated
(e.g. Llama, Gemma). The token is validated in real-time and an
error is shown inline if it is invalid.
Method
Description
VRAM
QLoRA
4-bit quantized base
model + LoRA adapter
Lowest
LoRA
Full-precision base
model + LoRA adapter
Medium
Full Fine-tuning
All weights are trained
Highest
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

9
Switch between two tabs to
choose where your data comes
from:
• HuggingFace Hub - live
search against the Hub. The
last-updated date is shown
for each result.
• Local - drag-and-drop or
click to upload a file
unstructured or structured
files like: PDF , DOCX , 
JSONL , JSON , CSV , or 
Parquet format. Previously
uploaded datasets appear in
a list that refreshes
automatically.
You can view our detailed 
Datasets Guide here.
Prompt Unsloth how to
interpret and format your data:
2. Dataset
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

10
Splits and Slicing
• Subset - automatically populated from the dataset card.
• Train split / Eval split - choose which splits to use. Setting an
eval split enables the Eval Loss chart during training.
• Dataset slice - optionally restrict training to a row range (start
index / end index) for quick experiments.
Column Mapping
If the Unsloth cannot automatically map your dataset columns to
the correct roles a Dataset Preview dialog opens. It shows sample
rows and lets you assign each column to instruction , input , output ,
image , etc. Suggested mappings are pre-filled where possible.
Parameters are grouped into collapsible sections. You can view our
detailed LoRA hyperparameters guide here:
🧠
Hyperparameters Guide
Format
When to use
auto
Let Unsloth detect the format
automatically
alpaca
instruction / input / output
columns
chatml
OpenAI-style messages array
sharegpt
ShareGPT-style conversations
3. Hyperparameters
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

11
LoRA Settings
(Hidden when Full Fine-tuning is selected)
For Vision models with an image dataset, four additional
checkboxes appear. Fine-tune:
Training Hyperparameters
Organized into three tabs:
Parameter
Default
Notes
Max Steps
0
0 means use Epochs
instead
Context Length
2048
Options: 512 → 32768
Learning Rate
2e-4
Parameter
Default
Notes
Rank
16
Slider 4–128
Alpha
32
Slider 4–256
Dropout
0.05
LoRA Variant
LoRA
LoRA / RS-LoRA / 
LoftQ
Target Modules
All on
q_proj , k_proj , 
v_proj , o_proj , 
gate_proj , up_proj , 
down_proj
Vision Layers
Language
Layers
Attention
Modules
MLP Modules
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

12
Unsloth Gradient Checkpointing: unsloth uses Unsloth's custom
memory-efficient implementation, which can reduce VRAM usage
significantly compared to the standard PyTorch option. It is the
recommended default.
The bottom-right card has three config management buttons and
the Start Training button.
Optimization
Schedule
Logging
Parameter
Default
Epochs
3
Batch Size
4
Gradient Accumulation
8
Weight Decay
0.01
Optimizer
AdamW 8-bit
4. Training and Config
Button
Action
Upload
Load a previously saved .yaml
config file
Save
Export the current config to YAML
Reset
Revert all parameters to the
model's defaults
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

13
The Start Training button stays disabled until a model and dataset
are both configured. Validation errors appear inline - for example,
setting eval steps without choosing an eval split, or pairing a text-
only model with a vision dataset.
After you click Start Training, a
full-page overlay appears while
the backend prepares
everything.
The overlay shows an animated
terminal with live phase
updates:
• Blue: Downloading model /
dataset
• Amber: Loading model /
dataset
• Blue: Configuring
• Green: Training
You can cancel at any time
using the × button in the corner.
A confirmation dialog will
appear before anything is
stopped.
Once the first training step arrives the overlay dismisses and the
live training view is revealed. The fine-tuning process is complete
when steps reach 100% on the progress bar. You can view the
elapsed time and tokens. 
Loading Screen
Training Progress and Observability
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

14
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

15
The left column shows:
• Epoch - current fractional
epoch (e.g. Epoch 1.23 )
• Progress bar - step-based,
with percentage
• Key metrics:
◦Loss - training loss to 4
decimal places
◦LR - current learning rate
in scientific notation
◦Grad Norm - gradient
norm
◦Model - the model being
trained
◦Method - QLoRA / LoRA
/ Full
• Timing row - elapsed time,
ETA, steps per second, and
total tokens processed
The right column shows live
GPU stats polled every few
seconds:
• Utilization - percentage bar
• Temperature - °C bar
• VRAM - used / total GB
• Power - draw / limit in watts
Use the Stop Training button in
the top-right of the progress
card. A dialog gives you two
choices:
• Stop & Save - saves a
checkpoint before stopping
• Cancel - stops immediately
with no checkpoint
Status Panel
GPU Monitor
Stopping Training
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

16
Four live charts update as
training progresses:
1. Training Loss - raw values
plus an EMA-smoothed line
and a running average
reference line
2. Learning Rate - the LR
schedule curve
3. Gradient Norm - gradient
norm over steps
4. Eval Loss - only shown when
you configured an eval split
Charts
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

17
Each chart has settings (gear
icon) with:
All training configurations can
be saved and reloaded as
YAML files. Files are named
automatically as:
Search
Option
Default
Viewing
window
Last N steps
slider
EMA
Smoothing
0.6
Show Raw
On
Show
Smoothed
On
Show Average
line
On
Scale (per
series)
Linear / Log
Outlier
clipping
No clip / p99 /
p95
Config Files
{model}_{method}_{dataset}_{ti
mestamp}.yaml
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

18
The YAML is structured into three sections:
This makes it easy to reproduce runs, share configurations, or
version-control your experiments.
Unsloth Data Recipes lets you upload documents like PDFs or CSVs
files and transforms them into useable datasets. Create and edit
datasets visually via a graph-node workflow.
The recipes page is the main entry point. Recipes are stored locally
in the browser, so you come back to saved work later. From here,
you can create a blank recipe or open a guided learning recipe.
training:
max_steps: 0
num_train_epochs: 3
per_device_train_batch_size: 4
...
lora:
r: 16
lora_alpha: 32
training:
max_steps: 0
num_train_epochs: 3
per_device_train_batch_size: 4
...
lora:
r: 16
lora_alpha: 32
 Data Recipes - Quickstart
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

19
Data Recipes follows the same basic path. You open the recipes
page, create or pick a recipe, build the workflow in the editor,
validate it run a preview, then run the full dataset once the output
looks right. Add seed data and generation blocks, validate the
workflow, preview sample output, then run a full dataset build.
Unsloth Data Recipes is powered by NVIDIA DataDesigner .
At a glance a usual workflow should look like this:
1. Open the recipes page.
2. Create a new recipe or open an existing one.
3. Add blocks to define your dataset workflow.
4. Click Validate to catch configuration issues early.
5. Run a preview to inspect sample rows quickly.
6. Run a full dataset build when the recipe is ready.
7. Review progress and output live in graph or in Executions view
for mode details.
8. Select the resulting dataset in Unsloth and fine tune a model.
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

20
Use Unsloth Studio 'Export' to export, save, or convert models to
GGUF, Safetensors, or LoRA for deployment, sharing, or local
inference in Unsloth, llama.cpp, Ollama, vLLM, and more. Export a
trained checkpoint or convert any existing model.
You can read our detailed tutorial / guide about exporting models
with Unsloth Studio here:
Model Export
The Unsloth Studio versions shown in the videos are old and are not
reflective of the current version.
 Export - Quickstart
 Video Tutorial
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

21
Here is a video tutorial created
by NVIDIA to get you started
with Unsloth:
How to Install Unsloth Studio
Video Tutorial
The Unsloth CLI ( cli.py ) provides the following commands:
NVIDIA Developer
Get Started with Uns
Get Started with Uns
Watch on
Daniel Han-Chen
How to Install Unslot
How to Install Unslot
Watch on
Advanced Settings
CLI Commands
Usage: cli.py [COMMAND]
Commands:
train             Fine-tune a model
inference         Run inference on a trained model
export            Export a trained adapter
list-checkpoints  List saved checkpoints
ui                Launch the Unsloth Studio web UI
studio            Launch the studio (alias)
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

22
All endpoints require a valid JWT Authorization: Bearer <token>
header (except /api/auth/* and /api/health ).
Project Structure
new-ui-prototype/
├── cli.py                     # CLI entry point
├── cli/                       # Typer CLI commands
│   └── commands/
│       ├── train.py
│       ├── inference.py
│       ├── export.py
│       ├── ui.py
│       └── studio.py
├
t
h
# B
t t
i t (Li
/ WSL / C l b)
new-ui-prototype/
├── cli.py                     # CLI entry point
├── cli/                       # Typer CLI commands
│   └── commands/
│       ├── train.py
│       ├── inference.py
│       ├── export.py
│       ├── ui.py
│       └── studio.py
├
t
h
# B
t t
i t (Li
/ WSL / C l b)
API Reference
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

23
Search
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

24
Method
Endpoint
Description
GET
/api/health
Health check
GET
/api/system
System info (GPU,
CPU, memory)
POST
/api/auth/signup
Create account
(requires setup token
on first run)
POST
/api/auth/login
Login and receive
JWT tokens
POST
/api/auth/refresh
Refresh an expired
access token
GET
/api/auth/status
Check if auth is
initialized
POST
/api/train/start
Start a training job
POST
/api/train/stop
Stop a running
training job
POST
/api/train/reset
Reset training state
GET
/api/train/status
Get current training
status
GET
/api/train/metrics
Get training metrics
(loss, LR, steps)
GET
/api/train/stream
SSE stream of real-
time training progress
GET
/api/models/
List available models
POST
/api/inference/chat
Send a chat message
for inference
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

25
Community
Reddit r/unsloth
Twitter (X)
LinkedIn
Resources
Tutorials
Docker
Hugging Face
Company
Unsloth Studio
Contact
Events
Previous
Introducing Unsloth
Studio
Next
Studio Chat
Last updated 5 days ago
Was this helpful?
GET
/api/datasets/
List / manage
datasets
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

26
© Unsloth, 2026
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.

## Extracted images

(pulled from the source doc by `.migrate/extract_images.py` -- Markdown conversion drops these; see `Get started with Unsloth Studio - Unsloth Documentation.pdf_images/`)

- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0005.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0014.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0017.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0020.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0023.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0027.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0031.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0035.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0038.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0041.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0045.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0048.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0092.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0095.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0096.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0098.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0101.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0104.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0107.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0139.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0140.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0142.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0145.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0148.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0151.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0183.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0184.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0186.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0187.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0188.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0191.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0194.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0197.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0228.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0229.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0230.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0231.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0232.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0233.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0234.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0237.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0240.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0243.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0278.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0279.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0280.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0283.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0286.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0289.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0324.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0325.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0329.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0332.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0335.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0338.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0369.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0372.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0375.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0378.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0409.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0410.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0411.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0414.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0417.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0420.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0453.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0456.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0459.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0462.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0497.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0500.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0503.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0506.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0539.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0542.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0545.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0548.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0580.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0581.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0582.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0585.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0588.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0591.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0622.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0623.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0624.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0627.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0630.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0633.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0664.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0667.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0670.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0673.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0704.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0705.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0706.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0709.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0712.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0715.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0746.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0750.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0751.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0752.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0755.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0756.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0757.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0760.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0763.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0766.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0797.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0835.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0838.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0841.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0844.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0876.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0877.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0878.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0881.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0884.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0887.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0920.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0921.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0922.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0925.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0928.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0931.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0963.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0964.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0966.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0967.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0968.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0969.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0971.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0994.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0996.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-0997.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1003.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1004.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1005.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1006.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1008.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1029.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1030.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1031.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1036.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1039.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1042.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1045.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1048.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1087.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1092.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1093.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1099.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1100.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1106.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1107.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1108.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1114.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1115.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1121.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1122.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1134.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1137.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1140.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1143.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1174.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1177.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1180.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1183.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1186.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1217.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1220.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1223.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1226.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1259.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1260.png) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1261.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1264.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1267.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1270.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1347.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1350.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1353.jpg) -- embedded raster
- ![embedded raster](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/image-1356.jpg) -- embedded raster
- ![page 1 render (106 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-1-diagram.png) -- page 1 render (106 vector ops)
- ![page 2 render (40 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-2-diagram.png) -- page 2 render (40 vector ops)
- ![page 3 render (22 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-3-diagram.png) -- page 3 render (22 vector ops)
- ![page 4 render (24 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-4-diagram.png) -- page 4 render (24 vector ops)
- ![page 5 render (36 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-5-diagram.png) -- page 5 render (36 vector ops)
- ![page 6 render (28 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-6-diagram.png) -- page 6 render (28 vector ops)
- ![page 7 render (36 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-7-diagram.png) -- page 7 render (36 vector ops)
- ![page 8 render (44 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-8-diagram.png) -- page 8 render (44 vector ops)
- ![page 9 render (44 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-9-diagram.png) -- page 9 render (44 vector ops)
- ![page 10 render (88 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-10-diagram.png) -- page 10 render (88 vector ops)
- ![page 11 render (146 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-11-diagram.png) -- page 11 render (146 vector ops)
- ![page 12 render (76 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-12-diagram.png) -- page 12 render (76 vector ops)
- ![page 13 render (20 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-13-diagram.png) -- page 13 render (20 vector ops)
- ![page 14 render (18 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-14-diagram.png) -- page 14 render (18 vector ops)
- ![page 15 render (34 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-15-diagram.png) -- page 15 render (34 vector ops)
- ![page 16 render (20 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-16-diagram.png) -- page 16 render (20 vector ops)
- ![page 17 render (70 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-17-diagram.png) -- page 17 render (70 vector ops)
- ![page 18 render (70 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-18-diagram.png) -- page 18 render (70 vector ops)
- ![page 19 render (22 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-19-diagram.png) -- page 19 render (22 vector ops)
- ![page 20 render (32 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-20-diagram.png) -- page 20 render (32 vector ops)
- ![page 21 render (106 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-21-diagram.png) -- page 21 render (106 vector ops)
- ![page 22 render (78 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-22-diagram.png) -- page 22 render (78 vector ops)
- ![page 23 render (24 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-23-diagram.png) -- page 23 render (24 vector ops)
- ![page 24 render (214 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-24-diagram.png) -- page 24 render (214 vector ops)
- ![page 25 render (64 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-25-diagram.png) -- page 25 render (64 vector ops)
- ![page 26 render (58 vector ops)](Get started with Unsloth Studio - Unsloth Documentation.pdf_images/page-26-diagram.png) -- page 26 render (58 vector ops)
