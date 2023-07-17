'''
RenameBot
Thanks to Spechide Unkle as always for the concept  ♥️
This file is a part of mrvishal2k2 rename repo 
Dont kang !!!
© Mrvishal2k2
'''
import os, logging
from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from root.config import Config
from root.messages import Translation

log = logging.getLogger(__name__)


@Client.on_message(filters.private)
async def force_join(c, m):
    if "https://t.me/Wizard_Bots" != "":
        try:
            user_state = await c.get_chat_member(-1OO1721659524, m.from_user.id)
            if user_state.status == "kicked":
                await m.reply_text("You were kicked from the chat. You can't use this bot.")
                return
        except UserNotParticipant:
            forcejoin = "https://t.me/Wizard_Bots"
            await m.reply_text("Join the given chat in order to use this bot.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Updates Channel", url=f"{forcejoin}")]]))
            return
        except ChatAdminRequired:
            log.error("The bot is not the admin in the chat make it admin first.")
            return
        except UsernameNotOccupied:
            log.error("Invalid FORCEJOIN ID can find that chat.")
            return
        except:
            log.exception("The ID should be of the channel/ group that you want the user to join.")
            return

    await msg.continue_propagation()


@Client.on_message(filters.command("start"))
async def start_msg(c,m):
    try:
       await m.reply_text(
            text=Translation.START_TEXT,
            quote=True, 
            reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton('⋆ Support ⋆', url=f"https://t.me/WizardBotHelper"),InlineKeyboardButton('⋆ 𝙾𝚠𝚗𝚎𝚛 ⋆', url="https://t.me/cant_think_1")]]))
    except Exception as e:
        log.error(str(e))

@Client.on_message(filters.command("help"))
async def help_user(c,m):
    try:
       await m.reply_text(text=Translation.HELP_USER,quote=True)
    except Exception as e:
        log.info(str(e))


@Client.on_message(filters.command("log") & filters.private & filters.user(Config.OWNER_ID))
async def log_msg(c,m):
  z =await m.reply_text("Processing..", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Log.txt", True)
     await z.delete()
  else:
    await z.edit_text("Log file not found")
