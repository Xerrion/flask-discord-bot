import datetime
import json
import os

import discord
from discord.ext import commands
import requests


class LolCommands:
    servers = {
        'ru': 'ru',
        'kr': 'kr',
        'br': 'br1',
        'oca': 'oc1',
        'jp': 'jp1',
        'na': 'na1',
        'euw': 'euw1',
        'eune': 'eun1',
        'tr': 'tr1',
        'la1': 'la1',
        'la2': 'la2'
    }
    response = None

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lolstatus',
                      description="Get an overview of lol status",
                      brief="Displays server status from Riots servers",
                      aliases=['lol_status', 'lolonline'],
                      pass_context=True)
    async def server_status(self, ctx, server=None):
        if not server:
            return await ctx.send('You need to specify a server')
        for server, domain in self.servers.items():
            if server == f'{server}':
                self.response = requests.get(
                    f"https://{domain}.api.riotgames.com/lol/status/v3/shard-data?api_key={os.environ.get('LOL_API_KEY')}")
            else:
                return await ctx.send('You need to specify a server')
        data = self.response.json()
        embed = discord.Embed(title=str(f'{data["name"]}'))
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        for d in data['services']:
            embed.add_field(name=str(f'{d["name"]}'), value=f'{d["status"].capitalize()}', inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(LolCommands(bot))
