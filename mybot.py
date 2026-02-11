from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8321454833:AAFwZ4-z-4EdQM8_8PxbT7QXtpOFDXU5zKw"
WEBHOOK_URL = "https://maisam-4wh0.onrender.com/webhook"  # لینک سرویس Render شما + /webhook

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("به ربات میثم خوش آمدید!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# این قسمت Webhook رو فعال می‌کنه
app.run_webhook(
    listen="0.0.0.0",
    port=10000,
    webhook_url=WEBHOOK_URL
)
