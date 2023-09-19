import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "EA_Y_N")
    CHANNEL = os.environ.get("CHANNEL", "EA_Y_N")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b6402152be44d90836339.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/b6402152be44d90836339.jpg")
