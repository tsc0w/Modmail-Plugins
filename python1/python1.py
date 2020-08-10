import discord
from discord.ext import commands
from core.checks import has_permissions
from core.models import PermissionLevel

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

    @commands.command()
    @has_permissions(PermissionLevel.OWNER)
    async def talk(self, ctx, *, message):
        await ctx.send(message)
        await ctx.message.delete()

    @commands.command()
    async def menu(self, ctx):
        await ctx.send("**The 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 you can use are here:**                                                                                                   ```.snippets, .addsnippet, .r, .c, .c <time> .ar, .block <userID>, .unblock <userID>, .block, .creator, .ping, .dev .subscribe, .unsubscribe, .purge <amount>, .flickz, .support .edit, .delete, ```                                                                                                       * *all of the 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 are seperated by a comma.*")

    @commands.command()
    async def tester(self, ctx):
        await ctx.send("im testing this out!")
        
    @commands.command()
    async def addsnippet(self, ctx):
        await ctx.send("**To add more Custom Snippet for this 𝚋𝚘𝚝, DM @sandy#1000!**")
   
    @commands.command()
    async def choose(self, ctx):
        await ctx.send("im testing this out!")
        
        
    @commands.command()
    async def flickz(self, ctx):
        await ctx.send("Interested in getting a nice Fun, Moderation Public 𝗯𝗼𝘁 for your own server? Well look no further, Flickz is the one for you!                                                                                        ```To join the official Flickz Support Server, use this link: https://discord.gg/RVcjqug                                                                                        Flickz Invite Link: https://discord.com/oauth2/authorize?client_id=712970263918149632&scope=bot&permissions=8 ``` __Thank You!__    ")
        
    @commands.command()
    async def dev(self, ctx):
        await ctx.send("                                                                                                           Developers: *kyb3r, Taki and FourJr.* Thank you for the help!")
   
def setup(bot):
    bot.add_cog(MyCog(bot))
