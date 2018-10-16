import datetime

from discord import Embed
from discord.ext import commands
from requests import HTTPError
from riotwatcher import RiotWatcher

import settings
from utils.regions import get_region


class LolCommands:
    watcher = RiotWatcher(settings.RIOT_API_KEY)
    domain = None
    lol_icon = 'https://i.imgur.com/1qe880q.png'

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
                await ctx.send('Error 401 - Unauthorized')
            if error.response.status_code == 403:
                await ctx.send('Error 403 - Forbidden')
            if error.response.status_code == 404:
                await ctx.send('Error 404 - Not Found')
            else:
                pass

    @commands.command(name='summoner',
                      brief='Get details about a summoner from a specific region. Usage: !summoner REGION SUMMONER')
    async def summoner_info(self, ctx, region=None, summoner=None):
        if not region and not summoner:
            await ctx.send('You need to specify a region and a summoner')
        elif not region:
            await ctx.send('You need to specify a region')
        elif not summoner:
            await ctx.send('You need to specify a summoner')
        elif not get_region(region):
            await ctx.send('Region does not exist')
        else:
            try:
                if get_region(region):
                    user = self.watcher.summoner.by_name(region=get_region(region), summoner_name=summoner)
                    leagues = self.watcher.league.positions_by_summoner(get_region(region), user['id'])
                    embed = Embed(title=f'{user["name"]}')
                    embed.set_thumbnail(
                        url=f'http://ddragon.leagueoflegends.com/cdn/8.20.1/img/profileicon/{user["profileIconId"]}.png')
                    for league in leagues:
                        if league['queueType'] == 'RANKED_SOLO_5x5':
                            queue_type = 'Solo/Duo'
                        if league['queueType'] == 'RANKED_FLEX_SR':
                            queue_type = 'Flex'
                    embed.add_field(name='Level', value=f'{user["summonerLevel"]}')
                    embed.set_footer(text='Generated')
                    await ctx.send(embed=embed)
            except HTTPError as error:
                if error.response.status_code == 404:
                    await ctx.send('Summoner not found')


def setup(bot):
    bot.add_cog(LolCommands(bot))
