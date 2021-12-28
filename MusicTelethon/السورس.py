import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("الأحد", 60 * 60 * 24 * 7),
    ("يوم", 60 * 60 * 24),
    ("الساعة", 60 * 60),
    ("الدقيقة", 60),
    ("الثانيه", 1),
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
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🏓 سرعه البوت : /b> `{delta_ping * 1000:.3f} بالثانيه` \n<b>⏳ وقت التشغيل : </b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["اعادة تشغيل","ريستارت"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("**مرحباً عزيزي المطور\n༄ جار اعادة تشغيل البوت 1**")
    await loli.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 2**")
    await loli.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 3**")
    await loli.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 4**")
    await loli.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 5**")
    await loli.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 6**")
    await loli.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 7**")
    await loli.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 8**")
    await loli.edit("**مرحباً عزيزي المالك\n༄ جار اعادة تشغيل البوت 9**")
    await loli.edit("**مرحباً عزيزي المالك\n༄ تم اعادة تشغيل البوت بنجاح **")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر","اوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HEPZ = f"""
<b>**- مرحباً {m.from_user.mention}**

 ⤃ 𝐌𝐮𝐬𝐢𝐜 𝐔𝐬𝐞𝐫𝐛𝐨𝐭‍ ⤂
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
➖ | لإعاده تشغيل البوت ↞ ⊰ `{HNDLR}اعاده_تشغيل`  ⊱
𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅✭𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅𓐅
- ➮ [𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ⚜](t.me/MQQQS)  """
    await m.reply(HELP, disable_web_page_preview=True)


@Client.on_message(filters.command(["سورس"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPZ = f"""
<b>⇸ **-  مرحباً  {m.from_user.mention} **

**༄ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ↠** [𝐙 𝐀 𝐈 𝐃 🎼](tg://user?id=1518220300)\n**༄ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ↠** [𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥‍ ⚜](t.me/MQQQS) .\n- **مالك البوت : {OWNER} **\n\n𐂂

"""
    await m.reply(REPZ, disable_web_page_preview=True)
