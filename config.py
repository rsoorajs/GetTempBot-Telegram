import os

BOT_NAME = "HK_TempTelegram"
GOOGLE_URL_SHORTEN_API = ""
API_TOKEN = os.environ.get("API_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
CHANNEL_REPLY_ID = os.environ.get("CHANNEL_REPLY_ID")
CHANNEL_REPLY_TELETHON_ID = os.environ.get("TELETHON_ID")
CHANNEL_REPLY_TELETHON_HASH = os.environ.get("TELETHON_HASH")
POLLING = False
DB_URL = os.environ.get("DB_URL")
#DB_URL = 'postgres://root@localhost:5432/GetTempBot'

CLIENT_API_ID = os.environ.get("APP_ID")
CLIENT_API_HASH =os.environ.get("API_HASH")
CLIENT_PHONE = os.environ.get("PHONE")
CLIENT_2FA_PASSWORD = os.environ.get("PASSWORD")
