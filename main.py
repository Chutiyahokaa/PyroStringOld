import os
import pyrogram
from pyrogram import Client

api_id = 21630147
api_hash = "394962449c1583fb83d4dbe1990acb3a"

try:
   os.remove("paradise.session")
except:
     pass
with Client("sahu", api_id=api_id, api_hash=api_hash) as app:
    session = f"**🥀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 » 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 💞**\n\n`{app.export_session_string()}`\n\n**💥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: [PARADISE](https://t.me/HEY_PARADISE) ✨**"
    app.send_message("me", session, disable_web_page_preview=True)
    try:
        app.join_chat("")
        app.join_chat("")
        app.join_chat("")
        app.join_chat("")
    except:
        pass
    print(f"✅ String Session Has 🌟 Been Sent\nTo Your 🔥 Saved Message ✨ ...")
    os.remove("paradise.session")

