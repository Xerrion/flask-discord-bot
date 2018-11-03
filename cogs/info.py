from discord import Embed
from discord.ext import commands
import psutil as ps
from utils.default import bytes2human


class InformationCommands:
    mem = ps.virtual_memory()

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info',
                      description="Get info about the bot",
                      brief="Get info about the bot, includes a download link.",
                      aliases=['botinfo', 'bot'],
                      pass_context=True)
    async def bot_information(self, context):
        embed = Embed(title='Bot Information')
        embed.add_field(name='CPU Usage',
                        value=f'Currently using: {ps.cpu_percent()}%',
                        inline=True)
        embed.add_field(name='RAM Usage',
                        value=f'Available: {bytes2human(self.mem.available)}\n'
                              f'Used: {bytes2human(self.mem.used)} \/ {self.mem.percent}%\n'
                              f'Total: {bytes2human(self.mem.total)}',
                        inline=True)
        for disk in ps.disk_partitions():
            usage = ps.disk_usage(disk.mountpoint)
            embed.add_field(name='Disk Volume', value=f'{disk.device}',
                            inline=False)
            embed.add_field(name='Disk Space Total',
                            value=f'{bytes2human(usage.total)}', inline=True)
            embed.add_field(name='Disk Space Free',
                            value=f'{bytes2human(usage.free)}', inline=True)
            embed.add_field(name='Disk Space Used',
                            value=f'{bytes2human(usage.used)}', inline=True)

        # embed.add_field(name='3', value='3', inline=True)
        # embed.add_field(name='4', value='4', inline=True)
        # embed.add_field(name='5', value='5', inline=True)
        # embed.add_field(name='6', value='6', inline=True)
        # embed.add_field(name='7', value='7', inline=True)
        # embed.add_field(name='8', value='8', inline=True)
        # embed.add_field(name='9', value='9', inline=True)
        # embed.add_field(name='10', value='10', inline=False)
        # embed.add_field(name='11', value='11', inline=False)
        await context.send(embed=embed)


def setup(bot):
    bot.add_cog(InformationCommands(bot))
