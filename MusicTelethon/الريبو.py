import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["ريستارت"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("- 1")
    await loli.edit("- 2")
    await loli.edit("- 3")
    await loli.edit("- 4")
    await loli.edit("- 5")
    await loli.edit("- 6")
    await loli.edit("- 7")
    await loli.edit("- 8")
    await loli.edit("- 9")
    await loli.edit("**- تم اعادة تشغيل البوت بنجاح .**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["اوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>- عزيزي {m.from_user.mention}!

- قائمة الاوامر .
——————×—————

✪ | لتشغيل صوتية في المكالمة أرسل ↞ [ `{HNDLR}تشغيل  + اسم الاغنية` ]
✪ | لتشغيل فيديو في المكالمة  ↞ [ `{HNDLR}تشغيل_فيديو  + اسم الاغنية` ]
———————×———————

✪ | لأيقاف الاغنية او الفيديو مؤقتآ  ↞ [ `{HNDLR}مؤقت` ] 
✪ | لأعاده تشغيل الاغنية ↞  [ `{HNDLR}متابعه` ]
✪ | لأيقاف الاغنية  ↞ [ `{HNDLR}ايقاف` ] 
———————×———————

✪ | لتحميل صوتية أرسل ↞ [ `{HNDLR}تحميل + اسم الاغنية او الرابط` ]
✪ | لتحميل فيديو  ↞  [ `{HNDLR}تحميل_فيديو + اسم الاغنية او الرابط` ]
———————×———————

✪ | لتخطي الاغنيه ↞ [ `{HNDLR}التالي`  ]
✪ | لعرض معلومات السورس ↞  [ `{HNDLR}سورس` ]
———————×———————
- ➮ [𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✪](t.me/E_B_3) """
    await m.reply(HELP)
@Client.on_message(filters.command(["سورس"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>- أهلاً {m.from_user.mention}!

🎼 قناة البوت : [𝑩𝒐𝒕 𝑪𝒉𝒂𝒏𝒏𝒆𝒍  𝅘𝅥𝅮](t.me/E_B_3)\n- 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : [𝐙 𝐀 𝐈 𝐃 🇵🇸](t.me/ZDDDU)

"""
    await m.reply(REPO, disable_web_page_preview=True)
