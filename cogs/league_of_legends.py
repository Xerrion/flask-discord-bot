import os

import discord
import requests
from cassiopeia import Summoner
from discord import Embed
from discord.ext import commands
import cassiopeia as lol


class LolCommands:
    servers = {
        'ru': {'domain': 'ru'},
        'kr': {'domain': 'kr'},
        'br': {'domain': 'br1'},
        'oca': {'domain': 'oc1'},
        'jp': {'domain': 'jp1'},
        'na': {'domain': 'na1'},
        'euw': {'domain': 'euw1'},
        'eune': {'domain': 'eun1'},
        'tr': {'domain': 'tr1'},
        'la1': {'domain': 'la1'},
        'la2': {'domain': 'la2'},
    }
    response = None
    lol.set_riot_api_key(os.environ.get('RIOT_API_KEY'))

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lolstatus',
                      description="Get an overview of lol status",
                      brief="Displays server status from Riots servers",
                      aliases=['lol_status', 'lolonline', 'islolup', 'lolstat'],
                      pass_context=True)
    async def server_status(self, ctx, server=None):
        for s, d in self.servers.items():
            if not server:
                return await ctx.send('You need to specify a server. eg. !lolstatus na')
            if s == server:
                self.response = requests.get(
                    f"https://{d['domain']}.api.riotgames.com/lol/status/v3/shard-data?api_key={os.environ.get('RIOT_API_KEY')}")
                break
            else:
                pass
        if self.response.status_code == 200:
            data = self.response.json()
            embed = Embed(title=str(f'{data["name"]}'))
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            for d in data['services']:
                embed.add_field(name=str(f'{d["name"]}'), value=f'{d["status"].capitalize()}', inline=True)
            return await ctx.send(embed=embed)
        elif self.response.status_code != 200:
            return print(f'It\'s properly the API Token - Status code: {self.response.status_code}')
        else:
            return await ctx.send('There was an error contacting Riot Developer API')

    @commands.command(name='summoner',
                      description='Get stats of a summoner',
                      brief='Get status of a summoner',
                      aliases=['summ', 'sum', 'lolsummoner'],
                      pass_context=True)
    async def get_summoner(self, ctx, server=None, summoner=None):
        if server is not None or summoner is not None:
            summoner = Summoner(name=summoner, region=server)
            league = Leagues
            embed = Embed(title=summoner.name)
            embed.add_field(name='Flex Rank', value=league.League('tier'))
            await ctx.send(embed=embed)
        elif server is None:
            await ctx.send('You must specify a region. E.g. !summoner EUNE Xerrion')
        elif summoner is None:
            await ctx.send('You must specify a summoner. E.g. !summoner EUNE Xerrion')


def setup(bot):
    bot.add_cog(LolCommands(bot))
