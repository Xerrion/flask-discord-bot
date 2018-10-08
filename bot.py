import os
import random

import discord
from discord.ext.commands import Bot

import settings

bot = Bot(command_prefix=settings.COMMAND_PREFIX)


def run():
    bot.run(settings.BOT_TOKEN)


@bot.event
async def on_ready():
    print(f"I am {bot.user.name}")

    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            bot.load_extension(f"cogs.{name}")
