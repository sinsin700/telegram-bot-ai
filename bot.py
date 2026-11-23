import os
import requests
from datetime import datetime, timezone, timedelta

TOKEN = os.environ.get("TELEGRAM_TOKEN")

def ambil_chat_id_otomatis():
    url = f"https://telegram.org{TOKEN}/getUpdates"
    response = requests.get(url).json()
    
    if response.get("result"):
        pesan_terakhir = response["result"][-1]
        if "message" in pesan_terakhir:
            return pesan_terakhir["message"]["chat"]["id"]
    return None

def kirim_pesan(teks):
    chat_id = ambil_chat_id_otomatis()
    if not chat_id:
        print("Gagal: Kirim pesan '/start' dulu ke bot Anda di Telegram.")
        return

    url = f"https://telegram.org{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": teks, "parse_mode": "HTML"}
    response = requests.post(url, data=payload)
    print("Status:", response.text)

if __name__ == "__main__":
    wib = timezone(timedelta(hours=7))
    waktu_sekarang = datetime.now(wib).strftime("%d-%m-%Y %H:%M:%S WIB")
    kirim_pesan(f"🤖 <b>Bot Aktif!</b>\nWaktu: <code>{waktu_sekarang}</code>")
