import os
import sys
import torch
from dotenv import load_dotenv
from diffusers import StableDiffusionPipeline
from langchain_core.runnables import RunnableLambda
from app import config
path=config.path
# === Resolve Paths ===
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))  # goes to insta_agent/
sys.path.insert(0, project_root)

# === Import Tokens and Custom Modules ===
from app.config import HUGGING_FACE as HF_TOKEN


# === Initialize Stable Diffusion Pipeline ===
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
).to("cpu") 
prompt="man doing workout"
# === Image Generation Function ===
def generate_image(prompt: str):   
    image = pipe(prompt).images[0]
    image.save(path)
    return f"✅ Image saved at: {path}"
    