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

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == '.help':
            await message.channel.send("pong")
        await client.process_commands(message)

 @commands.command()
    async def choose(self, ctx):
            await ctx.send(_("Not enough options to pick from."))
        
def setup(bot):
    bot.add_cog(MyCog(bot))
