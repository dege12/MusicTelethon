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


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["restart","zaid","غدو","عسعس","كوكو"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("**مرحباً عزيزي المطور {m.from_user.mention}\n༄ جار اعادة تشغيل البوت 1**")
    await loli.edit("**مرحباً عزيزي المطور {m.from_user.mention}\n༄ جار اعادة تشغيل البوت 2**")
    await loli.edit("**مرحباً عزيزي المطور {m.from_user.mention}\n༄ جار اعادة تشغيل البوت 3**")
    await loli.edit("**مرحباً عزيزي المطور {m.from_user.mention}\n༄ جار اعادة تشغيل البوت 4**")
    await loli.edit("**مرحباً عزيزي المطور {m.from_user.mention}\n༄ جار اعادة تشغيل البوت 5**")
    await loli.edit("**مرحباً عزيزي المطور {m.from_user.mention}\n༄ جار اعادة تشغيل البوت 6**")
    await loli.edit("**مرحباً عزيزي المطور {m.from_user.mention}\n༄ جار اعادة تشغيل البوت 7**")
    await loli.edit("**مرحباً عزيزي المطور {m.from_user.mention}\n༄ جار اعادة تشغيل البوت 8**")
    await loli.edit("**مرحباً عزيزي المطور {m.from_user.mention}\n༄ جار اعادة تشغيل البوت 9**")
    await loli.edit("**- تم اعادة تشغيل البوت بنجاح 🧚‍♀**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["اوامر","help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>**- مرحباً {m.from_user.mention}**

 ⤃𝐌𝐚𝐝𝐚 𝐌𝐮𝐬𝐢𝐜 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🧚‍♂⤂
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅

𓏬 | لتشغيل صوتية في المكالمة أرسل ↞ ⊰ `{HNDLR}تشغيل  + اسم الاغنية` ⊱
𓏬 | لتشغيل فيديو في المكالمة  ↞ ⊰ `{HNDLR}تشغيل_فيديو  + اسم الاغنية` ⊱
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅

𓏬 | لأيقاف الاغنية او الفيديو مؤقتآ  ↞ ⊰ `{HNDLR}مؤقت` ⊱ 
𓏬 | لأعاده تشغيل الاغنية ↞  ⊰ `{HNDLR}متابعه` ⊱
𓏬 | لأيقاف الاغنية  ↞ ⊰ `{HNDLR}ايقاف` ⊱ 
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅

𓏬 | لتحميل صوتية أرسل ↞ ⊰ `{HNDLR}تحميل + اسم الاغنية او الرابط` ⊱
𓏬 | لتحميل فيديو  ↞  ⊰ `{HNDLR}فيديو + اسم الاغنية او الرابط` ⊱
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅

𓏬 | لتخطي الاغنيه ↞ ⊰ `{HNDLR}التالي`  ⊱
𓏬 | لعرض معلومات السورس ↞  ⊰ `{HNDLR}سورس` ⊱
𓏬 | لتشغيل 10 اغاني عشوائيه ↞ ⊰ `{HNDLR}عشوائيه` + معرف القناه او القروب  ⊱
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅
- ➮ [𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ⚜](t.me/MQQQS)  """
    await m.reply(HELP, disable_web_page_preview=True)
@Client.on_message(filters.command(["سورس","المطور","repo","alive","المطورين"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>⇸ **𝐖𝐞𝐥𝐜𝐨𝐦𝐞 ❪ {m.from_user.mention} ❫**

**༄ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ↠** [𝐙 𝐀 𝐈 𝐃 🎼](tg://user?id=1518220300)\n**༄ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ↠** [𝐌𝐚𝐝𝐚  𝐔𝐬𝐞𝐫𝐛𝐨𝐭 🧚‍♂](t.me/MQQQS) .\n\n༄ [𝐆𝐘𝐃𝐀𝐀 🧚‍♀](t.me/IGIDD)\n༄ [𝐄𝐒𝐒𝐀 𝄬](t.me/E_4_B)\n༄  [𝐊𝐎𝐊𝐎 メ](t.me/T_G_L)\n\n𐂂

"""
    await m.reply(REPO, disable_web_page_preview=True)

        
