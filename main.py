import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from openai import OpenAI

# Load environment variables
load_dotenv()
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELELINK")
BASE_URL = os.getenv("BASE_URL")

# OpenAI Client setup
client = OpenAI(
    api_key=OPEN_AI_KEY,
    base_url=BASE_URL,
)

# Context class
class Reference:
    def __init__(self) -> None:
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    def clear(self):
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]


reference = Reference()
model_name = "provider-5/o3-mini-low"

# Telegram bot setup
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

# /start command
@dispatcher.message_handler(commands=["start"])
async def command_start_bot(message: types.Message):
    await message.reply("👋 Hi! I'm Sumit's little bot. How can I help you?")

# /clear command
@dispatcher.message_handler(commands=["clear"])
async def command_clear(message: types.Message):
    reference.clear()
    await message.reply("✅ Cleared previous conversation.")

# /help command
@dispatcher.message_handler(commands=["help"])
async def help_command(message: types.Message):
    help_text = (
        "🤖 <b>Bot Help</b>\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/clear - Clear past conversation\n"
    )
    await message.reply(help_text, parse_mode="HTML")

# Main chat handler
@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    try:
        user_msg = {"role": "user", "content": message.text}
        reference.messages.append(user_msg)

        completion = client.chat.completions.create(
            model="provider-5/gpt-3.5-turbo",
            messages=reference.messages,
            max_tokens=200
        )

        response_text = completion.choices[0].message.content.strip()

        assistant_msg = {"role": "assistant", "content": response_text}
        reference.messages.append(assistant_msg)

        await message.reply(response_text)

    except Exception as e:
        print(f"❌ Error: {e}")
        await message.reply("❌ Something went wrong while contacting the AI.")

# Start polling
if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)
