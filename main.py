import random

import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('message from {0.author}: {0.content}'.format(message))
        if message.content == ('!roleta'):
            await message.channel.send(f'O sorteado foi: {self.users.copy()[random.randint(0, len(message.guild.members)- 1)]}')


client = MyClient(intents=intents)
client.run('')
