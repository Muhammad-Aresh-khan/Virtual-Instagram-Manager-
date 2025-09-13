import os
import sys
from google import genai
import base64
import mimetypes 

# Set up project path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))  # goes to insta_agent/
sys.path.insert(0, project_root)

from app.config import API_KEY, IMG_MODEL, path

# ✅ Configure Gemini client
client = genai.Client(api_key=API_KEY)

# ✅ Upload the logo to Gemini
logo_path = "logo.png"  # Path to your logo file


# # ✅ Upload the logo to Gemini
# uploaded_logo = genai.upload_file(
#     path=logo_path,
#     display_name="company_logo.png"
# )

def image_gen(image_desc: str):
    """Generate an image using Gemini + include uploaded logo."""

    prompt = (
        f"Generate an image about {image_desc}."
    )

    result = client.models.generate_images(
        model="models/veo-2.0-generate-001",  # Imagen model
        prompt=prompt,
        # config=dict(
        #     number_of_images=1,
        #     output_mime_type="image/jpeg",
        #     aspect_ratio="1:1",
        #     image_size="1K",
        #     # references=[uploaded_logo.uri],  # attach uploaded logo
        # )
    )

    if not result.generated_images:
        print("❌ No image generated.")
        return

    # Save generated image
    generated_image = result.generated_images[0]
    output_path = path

    # The google-genai client gives you a PIL image directly:
    generated_image.image.save(output_path)

    print(f"✅ Generated image saved at {output_path}")
