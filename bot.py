import os
import requests
from datetime import datetime, timezone, timedelta

TOKEN = os.environ.get("TELEGRAM_TOKEN")

def ambil_chat_id_otomatis():
    if not TOKEN:
        print("ERROR: TELEGRAM_TOKEN kosong! Pastikan sudah disimpan di GitHub Secrets dengan nama TELEGRAM_TOKEN.")
        return None

    url = f"https://telegram.org{TOKEN}/getUpdates"
    res = requests.get(url)
    
    if res.status_code != 200:
        print(f"ERROR dari Telegram (Status {res.status_code}): {res.text}")
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
        print("Gagal: Chat ID tidak ditemukan. Kirim pesan '/start' ke bot Anda di Telegram terlebih dahulu.")
        return

    url = f"https://telegram.org{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": teks, "parse_mode": "HTML"}
    res = requests.post(url, data=payload)
    print("Hasil kirim pesan:", res.text)

if __name__ == "__main__":
    wib = timezone(timedelta(hours=7))
    waktu_sekarang = datetime.now(wib).strftime("%d-%m-%Y %H:%M:%S WIB")
    kirim_pesan(f"🤖 <b>Bot Aktif!</b>\nWaktu: <code>{waktu_sekarang}</code>")
