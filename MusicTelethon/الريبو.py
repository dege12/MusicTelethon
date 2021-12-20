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
    loli = await m.reply("**- هلا بك عزيزي**")
    await loli.edit("**- هلا بك عزيزي المطور جار**")
    await loli.edit("**- هلا بك عزيزي المطور جار اعادة**")
    await loli.edit("**- اهلا بك عزيزي المطور جار اعادة تشغيل**")
    await loli.edit("**- اهلا بك عزيزي المطور جار اعادة تشغيل البوت .**")
    await loli.edit("**- من **")
    await loli.edit("**- من فضلك**")
    await loli.edit("**- من فضلك انتظر .**")
    await loli.edit("**- من فضلك انتظر قليلاً .**")
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
- ➮ [𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ](t.me/MQQQS) """
    await m.reply(HELP)
@Client.on_message(filters.command(["سورس"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>- أهلاً {m.from_user.mention}!

↠  [𓅓𝗠𝗔𝗦𝗧𝗘𝗥](t.me/ZDDDU)\n↠  [𓅔𝗖𝗛𝗔𝗡𝗡𝗘𝗟](t.me/MQQQS)\n**- المطور الاساسي ↠** [𝐙 𝐀 𝐈 𝐃 🎼](t.me/ZDDDU)\n**- باقي مطورين البوت : **\n➢ [𝐄 𝐬 𝐬 𝐚 ✪](t.me/E_4_B) \n ➢ [𝐆𝐡𝐚𝐢𝐝𝐚𝐚](t.me/IGIDD) \n ➢ [𝒌 𝒐 𝒌 𝒐](t.me/T_G_L)

"""
    await m.reply(REPO, disable_web_page_preview=True)
