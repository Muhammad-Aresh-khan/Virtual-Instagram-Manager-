import os
import re
from config import  CAPTION_PATH, IMAGE_PATH,USERNAME,PASSWORD
from playwright.sync_api import sync_playwright

from agents import post_agent
topic=input("Enter Topic For Post")
post_agent.post_agent(topic)

USERNAME = "beautiful_caption_710"
PASSWORD = "123Wellcome!@"

def clean_caption(text):
    return re.sub(r'[^\u0000-\uFFFF]', '', text)

def upload_instagram_post():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # --- Go to Instagram ---
        page.goto("https://www.instagram.com/", timeout=60000)

        # --- Login ---
        page.wait_for_selector("input[name='username']", timeout=15000)
        page.fill("input[name='username']", USERNAME)
        page.fill("input[name='password']", PASSWORD)
        page.keyboard.press("Enter")
        print("✅ Logged in.")
        page.wait_for_timeout(10000)

        # --- Click ➕ Create Button ---
        try:
            page.click("svg[aria-label='New post']")
            print("➕ Clicked Create.")
        except Exception as e:
            print(f"❌ Could not click Create: {e}")
            browser.close()
            return

        # --- Click 'Post' option ---
        try:
            post_btn = page.wait_for_selector("svg[aria-label='Post']", timeout=8000)
            post_btn.click()
            print("🖼 Clicked 'Post'.")
        except Exception as e:
            print(f"❌ Failed to click 'Post': {e}")
            browser.close()
            return

    
        # --- Upload Image ---
        print("📷 IMAGE_PATH:", IMAGE_PATH)
        print("🔍 File exists:", os.path.exists(IMAGE_PATH))

        input_file = page.locator("input[type='file']")
        # input_file.wait_for(state="visible", timeout=10000)
        # input_file.click(force=True)  # Optional but helps sometimes
        input_file.set_input_files(IMAGE_PATH)
        print("✅ Image uploaded.")
        page.wait_for_timeout(5000)

        # --- Click Next (twice) ---
        for i in range(2):
            next_btn = page.locator("//div[text()='Next']")
            next_btn.click()
            print(f"👉 Clicked 'Next' ({i+1}/2)")
            page.wait_for_timeout(3000)

        # --- Read and Clean Caption ---
        with open(CAPTION_PATH, 'r', encoding='utf-8') as f:
            raw_caption = f.read().strip()
        caption = clean_caption(raw_caption)

        # --- Add Caption ---
        caption_box = page.wait_for_selector("div[aria-label='Write a caption...']", timeout=15000)
        caption_box.click()
        page.keyboard.type(caption)
        print("✅ Caption added.")
        page.wait_for_timeout(2000)

        # --- Click Share ---
        share_btn = page.locator("//div[text()='Share']")
        share_btn.click()
        print("🎉 Post shared!")

        page.wait_for_timeout(10000)
        browser.close()

if __name__ == "__main__":
    upload_instagram_post()
 