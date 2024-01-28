import discord
from discord.ext import commands

from src import settings
from src.logger import setup_logger

_log = setup_logger('src.main')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
server_id = discord.Object(settings.DISCORD_SERVER_ID)


@bot.event
async def on_ready():
    _log.info('Logged')
    try:
        synced = await bot.tree.sync(guild=server_id)
        _log.info(f'Synced {len(synced)} command(s)')
    except Exception as e:
        _log.error(e)


@bot.tree.command(name='hello', guild=server_id, description='teste de descrição')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('Hello World!!')

if __name__ == '__main__':
    bot.run(settings.DISCORD_TOKEN)
