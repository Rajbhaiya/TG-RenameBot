from pyrogram import Client, filters
from root.utils import *
import os
from root.config import Config
from root.messages import Translation

log = logging.getLogger(__name__)
    
@Client.on_message(filters.command("broadcast") & filters.user(Config.OWNER_ID))
async def bcast(c, m):
    if m.reply_to_message:
        MSG = m.reply_to_message
    else:
        return await m.reply_text("First send me the message that you want to send to the other users of this bot! <b>Then as a reply to it send <code>/broadcast</code></b>")
    m = await m.reply_text("`Broadcasting..`")
    ALLCHATS =  get_users()
    SUCE = 0
    FAIL = 0
    STR = "ERROR Report !\n\n"
    for chat in ALLCHATS:
        try:
            await MSG.copy(chat)
            SUCE += 1
        except Exception as e:
            FAIL += 1
            STR += f"{chat} - {str(e)}"
    await message.reply_text(
        f"Successfully Broadcasted to {SUCE} Chats\nFailed - {FAIL} Chats !"
    )
    if FAIL > 0:
      await m.edit_text("Generating Error Report !")
      open("ErrorReport.txt", "w").write(STR)
      await m.reply_document("ErrorReport.txt", caption="Errors on Broadcast")
      os.remove("ErrorReport.txt")
    await m.delete()
