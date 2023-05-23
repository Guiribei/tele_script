from dotenv import load_dotenv
from telethon import TelegramClient, events
import os

load_dotenv()

api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
phone = os.getenv('TELEGRAM_PHONE')

keywords = ["jr", "júnior", "junior", "Jr", "Júnior", "Junior", "JUNIOR", "CLT", "clt", "PJ", "pj"]

session_file = 'my_session'
client = TelegramClient(session_file, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
        if any(keyword in event.raw_text for keyword in keywords):
        # Insert the message into the database
                if (event.chat_id == -1052992679):
                        print(f"Message recieved: {event.raw_text}")

with client:
    client.run_until_disconnected()
