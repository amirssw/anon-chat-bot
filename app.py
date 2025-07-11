from flask import Flask, request
import telegram
import os

app = Flask(name)
TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text
    bot.send_message(chat_id=chat_id, text="پیام شما دریافت شد!")
    return "ok"

@app.route("/")
def home():
    return "ربات فعال است"

if name == "main":
    app.run()
