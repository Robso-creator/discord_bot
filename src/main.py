from typing import Optional

import discord
import requests
from discord import app_commands
from discord.ext import commands
from discord.ui import Button
from discord.ui import View
from googletrans import Translator

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


@bot.tree.command(name='help', guild=server_id, description='teste de descrição')
@app_commands.describe(command='comando que o usuário precisa de mais detalhes')
async def help(interaction: discord.Interaction, command: Optional[str] = None):
    if command is None:
        embed = discord.Embed(
            title='Ajuda com comandos',
            description='Para melhores detalhes sobre comandos, digite: `/help <nome_comando>`',
            color=discord.Color.dark_magenta(),
        )
    else:
        desired_command = next(
            (
                _command for _command in bot.tree.walk_commands(
                    guild=server_id,
                ) if _command.name == command
            ), None,
        )

        if desired_command is None:
            _log.error('invalid command')
            await interaction.response.send_message(content=f'Comando {command} é inválido.', ephemeral=True)
            return

        else:
            _log.info(f"user asked help with command '{desired_command.name}'")
            embed = discord.Embed(
                title=f"Informações sobre comando '{desired_command.name}'",
                description=f'_Nome_: `{desired_command.name}`\n_Descrição_: `{desired_command.description}`',
                color=discord.Color.dark_magenta(),
            )

    repo_button = Button(
        label='Repositório',
        url='https://github.com/Robso-creator/discord_bot',
    )
    doc_button = Button(
        label='Documentação',
        url='https://robso-creator.github.io/discord_bot',
    )
    view = View()
    view.add_item(repo_button)
    view.add_item(doc_button)

    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@bot.tree.command(name='apod', guild=server_id, description='foto astronômica do dia!')
async def apod(interaction: discord.Interaction):
    response = requests.get(
        f'https://api.nasa.gov/planetary/apod?api_key={settings.NASA_TOKEN}',
    ).json()
    img_url = response['url']
    img_author = response['copyright']

    translator = Translator(service_urls=['translate.googleapis.com'])
    img_explanation = translator.translate(
        response['explanation'], dest='pt',
    ).text
    img_name = translator.translate(response['title'], dest='pt').text

    translate_append = 'Tradução automática feita utilizando Google Tradutor'

    embed = discord.Embed(
        title=img_name,
        description=f'{img_explanation}\n\n{translate_append}',
        color=discord.Color.dark_magenta(),
    )

    embed.set_thumbnail(
        url='https://gpm.nasa.gov/sites/default/files/NASA-Logo-Large.jpg',
    )  # nasa logo
    embed.set_image(url=img_url)
    embed.set_footer(text=f'Autor(es):{img_author}')

    await interaction.response.send_message(embed=embed)


if __name__ == '__main__':
    bot.run(settings.DISCORD_TOKEN)
