import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID,"26119931"))
API_HASH = getenv("API_HASH,"79e5b0d03df604b1bd1ee8b2f753372e")
BOT_TOKEN = getenv("BOT_TOKEN,"5579550471:AAFm7fzyAMLQ58g-mdeiAR9q61_efqfy9XE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION,"BQBUg1tj4wgXT7jM3EipMwwrjhV1vvZ1PIGz856YhrYFVulykfLvfOIrbfRXMg97nhcbnNhN_bhacp3DvFlPER5M0jWafJtN8IlUk4P-JWs6jwzlzStjF_ZxLVl4JFhXVNXrrotPCcwOWgmcMp6dYix9z3VuUj-mIuQIXyxM0iETS0zCg223CK4oZj2w7PBVKvrj_o5FCm95H2cYnrD7F2XWq8KmDCVaoZxD8Sb3lZSzW0_vG6viRW49JxsMpZwfBhHzkLrqsaQ6osOYTnlHSkck3KE3ctipoFYBXbtIaOBUDlKakdirhGyIPWcAl_sJ7YMBtV2GKw_fvFSdPVtyTFmiAAAAAVw9gkoA")
OWNER_USERNAME = getenv("OWNER_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP","https://t.me/puuusy_gruup")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL","https://t.me/puuusy_gruup")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
aiohttpsession = aiohttp.ClientSession()
