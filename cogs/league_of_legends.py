import datetime

from discord import Embed
from discord.ext import commands
from requests import HTTPError
from riotwatcher import RiotWatcher
from pprint import pprint

import settings
from utils.regions import get_region


class LolCommands:
    regions = {
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
    watcher = RiotWatcher(settings.RIOT_API_KEY)
    domain = None

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lolstatus',
                      description="Get an overview of lol status",
                      brief="Displays server status from Riots servers",
                      aliases=['lol_status', 'lolonline', 'islolup', 'lolstat'],
                      pass_context=True)
    async def server_status(self, ctx, region=None):
        try:
            if get_region(region):
                shard = self.watcher.lol_status.shard_data(get_region(region))
                embed = Embed(title=shard['name'], timestamp=datetime.datetime.now())
                embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                for service in shard['services']:
                    embed.add_field(name=service['name'].upper(), value=service['status'].capitalize(), inline=True)
                embed.set_footer(text='Generated')
                await ctx.send(embed=embed)
            else:
                await ctx.send('Region Not Found')
        except HTTPError as error:
            if error.response.status_code == 401:
                pass
            if error.response.status_code == 404:
                await ctx.send('not found')
            else:
                pass

    @commands.command(name='summoner',
                      brief='Get details about a summoner from a specific region. Usage: !summoner REGION SUMMONER')
    async def summoner_info(self, ctx, region, summoner):
        try:
            if get_region(region):
                user = self.watcher.summoner.by_name(region=get_region(region), summoner_name=summoner)
                league = self.watcher.league.positions_by_summoner(get_region(region), user['id'])
                if league[0]['queueType'] == 'RANKED_SOLO_5x5':
                    queue_type = 'Solo/Duo'
                embed = Embed(title=f'{queue_type}')
                embed.set_thumbnail(url=
                                    'http://www.macupdate.com/images/icons256/47210.png')
                embed.add_field(name='Test', value='Tester')
                embed.set_footer(text='Generated')
                await ctx.send(embed=embed)
        except HTTPError as error:
            if error.response.status_code == 404:
                await ctx.send('Summoner not found')


def setup(bot):
    bot.add_cog(LolCommands(bot))
