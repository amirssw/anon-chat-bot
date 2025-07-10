from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

users = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! شما به ربات چت ناشناس وصل شدید. منتظر باشید تا یک کاربر به شما متصل شود.")
    users.append(update.message.chat_id)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sender_id = update.message.chat_id
    for user in users:
        if user != sender_id:
            await context.bot.send_message(chat_id=user, text=update.message.text)

app = ApplicationBuilder().token("7530531822:AAHPGBMzrBYcZ3krh0ujC8yVJSFCohfTQIY").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

app.run_polling()
