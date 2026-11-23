import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Ambil token dari environment variable
TOKEN = os.environ.get("TELEGRAM_TOKEN")

if not TOKEN:
    raise RuntimeError("❌ BOT_TOKEN tidak ditemukan di environment variable!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Halo {update.effective_user.first_name}! 👋")

async def balas_pesan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Kamu mengirim: {update.message.text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, balas_pesan))
    print("Bot berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
