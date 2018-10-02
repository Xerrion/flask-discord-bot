import os

import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix=os.environ.get('COMMAND_PREFIX'))

client = discord.Client()


def run():
    client.run(os.environ.get('BOT_TOKEN'))


@client.event
async def on_ready():
    return print("{} ".format(client.user.name))


for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")
