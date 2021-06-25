import asyncio
import time

from telethon import version
from userbot.utils import admin_cmd, sudo_cmd

from Lion import ALIVE_NAME, StartTime, lionver
from Lion.helper import functions as dcdef 
from Lion.LionConfig import Config, Var

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "∂αяк υℓтяα υsεя"

# Thanks to Sipak bro and Aryan..
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
# modded for Dark ultra Userbot
global fuk
fuk = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/88658a686a2ed5e66b7b9.jpg"
""" =======================CONSTANTS====================== """
# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "∂αяк υктяα  ʊֆɛʀɮօȶ ɨֆ օռʟɨռɛ!"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else "https://telegra.ph/file/88658a686a2ed5e66b7b9.jpg"
lionemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**〢**"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#

@Lion.on(admin_cmd(pattern=r"alive"))
@Lion.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def hmm(yes):
    await yes.get_chat()
    global fuk
    fuk = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - StartTime))
    pm_caption = f"{Darkultraemoji}**{CUSTOM_ALIVE}**\n\n"
    pm_caption += f"{Darkultraemoji}**Mʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ**\n\n"
    pm_caption += f"{Darkultraemoji} Aʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n"
    pm_caption += f"{Darkultraemoji} **Darkultra 𝙑𝙀𝙍𝙎𝙄𝙊𝙉**: `{lionver}`\n"
    pm_caption += f"{Darkultraemoji} **𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉** ☞ {version.__version__}\n"
    pm_caption += f"{Darkultraemoji} **𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝘾𝙃𝘼𝙉𝙉𝙀𝙇** ☞ [ᴊᴏɪɴ](https://t.me/Dark_ultra_support)\n"
    pm_caption += f"{Darkultraemoji} **𝙇𝙄𝘾𝙀𝙉𝙎𝙀**  ☞ [𝚃𝙴𝙰𝙼 Darkultra 𝚄𝙱](https://github.com/kaal0408)\n"
    pm_caption += (
        f"{Darkultraemoji} **𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔** ☞ [Dark ultra 𝚄𝙱](https://github.com/kaal0408/darkultra)\n\n"
    )
    pm_caption += f"{Darkultraemoji} **D a r k u l t r a 𝙐𝙋𝙏𝙄𝙈𝙀** ☞ {uptime}\n\n"
    pm_caption += f"{Darkultramoji} **𝙈𝙔 𝙋𝙀𝙍𝙊 𝙈𝘼𝙎𝙏𝙀𝙍** ☞ [{DEFAULTUSER}](tg://user?id={fuk})\n"
    on = await borg.send_file(
        yes.chat_id, file=ALV_PIC, caption=pm_caption, link_preview=False
    )

# This Alive is for Dark ultra modded from dc 
# use with credits
