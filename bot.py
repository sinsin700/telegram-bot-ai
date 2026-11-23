import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Konfigurasi logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ⚠️ PENTING: Nama di sini disesuaikan dengan nama Secret di GitHub (TELEGRAM_TOKEN)
TOKEN = os.environ.get("TELEGRAM_TOKEN")

if not TOKEN:
    raise RuntimeError("❌ TELEGRAM_TOKEN tidak ditemukan! Pastikan Secret di GitHub sudah benar.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Halo {update.effective_user.first_name}! 👋 Bot berhasil berjalan.")

async def balas_pesan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Kamu mengirim: {update.message.text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, balas_pesan))

    print("✅ Bot berjalan... Menunggu pesan dari Telegram.")
    app.run_polling()

if __name__ == "__main__":
    main()
