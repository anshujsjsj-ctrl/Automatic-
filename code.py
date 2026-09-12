import time
import requests
import google.generativeai as genai
from datetime import datetime, timedelta
import pytz
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

# ===== CONFIG (yaha apni cheezein daalo) =====
BOT_TOKEN = "8617014423:AAEztr2WNnWRbonUQo-nNhnUvpkdaMC7uMQ"   # 👈 BotFather wala token
GEMINI_API_KEY = "AQ.Ab8RN6LPNPpDffeHhqKAUp2mpPM30di8NobJa-lu8MucKh3ScQ"             # 👈 aistudio.google.com se free key lo
GROUP_IDS = [
    "-1003565032579",  # 👈 Group 1
    "-1002222222222",  # 👈 Group 2
    "-1003333333333",  # 👈 Group 3
    "-1004444444444",  # 👈 Group 4
    "-1005555555555",  # 👈 Group 5
    "-1006666666666",  # 👈 Group 6
    "-1007777777777",  # 👈 Group 7
    "-1008888888888",  # 👈 Group 8
    "-1009999999999",  # 👈 Group 9
    "-1001010101010",  # 👈 Group 10
]
LIKE_MESSAGE = "/like ind 8573041578"
# =============================================

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# ---------- AI COMMAND ----------
async def ai_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("❓ Kuch poocho! Jaise: /ai IPL ka score batao")
        return
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    try:
        response = model.generate_content(question)
        await update.message.reply_text(f"🤖 {response.text}")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ---------- AUTO LIKE (roz 4 baje) ----------
def send_like_messages():
    for gid in GROUP_IDS:
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={"chat_id": gid, "text": LIKE_MESSAGE})
            print(f"✅ Like message bhej diya: {gid}")
            time.sleep(2)
        except Exception as e:
            print(f"❌ Error ({gid}): {e}")

async def like_scheduler(app):
    IST = pytz.timezone("Asia/Kolkata")
    while True:
        now = IST.now()
        target = now.replace(hour=4, minute=0, second=0, microsecond=0)
        if now >= target:
            target += timedelta(days=1)
        wait = (target - now).total_seconds()
        print(f"⏰ Agla like message: {target} ({int(wait)} sec baad)")
        await asyncio.sleep(wait)
        send_like_messages()

# ---------- MAIN ----------
async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("ai", ai_command))

    print("🤖 Bot chalu! /ai command aur 4 baje like message dono active hai...")

    # Like scheduler background me chalao
    asyncio.create_task(like_scheduler(app))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()  # hamesha chalte raho

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())