"""
© Mrvishal2k2
RenameBot
This file is a part of mrvishal2k2 rename repo
Dont kang !!!
© Mrvishal2k2
"""
import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "13675555"))
    API_HASH = os.environ.get("API_HASH", "c0da9c346d2c45dbc7ec49a05da9b2b6")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6113104447:AAHHE56nNSAQEr6KBbCN4vNEwNjki_8q7ZY")
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "5591954930").split()]
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./bot/DOWNLOADS")
    DB_URI = os.environ.get("DATABASE_URL", "postgres://kkktawwp:c9JreackKuiGxphwp0jDXlPilw4SFKLv@mouse.db.elephantsql.com/kkktawwp")
    # owner is for log cmd only owner can use (this can be multiple users)
    OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID").split("5591954930 ")]
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "cant_think_1")
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", False)
