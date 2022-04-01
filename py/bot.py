#run bot with this syntax
# python3 bot.py
#run venv: source .venv/bin/activate
#create venv if ^^^ doesnt work: python3.9 -m venv .venv


from dotenv import load_dotenv
from os import getenv
load_dotenv()
import discord
from discord.ext import commands
token = getenv("token")

client = discord.Client()

#sets prefix
client = commands.Bot(command_prefix = "!")


#on ready message log in terminal
@client.event
async def on_ready():
    client.message('i am online')

#hello command which btw is the only one that works rn
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')



#i made this so it sucks. dm command that doesnt work
@client.event 
async def dm(message, ctx):
    if message.author == client.user:
        return
    
    if message.content.startswith('!dm'):
        me = await client.get_user_info('')
        await client.send_message(me, ctx)


#pasted command for ping that doesnt work
@client.command
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


#trying to make an "on join dm" message. havent tested yet imma ask someone 
@client.event
async def on_member_join(member):
    await member.send('welcome to the server')



#set status
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('being useless'))



client.run(token)
