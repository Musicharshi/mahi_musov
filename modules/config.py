import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID,"15418866"))
API_HASH = getenv("API_HASH,"dbbf679a4b429fab1bfea0b52b8f9be8")
BOT_TOKEN = getenv("BOT_TOKEN,"5850385258:AAGgtswykyvc9OO9i1hHlECPRMmTvtBruDI")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION,"BQDrRfIAu752luI5VI0LXu4wNmSCWZLLb0xnnRmOwdJgBGAWxsHrjMovqbvTT0zeIk_4v792tGF6E_DVSfxeBtoyhgra72CkCUVRBCMBsi762SjsI3oRa1sqsrslgZ611WSTcPwMnYyVHqBY5qJf1Li4XK9SGyuwh9yGw_b3EMM4lHnHC6Gr2e4HzqRAIsfr5DUBrKiVqxIRabnO7G9exFITCvX7hGrwKaOI_foeYYhpc_m0tj6JGz5Y7J6-h3m_SkbzrU3JMSZmyqyyj2FYgIU_YZ7p6UDFILHHGQz4bURWboexgpgv1gG_981jfQwDBjIM5lzePRZZ6u2FoD2E-V1IPjlA7gAAAAFfhezDAA")
OWNER_USERNAME = getenv("OWNER_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
aiohttpsession = aiohttp.ClientSession()
