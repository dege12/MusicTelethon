import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS, OWNER_NAME, OWNER, PING_PIC

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("**Sat**", 60 * 60 * 24 * 7),
    ("**Day**", 60 * 60 * 24),
    ("**h**", 60 * 60),
    ("**m**", 60),
    ("**s**", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنق","ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡ | جار حساب سرعه البوت")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"**✶ مرحباً بك عزيزي بوت الأغاني يعمل بنجاح .**\n[ㅤㅤㅤㅤㅤㅤ]({PING_PIC})\n**༄ 𝐏𝐢𝐧𝐠 ⇝** `{delta_ping * 1000:.3f}ms ` \n**༄ 𝐔𝐩𝐭𝐢𝐦𝐞 ⇝**  {uptime}\n\n  ༄  [𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 🎼](t.me/ZDDDU)\n  ༄  [𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ⚜](t.me/MQQQS)"
    )

@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart","zaid","ريستارت"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    mada = await m.reply("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 1**")
    await mada.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 2**")
    await mada.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 3**")
    await mada.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 4**")
    await mada.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 5**")
    await mada.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 6**")
    await mada.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 7**")
    await mada.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 8**")
    await mada.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 9**")
    await mada.edit("**مرحباً عزيزي المالك\n༄ تم اعادة تشغيل البوت بنجاح ✔️**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["اوامر","مساعدة"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HEPZ = f"""
**- مرحباً {m.from_user.mention}**

 ⤃ 𝐌𝐮𝐬𝐢𝐜 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 ⤂
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅

➖ | لتشغيل صوتية في المكالمة أرسل ↞ ⊰ `{HNDLR}تشغيل  + اسم الاغنية` ⊱
➖ | لتشغيل فيديو في المكالمة  ↞ ⊰ `{HNDLR}تشغيل_فيديو  + اسم الاغنية` ⊱
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅

➖ | لأيقاف الاغنية او الفيديو مؤقتآ  ↞ ⊰ `{HNDLR}مؤقت` ⊱ 
➖ | لأعاده تشغيل الاغنية ↞  ⊰ `{HNDLR}متابعه` ⊱
➖ | لأيقاف الاغنية  ↞ ⊰ `{HNDLR}ايقاف` ⊱ 
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅

➖ | لتحميل صوتية أرسل ↞ ⊰ `{HNDLR}تحميل + اسم الاغنية او الرابط` ⊱
➖ | لتحميل فيديو  ↞  ⊰ `{HNDLR}فيديو + اسم الاغنية او الرابط` ⊱
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅

➖ | لتخطي الاغنيه ↞ ⊰ `{HNDLR}التالي`  ⊱
➖ | لعرض معلومات السورس ↞  ⊰ `{HNDLR}سورس` ⊱
➖ | لتشغيل 10 اغاني عشوائيه ↞ ⊰ `{HNDLR}عشوائيه` + معرف القناه او القروب  ⊱
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅
- ➮ [𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ⚜](t.me/MQQQS) 
"""
    await m.reply(HEPZ, disable_web_page_preview=True)


@Client.on_message(filters.command(["السورس","سورس","المالك","المطور"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPZ = f"""
<b>⇸ **𝐖𝐞𝐥𝐜𝐨𝐦𝐞 ❪ {m.from_user.mention} ❫**

**༄ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ↠** [𝐙 𝐀 𝐈 𝐃 🎼](t.me/ZDDDU)\n**༄ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ↠** [𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ⚜‍](t.me/MQQQS) .\n\n**༄ 𝐎𝐰𝐧𝐞𝐫 ↠ [{OWNER_NAME}](t.me/{OWNER}) **\n\n𐂂

"""
    await m.reply(REPZ, disable_web_page_preview=True)
