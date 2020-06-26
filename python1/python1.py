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
    async def maker(self, ctx):
        e = discord.Embed(title="Looking for the maker of this bot?", description="The maker of this bot is <@514465594175651841>, if you want a custom bot also , DM him! ", color=0xf5427b)       
        await ctx.send(embed=e)
        
def setup(bot):
    bot.add_cog(MyCog(bot))
