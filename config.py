import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
OWNER = os.getenv("OWNER")
OWNER_NAME = os.getenv("OWNER_NAME")
HNDLR = os.getenv("HNDLR", "$")
PING_PIC = os.getenv("PING_PIC") 
THUMB_PIC = os.getenv("THUMB_PIC")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
