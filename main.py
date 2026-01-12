import requests
import time

TOKEN = "7432590124:AAE2WaUxe-xjkQ7a9Biwk1YWkGU_pFSCj24"
CHAT_ID = "303839054"

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send(msg):
    try:
        requests.post(URL, data={"chat_id": CHAT_ID, "text": msg})
    except Exception as e:
        print("Gagal kirim pesan:", e)

send("🤖 BOT ONLINE 24 JAM (RAILWAY)")

while True:
    send("🤖 BOT MASIH ONLINE")
    time.sleep(3600)
