import os
import sys
# Import tools
from tools import caption_generator, image_desc_gen, image_visual
from app import config
filename=config.filename
# Generate content
def post_agent (caption: str ) -> str: 
    caption = caption_generator.generate_caption(caption)
    prompt = image_desc_gen.generate_Visual_desc(caption)
    image_visual.generate_image(prompt)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{caption}\n")
    return filename 

