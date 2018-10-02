import discord
import os
import app

bot = discord.Client()


def run():
    """Run the bot"""
    bot.run(os.environ.get('BOT_SECRET'))


@bot.event
async def on_ready():
    return print('I am {}'.format(bot.user.name))


@bot.event
async def on_message(ctx):
    await ctx.content.message
