import os
import random
import discord
import datetime

from discord.ext import commands


class FunCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Ask the magic 8ball """
        await ctx.send('sut')

def setup(bot):
    bot.add_cog(FunCommands(bot))
