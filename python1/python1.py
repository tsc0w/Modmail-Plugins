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
        await ctx.message.delete()

    @commands.command()
    async def menu(self, ctx):
        await ctx.send("**The 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 you can use are here:**                                                                                                   ```.snippets, .r, .c, .c <time> .ar, .block <userID>, .unblock <userID>, .block, .creator, .ping, .dev .subscribe, .unsubscribe, .purge <amount>, .flickz, .support .edit, .delete, ```                                                                                                       * *all of the 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 are seperated by a comma.*")

    @commands.command()
    async def tester(self, ctx):
        await ctx.send("im testing this out!")
   
    @commands.command()
    async def choose(self, ctx):
        await ctx.send("im testing this out!")
        
    @commands.command()
    async def support(self, ctx):
        await ctx.send("Need support with this 𝗯𝗼𝘁? Join The Support Server, we will be happy to help! Server Link: https://discord.gg/RVcjqug ")
        
    @commands.command()
    async def flickz(self, ctx):
        await ctx.send("Interested in getting a nice Fun, Moderation Public 𝗯𝗼𝘁 for your own server? Well look no further, Flickz is the one for you!                                                                                        ```To join the official Flickz Support Server, use this link: https://discord.gg/RVcjqug                                                                                        Flickz Invite Link: https://discord.com/oauth2/authorize?client_id=712970263918149632&scope=bot&permissions=8 ``` __Thank You!__    ")
        
    @commands.command()
    async def dev(self, ctx):
        await ctx.send("Main Developer: **@sandy#1000**,                                                                                                            Helpers: *kyb3r, Taki and FourJr.* Thank you for the help!")
   
    @commands.command()
    async def creator(self, ctx):
        await ctx.send("**Looking for the maker of this 𝗯𝗼𝘁?**                                                                                            ```If so, the maker is @sandy#1000, if you want a Custom 𝗯𝗼𝘁 like this, DM him!```")
        
def setup(bot):
    bot.add_cog(MyCog(bot))
