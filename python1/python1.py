import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

    @commands.command()
    async def echo(self, ctx, *, message):
        await ctx.send(message)

    @commands.command()
    async def choose(self, ctx):
        await ctx.send("Not enough options to pick from.")

    @commands.command()
    async def tester(self, ctx):
        await ctx.send("im testing this out!")
        
def setup(bot):
    bot.add_cog(MyCog(bot))
