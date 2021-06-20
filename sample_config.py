#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3


import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")

    # Group / channel Id: Members to which inline query answered
    DEFAULT_CHAT_ROOM = int(os.environ.get("DEFAULT_CHAT_ROOM", ""))

    # List of admin user ids for special functions(Storing as an array)
    ADMIN_USERS = set(int(x) for x in os.environ.get("ADMIN_USERS", "").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
