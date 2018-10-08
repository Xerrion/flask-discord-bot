import datetime

from discord import Embed
from discord.ext import commands
from requests import HTTPError
from riotwatcher import RiotWatcher
from pprint import pprint

import settings


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
            if region is None:
                return await ctx.send('Region is missing. E.g !lolstatus NA')
            else:
                for self.region, domain in self.regions.items():
                    if region == self.region:
                        self.domain = domain['domain']
                        break
                    else:
                        self.domain = None
                if self.domain:
                    shard = self.watcher.lol_status.shard_data(self.domain)
                    pprint(shard)
                    embed = Embed(title=shard['name'], timestamp=datetime.datetime.now())
                    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                    for service in shard['services']:
                        embed.add_field(name=service['name'].upper(), value=service['status'].capitalize(), inline=True)
                    # embed.add_field(name=)
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


def setup(bot):
    bot.add_cog(LolCommands(bot))
