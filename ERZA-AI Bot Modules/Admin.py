import discord
from discord.http import json_or_text
from discord.ext.commands.core import has_guild_permissions
from discord.ext import commands
from discord.utils import get
client = commands.Bot(command_prefix=".",intents=discord.Intents.all())
@client.event
async def on_ready():
    print('Logged in ')
@client.command(pass_content=True)    
async def slowmode(message,seconds: int):
 member=message.author.id
 member2=message.author
 if member==504564888576983050:
  await message.channel.edit(slowmode_delay=seconds)
  await message.channel.send(":stuck_out_tongue_winking_eye:")
 else:
  await message.channel.send(f'{member2.mention}Not authorized')  
@client.command(pass_content=True)     
async def changenick(message,member: discord.Member, nick):
    member1=message.author.id
    member2=message.author
    if member1==504564888576983050:
     await member.edit(nick=nick)
     await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')   
@client.command(pass_content=True)     
async def createchannel(message,channelname, cat= 5):
    guild=message.guild
    member=message.author.id
    member2=message.author
    category=discord.utils.get(guild.categories,id=cat)
    if member==504564888576983050:
     await guild.create_text_channel(name='{}'.format(channelname),category=category) 
     await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized') 
@client.command(pass_content=True)     
async def deletechannel(message):
    guild=message.guild
    member=message.author.id
    if member==504564888576983050:
     await message.channel.delete()
         
@client.command(pass_content=True)    
async def purge(message,amount=5):
 member=message.author.id
 member2=message.author
 if member==504564888576983050:
  await message.channel.purge(limit=amount)
  await message.channel.send(":stuck_out_tongue_winking_eye:")
 else:
  await message.channel.send(f'{member2.mention}Not authorized')
@client.command(pass_content=True)     
async def move(message,member: discord.Member, channel: discord.VoiceChannel):
    
    member1=message.author.id
    member2=message.author
    
    if member1==504564888576983050:
     await member.move_to(channel)
     await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')   
@client.command(pass_content=True)     
async def disconnect(message,member: discord.Member, channel=None):
    
    member1=message.author.id
    member2=message.author
    
    if member1==504564888576983050:
     await member.move_to(channel)
     await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')  
@client.command(pass_content=True)     
async def kick(message,member: discord.Member, reason):
    member1=message.author.id
    member2=message.author
    if member1==504564888576983050:
     await member.kick(reason=reason)
     await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')  
@client.command(pass_content=True)     
async def ban(message,member: discord.Member, reason):
    member1=message.author.id
    member2=message.author
    if member1==504564888576983050:
     await member.ban(reason=reason)
     await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')                
@client.command(pass_content=True)     
async def unban(message,user: discord.User):
    guild=message.guild
    member1=message.author.id
    member2=message.author
    if member1==504564888576983050:
     await guild.unba(user=user)
     await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')  
@client.command(pass_content=True)     
async def mute(message,member: discord.Member):
    guild=message.guild
    role=discord.utils.get(message.guild.roles, name="Muted")
    member1=message.author.id
    member2=message.author
    if member1==504564888576983050:
      if role not in guild.roles:
        perms=discord.Permissions(send_message=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await message.channel.send(f"{member} was muted.")
        await message.channel.send(":stuck_out_tongue_winking_eye:")
      else:
        await member.add_roles(role)
        await message.send(f"{member} was muted.")
        await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')    
@client.command(pass_content=True)     
async def unmute(message,member: discord.Member):
    
    role=discord.utils.get(message.guild.roles, name="Muted")
    member1=message.author.id
    member2=message.author
    if member1==504564888576983050:
      await member.remove_roles(role)
      await message.channel.send(f"{member} was unmuted.")
      await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')
@client.command(pass_content=True)     
async def servermute(message,member: discord.Member):
    member1=message.author.id
    member2=message.author
    if member1==504564888576983050:
      await member.edit(mute = True)
      await message.channel.send(f"{member} was servermuted.")
      await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')
@client.command(pass_content=True)     
async def serverunmute(message,member: discord.Member):
    member1=message.author.id
    member2=message.author
    if member1==504564888576983050:
      await member.edit(mute = False)
      await message.channel.send(f"{member} was servermuted.")
      await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')
@client.command(pass_content=True)     
async def serverdeafen(message,member: discord.Member):
    member1=message.author.id
    member2=message.author
    if member1==504564888576983050:
      await member.edit(deafen = True)
      await message.channel.send(f"{member} was server deafened.")
      await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized') 
@client.command(pass_content=True)     
async def serverundeafen(message,member: discord.Member):
    member1=message.author.id
    member2=message.author
    if member1==504564888576983050:
      await member.edit(deafen = False)
      await message.channel.send(f"{member} was server undeafened.")
      await message.channel.send(":stuck_out_tongue_winking_eye:")
    else:
     await message.channel.send(f'{member2.mention}Not authorized')                                     
client.run('Enter your token here')
