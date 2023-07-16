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
from root.config import Config
from root.messages import Translation

log = logging.getLogger(__name__)


@Client.on_message(filters.command("start"))
async def start_msg(c,m):
    try:
       await m.reply_text(
            text=Translation.START_TEXT,
            quote=True, 
            reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton('⋆ Support ⋆', url=f"https://t.me/WizardBotHelper"),InlineKeyboardButton('⋆ 𝙾𝚠𝚗𝚎𝚛 ⋆', url="https://t.me/{OWNER_USERNAME}")]])),
            disable_web_page_preview=True
      ) 
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

async def force_join(client: Client, msg: Message) -> None:
    if Config.FORCEJOIN != "":
        try:
            user_state = await client.get_chat_member(Config.FORCEJOIN_ID, msg.from_user.id)
            if user_state.status == "kicked":
                await msg.reply_text("You were kicked from the chat. You can't use this bot.")
                return
        except UserNotParticipant:
            forcejoin = Config.FORCEJOIN
            await msg.reply_text("Join the given chat in order to use this bot.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Updates Channel", url=f"{forcejoin}")]]))
            return
        except ChatAdminRequired:
            renamelog.error("The bot is not the admin in the chat make it admin first.")
            return
        except UsernameNotOccupied:
            renamelog.error("Invalid FORCEJOIN ID can find that chat.")
            return
        except:
            renamelog.exception("The ID should be of the channel/ group that you want the user to join.")
            return

    await msg.continue_propagation()
