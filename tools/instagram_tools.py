from google import genai
import os
import sys

# Set up project path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))  # goes to insta_agent/
sys.path.insert(0, project_root)

from app.config import API_KEY
client = genai.Client(api_key=API_KEY)

print("Available models with this key:\n")
for model in client.models.list():
    print(model.name, model.supported_actions)
