import os
import sys
from google import genai
import base64

# Set up project path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))  # goes to insta_agent/
sys.path.insert(0, project_root)

from app.config import API_KEY, path

# ✅ Configure Gemini client
client = genai.Client(api_key=API_KEY)

def image_gen(image_desc: str):
    """Generate an image using VEO model (predictLongRunning)."""

    prompt = f"Generate an image about {image_desc}."

    # Use predict_long_running for VEO
    response = client.predict_long_running(
        model="models/veo-2.0-generate-001",
        input={
            "prompt": prompt,
            # Optional: you can set size/aspect_ratio if model supports it
            # "size": "1024x1024"
        }
    )

    # Wait for the result to complete
    result = response.result()

    if "artifacts" not in result or len(result["artifacts"]) == 0:
        print("❌ No image generated.")
        return

    # The model returns base64 images
    image_b64 = result["artifacts"][0]["content"]
    image_bytes = base64.b64decode(image_b64)

    # Save generated image
    with open(path, "wb") as f:
        f.write(image_bytes)

    print(f"✅ Generated image saved at {path}")
