import os
import requests
from datetime import datetime, timezone, timedelta

# Mengambil token secara aman dari GitHub Secrets
TOKEN = os.environ.get("TELEGRAM_TOKEN")

def ambil_chat_id_otomatis():
    if not TOKEN:
        print("ERROR: TELEGRAM_TOKEN belum terbaca dari GitHub Secrets.")
        return None

    url = f"https://telegram.org{TOKEN}/getUpdates"
    res = requests.get(url)
    
    if res.status_code != 200:
        print(f"ERROR Telegram ({res.status_code}): {res.text}")
        return None

    data = res.json()
    if data.get("result"):
        pesan_terakhir = data["result"][-1]
        if "message" in pesan_terakhir:
            return pesan_terakhir["message"]["chat"]["id"]
    return None

def kirim_pesan(teks):
    chat_id = ambil_chat_id_otomatis()
    if not chat_id:
        print("Gagal: Chat ID tidak ditemukan. Buka bot Anda di Telegram dan kirim pesan '/start' terlebih dahulu.")
        return

    url = f"https://telegram.org{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": teks,
        "parse_mode": "HTML"
    }
    
    res = requests.post(url, data=payload)
    if res.status_code == 200:
        print(f"SUKSES! Pesan terkirim ke Chat ID: {chat_id}")
    else:
        print(f"Gagal mengirim pesan: {res.text}")

if __name__ == "__main__":
    wib = timezone(timedelta(hours=7))
    waktu_sekarang = datetime.now(wib).strftime("%d-%m-%Y %H:%M:%S WIB")

    pesan = (
        f"🤖 <b>Bot Telegram Aktif!</b>\n\n"
        f"Status: <b>Berjalan Normal di GitHub Actions</b>\n"
        f"Waktu Eksekusi: <code>{waktu_sekarang}</code>"
    )

    kirim_pesan(pesan)
