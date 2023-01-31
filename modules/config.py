import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID",15418866"))
API_HASH = getenv("API_HASH",dbbf679a4b429fab1bfea0b52b8f9be8")
BOT_TOKEN = getenv("BOT_TOKEN",5579550471:AAFm7fzyAMLQ58g-mdeiAR9q61_efqfy9XE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION",BQCStHHd-ufF6lGi-h3EnCiVL7RGJ66FToXxrUFXXD_DIzXSjq-b6N_T-WlEtM2ozQI3IyCtc-8nx1uPbcguqPkfH-lUt1JhXQXXiotdNTEl8WWwvaevlHneX41RJ2QUtznAlp2mVW1qagRsHrNyKoJ21_iZndsS42NGMxUgeUcdmxiDxDQ_UEKanEvXf5H2NAlClusWscvU7aYycNl9MF2iJW5O7TFeh7PgsfM54rvCsBXr94mf9dJAZsuo4dj06gapRZz9jcsBpnl6-dYt07pHzzbsk9vq8iQ3BEBhzvRSGp6pao-jbGHa0r_otHYUQJR8Nb_Vp4ZNuAsz96qnZP-wAAAAAV-F7MMA")
OWNER_USERNAME = getenv("OWNER_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP","https://t.me/puuusy_gruup")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL","https://t.me/puuusy_gruup")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
aiohttpsession = aiohttp.ClientSession()
