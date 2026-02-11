from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("به ربات میثم خوش امدید ")
app = ApplicationBuilder().token("8321454833:AAFwZ4-z-4EdQM8_8PxbT7QXtpOFDXU5zKw").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
