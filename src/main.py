import random

import discord

from src.logger import setup_logger

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

_log = setup_logger('src.main')


class MyClient(discord.Client):
    async def on_ready(self):
        _log.info(f'Logged on as {self.user}!')

    async def on_message(self, message):
        _log.info('message from {0.author}: {0.content}'.format(message))
        if message.content == '!roleta':
            await message.channel.send(
                f'O sorteado foi: {self.users.copy()[random.randint(0, len(message.guild.members) - 1)]}',
            )


if __name__ == '__main__':
    import settings

    client = MyClient(intents=intents)
    client.run(settings.DISCORD_TOKEN)
