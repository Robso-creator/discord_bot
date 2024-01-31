import os
from logging import DEBUG
from typing import Optional

import discord
from discord.ui import Button
from discord.ui import View

from src import settings
from src.logger import setup_logger

_log = setup_logger('src.main', level=DEBUG)

bot = discord.Bot()
server_id = discord.Object(settings.DISCORD_SERVER_ID)


@bot.event
async def on_ready():
    _log.info('Logged')
    try:
        loaded_commands = []
        for filename in os.listdir('./src/commands'):
            if filename != '__init__.py' and filename.endswith('.py'):
                if filename not in loaded_commands:
                    _log.info(f'loading command {filename[:-3]}')
                    synced = bot.load_extension(
                        f'src.commands.{filename[:-3]}',
                    )
                    loaded_commands.append(filename)
                    _log.debug(f'{len(synced)} commands loaded')

        await bot.sync_commands(guild_ids=[settings.DISCORD_SERVER_ID])

        await bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name='a todos monkeys online',
            ),
        )

    except Exception as e:
        _log.error(e)


@bot.slash_command(name='help', description='teste de descrição')
async def help(
    interaction: discord.Interaction,
    command: Optional[str] = None,
):
    if command is None:
        embed = discord.Embed(
            title='Ajuda com comandos',
            description='Para melhores detalhes sobre comandos, digite: `/help <nome_comando>`',
            color=discord.Color.dark_magenta(),
        )
    else:
        desired_command = next(
            (_command for _command in bot.commands if _command.name == command), None,
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

    button = Button(
        label='Visitar repositório',
        url='https://github.com/Robso-creator/discord_bot',
    )
    view = View()
    view.add_item(button)

    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


if __name__ == '__main__':
    # bot.run(settings.DISCORD_TOKEN)
    async def simulate_on_ready():
        # Simulando um objeto Event para chamar on_ready
        event = discord.Raw(
            data={
                't': 'READY', 'd': {
                    'guilds': [], 'user': {},
                    'session_id': '', 'shard': [0, 1], 'application': {},
                },
            },
        )
        await bot.dispatch('raw_socket_event', event)
