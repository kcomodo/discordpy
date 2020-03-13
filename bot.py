import discord
import random
import os
import json
import youtube_dl
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
''''
def get_prefix(client,message):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix = get_prefix)
'''
#Use.command to command bot
client = commands.Bot(command_prefix='.')
players = {}
#status = (['Status 1','Status 2'])
#When running, the bot will notify that it will run
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('your mom'))
    #change_status.start()
    print("Bot is ready")
'''
#Check if member has permission or is rank high enough for a command
@commands.has_permissions(manage_messages=True)
#If user type in the wrong commands, inform them
@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('This command doesnt exist dumbass')
'''
'''
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
'''
'''
@client.event
#When a member joins, the bot will notify the admin
async def on_member_join(member):
    print('f{member} has joined a server.')
@client.event
#When a member leaves, the bot will notify the admin
async def on_member_remove(member):
    print('f{member} has left a server')
@client.command()
#Using .ping will ask the bot for the ping
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')
'''

'''
Import random and import a list for the bot
User can ask a question using the .question1 command
The bot will answer the question using a random answer
'''
'''
@client.command(aliases = ['8ball', 'test'])
async def ask_about_aqua(ctx,*, question):
    responses = ['maybe','yes', 'she most definitely is']
    await ctx.send(f'{random.choice(responses)}')
#Using the .clear command, this will clear out all previous messages in the server
#if user does not meet the requirement, inform them
@client.command()
#async def clear (ctx, amount=5):
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount )
#Only trigger if the clear command triggers an error
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete')
#Using the kick command will allow the admin to kick any users
@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
#Using the ban command will allow the admin to kick any users
@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'Banned{member.mention}')
#Use .unban to unban a member
@client.command()
async def unban(ctx, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discrimination = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator) == (member_name):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return
#Use command to find file as a "extension"
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
#Default value for all server to start with
@client.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '.'
    with open('prefixes.json','w') as f:
        json.dump(prefixes.f, indent=4)
@client.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open('prefixes.json','w') as f:
        json.dump(prefixes.f, indent=4)
@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes [str(ctx.guild.id)] = prefix
    with open('prefixes.json','w') as f:
        json.dump(prefixes, f, indent =4)
    await ctx.send(f'Prefix changed to: {prefix}')
def is_it_me(ctx):
    return ctx.author.id == 326406236746547201
@client.command()
@commands.check(is_it_me)
async def check_name(ctx):
    await ctx.send(f'Hi Im {ctx.author}')
'''

'''
#Connect command
@client.command(pass_context = True)
async def connect(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
#Disconnect command
@client.command(pass_context = True)
async def disconnect(ctx):
    server = ctx.message.guild
    voice_client = client.voice_clients_iN(server)
    await voice_client.disconnect()
#Play commands
'''
'''
@client.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
@client.command(pass_context = True)
@client.command(pass_context=True)
async def disconnect(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.disconnect()
@client.command(pass_context = True)
'''
@client.command()
async def join(ctx):
 if ctx.author.voice and ctx.author.voice.channel:
  channel = ctx.author.voice.channel
 else:
  await ctx.send("You are not connected to a voice channel")
  return
 global vc
 try:
  vc=await channel.connect()
 except:
  TimeoutError
@client.command()
async def leave(ctx):
 try:
  if vc.is_connected():
   await vc.disconnect()
 except:
  TimeoutError
  pass
@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return
    await ctx.send("Getting everything ready now")
    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07
    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")
client.run('Njg0NTAyODY4OTc1MTU3Mjc1.Xmeuzg.dmTbZpxMIyyVkXFyOBc2zFl8ibA')