import random

from discord.ext import commands

from app import Answers


class FunCommands:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball',
                      description="Answers a yes/no question.",
                      brief="Answers from the beyond.",
                      aliases=['eight_ball', 'eightball', '8-ball'],
                      pass_context=True)
    async def eight_ball(self, context):
        a = Answers.query.all()
        possible_responses = random.choice(a)
        await context.send(f"{possible_responses}, {context.message.author.mention}")


def setup(bot):
    bot.add_cog(FunCommands(bot))
