"""
© Mrvishal2k2
RenameBot
This file is a part of mrvishal2k2 rename repo
Dont kang !!!
© Mrvishal2k2
"""
import os


class Config(object):
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", False)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "cant_think_1")
    APP_ID = int(os.environ.get("APP_ID", "13675555"))
    API_HASH = os.environ.get("API_HASH", "c0da9c346d2c45dbc7ec49a05da9b2b6")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5304876457:AAFfrsInLodQuWclHyyC7-GzLGbS77tmmFk")
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "5591954930").split()]
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./bot/DOWNLOADS")
    DB_URI = os.environ.get("DATABASE_URL", "postgres://vyjeeprz:QZJFgX_Q5WXo81HDWoDMnYgMz2nvfRQW@snuffleupagus.db.elephantsql.com/vyjeeprz")
    # owner is for log cmd only owner can use (this can be multiple users)
    OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "5591954930")]
    FORCEJOIN = os.environ.get("FORCEJOIN", "Wizard_Bots")
    FORCEJOIN_ID = os.environ.get("FORCEJOIN_ID", "-1OO1721659524")
