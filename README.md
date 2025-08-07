# Virtual Instagram Manager

**Virtual Instagram Manager** is an AI-powered automation tool for Instagram, designed to generate and post content dynamically using Playwright and advanced language models. This project leverages Python, LangChain, Groq API, Hugging Face Diffusers, and Playwright to automate and enhance your Instagram experience.

---

## 🚀 Features

- **AI-generated Captions:** Uses Groq LLM via LangChain for smart, engaging captions.
- **Automated Posting:** Playwright automates login and posting to Instagram.
- **AI Image Generation:** Hugging Face Diffusers create unique images from user topics.
- **Logging & Timestamping:** All captions and logs are saved with timestamps for easy tracking.
- **Future Enhancements:**
  - **DM Automation:** AI-driven direct message replies (coming soon).
  - **Comment Automation:** AI-powered comment replies for full engagement automation (coming soon).

---

## 🛠️ Technologies Used

- **Python**
- **LangChain** (LLM orchestration)
- **Groq API** (caption generation)
- **Hugging Face Diffusers** (image creation)
- **Playwright** (browser automation)

---

## ⚙️ How It Works

1. **Input a Topic:** User provides a topic or prompt.
2. **Caption Generation:** AI (Groq LLM via LangChain) creates a relevant caption.
3. **Image Creation:** Hugging Face Diffusers generate an image based on the topic.
4. **Automated Posting:** Playwright logs in and posts the generated content to Instagram.
5. **Logging:** Captions and logs are saved locally with timestamps for reference.

---

## 📈 Future Enhancements

- **DM Automation:** Enable AI to reply to DMs automatically, increasing engagement and responsiveness.
- **Comment Automation:** AI-driven replies to comments for better audience interaction.
- **Scheduling:** Plan and schedule posts ahead of time.
- **Analytics Dashboard:** Track engagement and performance metrics.

---

## 🔧 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammad-Aresh-khan/Virtual-Instagram-Manager-.git
   cd Virtual-Instagram-Manager-
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

3. **Configure environment variables:**
   - Add your Groq API key, Instagram credentials, and other required secrets to a `.env` file.

4. **Run the application:**
   ```bash
   python app/main.py
   ```

---

## 📝 Usage Example

```python
# main.py
topic = "AI in social media"
# The app will generate a caption and image, then post to Instagram automatically.
```

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Please open issues for feature requests or bug reports.

---

## 📄 License

[MIT](LICENSE)

---

## 🗂️ More Details

Virtual Instagram Manager blends AI content generation (Groq LLM, Hugging Face Diffusers) and browser automation (Playwright) to deliver a seamless posting experience. The project is actively evolving to include full engagement automation—DMs, comments, and beyond!

For questions, reach out via [GitHub Issues](https://github.com/Muhammad-Aresh-khan/Virtual-Instagram-Manager-/issues).
