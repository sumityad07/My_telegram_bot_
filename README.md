# 🤖 Telegram Chatbot using OpenAI (GPT-3.5)

A lightweight, intelligent Telegram bot that chats with users using OpenAI’s GPT-3.5-turbo model. It supports conversational memory, clear/reset commands, and more!

Built with:
- [Aiogram](https://docs.aiogram.dev/en/latest/)
- [OpenAI Python SDK](https://platform.openai.com/docs/libraries/python-library)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## ✨ Features

✅ `/start` - Welcomes the user  
✅ `/help` - Shows available commands  
✅ `/clear` - Clears conversation memory  
✅ Context-aware responses  
✅ Easy deployment and config

---

## 🚀 Demo

> 💬 Sample Telegram Conversation  
> ![Bot Screenshot](assets/screenshot.png) *(Add your own)*

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add environment variables
Create a .env file using the template:

env
Copy
Edit
OPEN_AI_KEY=your_openai_api_key
TELELINK=your_telegram_bot_token
BASE_URL=https://api.openai.com/v1
✅ Tip: Use .env.example for reference

4. Run the bot
bash
Copy
Edit
python bot.py
📦 File Structure
bash
Copy
Edit
├── bot.py                # Main Telegram bot logic
├── .env                  # Secret keys (not pushed)
├── .env.example          # Sample env file
├── requirements.txt      # Python dependencies
├── README.md             # This file
📌 Future Improvements
Voice and image input

Deploy on Render or Railway

Add inline keyboard support

Multilingual replies

🧠 Powered By
🤖 OpenAI

🟢 Aiogram

🧩 Python

🙌 Author
Sumit Yadav
Connect with me on LinkedIn

📜 License
This project is licensed under the MIT License

yaml
Copy
Edit

---

### 🧾 Also add this in your project root:

**`requirements.txt`**
```txt
aiogram
openai
python-dotenv
.env.example

env
Copy
Edit
OPEN_AI_KEY=your_openai_key
TELELINK=your_telegram_bot_token
BASE_URL=https://api.openai.com/v1
