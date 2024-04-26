
# --------------M----------------------------------

import os
from os import getenv
from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------
# ------------------------------------------------
LOGGER_ID = int(os.environ.get("LOGGER_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# ------------------------------------------------
MESSAGE_DUMP = int(os.environ.get("MESSAGE_DUMP"))
#---------------------------------------------------
DB_URI = os.environ.get("DB_URI")
#----------------------------------------------
DB_NAME = os.environ.get("DB_NAME")
#-------------------------------------------
BDB_URI = config("BDB_URI",default=None)
NO_LOAD = config("NO_LOAD", default="").split()
PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_bots_network")
SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_bots_network")
WORKERS = int(config("WORKERS", default=16))
TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
