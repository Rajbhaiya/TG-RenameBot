from pyrogram import Client, filters
from utils.database.Thumbnail import get_all_chats
import os
from root.config import Config
from root.messages import Translation

log = logging.getLogger(__name__)

@Client.on_message(filters.command("stats") & filters.user(int(Config.OWNER_ID))
async def gi_stat(c, m):
    al = get_all_chats()
    await message.reply_text(f"Total Chats in Database - {len(al)}", quote=True)
    
@Client.on_message(filters.command("broadcast") & filters.user(Config.OWNER_ID))
async def bcast(c, m):
    if message.reply_to_message:
        MSG = message.reply_to_message
    else:
        return await message.reply_text("First send me the message that you want to send to the other users of this bot! <b>Then as a reply to it send <code>/broadcast</code></b>")
    m = await message.reply_text("`Broadcasting..`")
    ALLCHATS = get_all_chats()
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
      await message.reply_document("ErrorReport.txt", caption="Errors on Broadcast")
      os.remove("ErrorReport.txt")
    await m.delete()
