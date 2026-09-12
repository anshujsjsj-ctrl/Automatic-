import time
import requests
from datetime import datetime, timedelta
import pytz

# ===== CONFIG =====
BOT_TOKEN = "8617014423:AAEztr2WNnWRbonUQo-nNhnUvpkdaMC7uMQ"   # 👈 Yaha apna BOT TOKEN daalo

GROUP_IDS = [
    "-1003565032579",   # 👈 Group 1 ka ID
    "-1002222222222",   # 👈 Group 2 ka ID
    "-1003333333333",   # 👈 Group 3 ka ID
    "-1004444444444",   # 👈 Group 4 ka ID
    "-1005555555555",   # 👈 Group 5 ka ID
    "-1006666666666",   # 👈 Group 6 ka ID
    "-1007777777777",   # 👈 Group 7 ka ID
    "-1008888888888",   # 👈 Group 8 ka ID
    "-1009999999999",   # 👈 Group 9 ka ID
    "-1001010101010",   # 👈 Group 10 ka ID
]

MESSAGE = "/like ind 8573041578"
# ==================

IST = pytz.timezone("Asia/Kolkata")

def send_message(chat_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": MESSAGE}
    r = requests.post(url, data=data)
    if r.json().get("ok"):
        print(f"✅ Bhej diya: {chat_id}")
    else:
        print(f"❌ Error ({chat_id}): {r.text}")

def main():
    print(f"🤖 Bot start! Roz 4:00 AM IST pe {len(GROUP_IDS)} groups me message jayega...")
    while True:
        now = IST.now()
        target_time = now.replace(hour=4, minute=0, second=0, microsecond=0)
        if now >= target_time:
            target_time += timedelta(days=1)

        wait_secs = (target_time - now).total_seconds()
        print(f"⏰ Agla message: {target_time} ({int(wait_secs)} sec baad)")
        time.sleep(wait_secs)

        for gid in GROUP_IDS:
            send_message(gid)
            time.sleep(2)  # har group me 2 sec gap (spam se bachne ke liye)

if __name__ == "__main__":
    main()
