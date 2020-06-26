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
    async def commands(self, ctx):
        await ctx.send("**The commands you can use are here:**                                                                                                   .snippets, .r, .c, .ar, .block <userID>, .unblock <userID>, .creator, .ping, .subscribe, .unsubscribe")

    @commands.command()
    async def tester(self, ctx):
        await ctx.send("im testing this out!")
   
    @commands.command()
    async def choose(self, ctx):
        await ctx.send("im testing this out!")
   
    @commands.command()
    async def creator(self, ctx):
        await ctx.send("Looking for the maker of this bot?                                                                                            If so, the maker is @sandy#1000, if you want a Custom bot like this, DM him!")
        
def setup(bot):
    bot.add_cog(MyCog(bot))
