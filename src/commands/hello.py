import discord
from discord.ext import commands

from src import main


@commands.slash_command(name='hello', guild=main.server_id, description='teste de descrição')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('Hello World!!')


def setup(client):
    client.add_application_command(hello)
