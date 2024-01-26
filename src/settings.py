import os

from loadotenv import load_env

load_env()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
NASA_TOKEN = os.getenv('NASA_TOKEN')
