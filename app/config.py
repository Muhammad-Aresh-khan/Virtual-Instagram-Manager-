import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
# setting date config
now = datetime.now()
today = now.date()
time_str = now.strftime("%H-%M")
TIMESTAMP = f"{today} {time_str}"
# === API KEYS ===
API_KEY = os.getenv("API_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
IG_USER_ID = os.getenv("IG_USER_ID")
PAGE_ID = os.getenv("PAGE_ID")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
HUGGING_FACE=os.getenv("HUGGING_FACE")

# === MODEL CONFIGS ===
MODEL = os.getenv("model_name") 
IMG_MODEL=os.getenv("img_model")# You can switch to other GROQ-supported models
REPLICATE_MODEL = "stability-ai/sdxl:6b5b74e4e8cd0bbaf3c5cdd82f6fc772f2610dd0e0e6e1e2f205d106c302d6ab"

# === CAPTION GENERATION SETTINGS ===
CAPTION_PROMPT_SYSTEM = (
    "You're an expert Instagram caption writer for Software Company 'WENAWA' . Be witty, emoji-friendly, and concise."
)
# === DEFAULT SETTINGS ===
DEFAULT_IMAGE_OUTPUT_DIR = "outputs"  # Optional if you want to store images later
# for main.py
USERNAME = "beautiful_caption_710"
PASSWORD = "123Wellcome!@"
IMAGE_PATH = os.path.abspath(f"outputs/generated {TIMESTAMP}.png")
CAPTION_PATH = os.path.abspath(f"outputs/Post Caption {TIMESTAMP}.txt")
# image output path used in image_visuals
path = f"outputs/generated {TIMESTAMP}.png"
# caption output path used in post agent
filename = f"outputs/Post Caption {TIMESTAMP}.txt"