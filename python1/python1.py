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
    async def suggest(self, ctx):
    e = discord.Embed(title="Suggestions for a Flickz Bot Command?", description="If you have a suggestion, please DM me it and i will be able to check it asap! ", color=0xf542f2)
    e.add_field(name="*Flickz V1.85*", value="**DM ME FOR ANY COMMAND SUGGESTIONS!**")
    await ctx.send(embed=e)
        
def setup(bot):
    bot.add_cog(MyCog(bot))
