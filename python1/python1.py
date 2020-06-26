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
    async def dog(self, ctx):
        """Get a Dog fact and a Dog image"""
        
        getfact = await self.bot.session.get('https://some-random-api.ml/facts/dog')
        getimg = await self.bot.session.get('https://some-random-api.ml/img/dog')
        
        facttext = await getfact.text()
        imgtext = await getimg.text()
        
        factjson = json.loads(facttext)
        imgjson = json.loads(imgtext)
        
        embed = discord.Embed(title = "Dog", description = factjson["fact"], color = 0x7289da)
        embed.set_image(url=imgjson["link"])
        await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(MyCog(bot))
