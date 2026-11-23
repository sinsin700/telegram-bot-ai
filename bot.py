import requests
from datetime import datetime, timezone, timedelta

# Cukup isi TOKEN saja
TOKEN = "9111187679:AAHIkybBcXQKPgQyMh8hsnNvU6P0Wy8J-PU"

def ambil_chat_id_otomatis():
    url = f"https://telegram.org{TOKEN}/getUpdates"
    response = requests.get(url).json()
    
    # Mengambil chat_id dari pesan terakhir yang masuk ke bot
    if response.get("result"):
        pesan_terakhir = response["result"][-1]
        if "message" in pesan_terakhir:
            return pesan_terakhir["message"]["chat"]["id"]
    return None

def kirim_pesan(teks):
    chat_id = ambil_chat_id_otomatis()
    
    if not chat_id:
        print("Gagal: Belum ada riwayat chat. Buka bot Anda di Telegram dan kirim pesan '/start' dulu.")
        return

    url = f"https://telegram.org{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": teks,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"Pesan berhasil dikirim otomatis ke Chat ID: {chat_id}")
    else:
        print(f"Gagal mengirim pesan: {response.text}")

if __name__ == "__main__":
    wib = timezone(timedelta(hours=7))
    waktu_sekarang = datetime.now(wib).strftime("%d-%m-%Y %H:%M:%S WIB")

    pesan = (
        f"🤖 <b>Laporan Bot Otomatis</b>\n\n"
        f"Status: <b>Berhasil Tanpa Input Chat ID!</b>\n"
        f"Waktu: <code>{waktu_sekarang}</code>"
    )

    kirim_pesan(pesan)
