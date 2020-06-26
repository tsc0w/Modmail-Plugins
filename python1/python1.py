import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()
client.remove_command('help')
 
@client.command()
async def suggest(ctx):
  e = discord.Embed(title="Suggestions for a Flickz Bot Command?", description="If you have a suggestion, please DM me it and i will be able to check it asap! ", color=0xf542f2)
  e.add_field(name="*Flickz V1.85*", value="**DM ME FOR ANY COMMAND SUGGESTIONS!**")
  await ctx.send(embed=e)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount + 1)

@client.command()
async def delete_things(ctx):
    confirm = await Confirm('Delete everything?').prompt(ctx)
    if confirm:
        await ctx.send('deleted...')

@client.command()
async def avatar(ctx, member: discord.Member=None):  
    if not member:
        member = ctx.message.author
    show_avatar = discord.Embed(description="[Avatar URL](%s)" % member.avatar_url)
    show_avatar.set_image(url="{}".format(member.avatar_url))
    show_avatar.set_footer(text=f'{member}')
    await ctx.send(embed=show_avatar)

@client.command()
async def av(ctx, member: discord.Member=None):  
    if not member:
        member = ctx.message.author
    show_avatar = discord.Embed(description="[Avatar URL](%s)" % member.avatar_url)
    show_avatar.set_image(url="{}".format(member.avatar_url))
    show_avatar.set_footer(text=f'{member}')
    await ctx.send(embed=show_avatar)
    
@client.command()
async def helpembed(ctx):
  e = discord.Embed(title="**Commands For Flickz:**", description=".ping, .version, .flickzbot, **.vote**, .pingme, .avatar, .avatar {user@}, .suggest, **.pro**, .dmhelp, .gm, .hi, .vibe, .bark, .botpage, .welcome, .mee6, .default, .takethel, .invite, .welcomegif, .welcomegif2, .discord, .support, .bug, .donate, .omg, .clown, .sandy, .maker, .skate, .babyyoda, .gg, .freenitro, .nitrogift, .membercount,", color=0xf542f2)
  e.add_field(name="**Flickz V1.85**", value="*Flickz is updated every week, so expect new commands coming soon!*")
  await ctx.send(embed=e)

@client.command()
async def dmhhelp(ctx):
  e = discord.Embed(title="**DM Sent with help to your inbox**", description="Check your inbox for help!", color=0xf542f2)
  e.add_field(name="**Flickz V1.85**", value="*For more Flickz Command info, visit the Flickz Docs @: [FlickzDocs](https://flickz-docs.com)*")
  await ctx.send(embed=e)

@client.command()
async def pro(ctx):
  e = discord.Embed(title="**FlickzPro**", description="FlickzPro. To support development of Flickz, we offer some features exclusively for premium members. But don't worry, the features you can use now will always be free! We will use the money we earn exclusively to pay for servers and fund development. When buying FlickzPro, you will gain a handful of new features, which will be coming very soon!", color=0xf542f2)
  e.add_field(name="**Thinking of buying Flickz Pro?**", value="*to buy FlickzPro, [Click here](https://bit.ly/flickzpro). Thank you for supporting Flickz.*")
  await ctx.send(embed=e)

@client.command()
async def botcount(ctx):
    embed=discord.Embed(description=f"FlickzTester is currently operating in `{len(client.guilds)}` servers!")
    await ctx.send(embed=embed)

@client.command(aliases=['info','user'])
async def userinfo(ctx, member : discord.Member=None):
    if member is None:
      roles = [role for role in ctx.author.roles]
 
      embed = discord.Embed(title="User info", colour=ctx.author.color, timestamp=ctx.message.created_at)
 
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
      embed.set_footer(text="Requested by: {}".format(ctx.author), icon_url=ctx.author.avatar_url)
     
 
      embed.add_field(name="Joined Discord at", value=ctx.author.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
      embed.add_field(name="Member since", value=ctx.author.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
      embed.add_field(name="Server", value=ctx.author.guild)
      embed.add_field(name="Status", value=ctx.author.status)
      embed.add_field(name=f'Roles ({len(roles)})', value=''.join([role.mention for role in roles]))
      embed.add_field(name="Highest Role", value=ctx.author.top_role)
     
      await ctx.send(embed=embed)
    else:
        roles = [role for role in member.roles]
 
        embed = discord.Embed(title="User info", colour=member.color, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=member.display_name, icon_url=member.avatar_url)
        embed.set_footer(text="Requested by: {}".format(ctx.author), icon_url=ctx.author.avatar_url)
       
 
        embed.add_field(name="Joined Discord at", value=member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
        embed.add_field(name="Member since", value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
        embed.add_field(name="Server", value=member.guild)
        embed.add_field(name="Status", value=member.status)
        embed.add_field(name=f'Roles ({len(roles)})', value=''.join([role.mention for role in roles]))
        embed.add_field(name="Highest Role", value=member.top_role)
       
        await ctx.send(embed=embed)

@client.command(aliases=['server'])
async def serverinfo(ctx):
    embed=discord.Embed(title='__Server Info__', colour=0xf542f2)
    embed.add_field(name="**Server Icon:**", value=ctx.guild.icon_url)
    embed.add_field(name="**Server Name:**", value=ctx.guild.name)
    embed.add_field(name="**Server Created:**", value=ctx.guild.created_at)
    embed.add_field(name="Members:", value=f'Do `.membercount` to see the amount of members in **{ctx.guild.name}**')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
	await ctx.send(f'**PONG!** `Latency = {round(client.latency * 1000)}ms`')
 
@client.command()
async def dmhelp(ctx):
  await ctx.author.send('The Commands that **Flickz** currently has are: .ping, .version, .flickzbot, **.vote**, .pingme, .avatar, .avatar {user@}, .texthelp .suggest, .dmhelp, .gm, .hi, .vibe, .bark, .botpage, .welcome, .mee6, .default, .takethel, .invite, .welcomegif, .welcomegif2, .discord, .support, .bug, .donate, .omg, .clown, .sandy, .maker, .skate, .babyyoda, .gg, .freenitro, .nitrogift, .membercount,                                                                                                                                      **For more commands visit Flickz Docs @: https://bit.ly/flickzdocs')

@client.command()
async def servername(ctx):
  await ctx.send (f'You are currently in: `{ctx.guild.name}`')

@client.command()
@commands.has_permissions(administrator = True)
async def say(ctx, *,repeat):
  await ctx.message.delete()
  await ctx.send(repeat)

@client.command()
async def membercount(ctx):
  await ctx.send(len(ctx.guild.members))

def setup(bot):
	bot.add_cog(MyCog(bot))
