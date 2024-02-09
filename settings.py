import os

from dotenv import load_dotenv
import discord

DISCORD_API_SECRET = os.environ['DISCORD_API_TOKEN']
GUILDS_ID = discord.Object(id=int(os.environ['GUILD']))




load_dotenv()



LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_Loggers": False,
    "formatters":{
        "verbose":{
            "format": "%(Levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard":{
            "format": "%(Levelname)-10s - %(name)-15s : %(message)s"
        }

    },
    "handler":{
        "console": {
            'Level' : "DEBUG",
            'class' : "logging.StreamHandler",
            'formatter' : "standard",
        },
        "console2": {
            'Level': "WARNING",
            'class': "Logging.StreamHandler",
            'formatter' : "simple",
        },
        "file": {
            'Level': "INFO",
            'class': "Logging.FileHandler",
            'filename' : "Logs/info.Log",
            'mode': "w",
            'formatter' : "simple"
        }
    },
    "Loggers":{
        "bot":{
            'handlers': ['console'],
            "Level": "INFO",
            "propagate":False
        },
        "discord":{
            'handlers': ['console2', "file"],
            "Level": "INFO",
            "propagate":False
        }
    }
}