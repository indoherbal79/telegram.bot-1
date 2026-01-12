import requests
import time

TOKEN = 7432590124:AAG7fcxBCWr41n2a-03Ha0XlzFE9abthvSM
CHAT_ID = "303839054"

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send(msg):
    requests.post(URL, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

send("🤖 BOT ONLINE 24 JAM (RAILWAY)")

while True:
    time.sleep(3600)
