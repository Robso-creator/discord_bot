import os

from loadotenv import load_env

load_env()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_SERVER_ID = os.getenv('DISCORD_SERVER_ID')
NASA_TOKEN = os.getenv('NASA_TOKEN')
