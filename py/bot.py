#run bot with this syntax
# python3 bot.py
#run venv: source .venv/bin/activate
#create venv if ^^^ doesnt work: python3.9 -m venv .venv

#loads dotenv and os (dependant on each other)
from dotenv import load_dotenv
from os import getenv
#runs dotenv
load_dotenv()
#import discord lib
import discord
#imports commands from discord
from discord.ext import commands
#gets token from .env using dotenv
token = getenv("token")
#sets client as connected to discord
client = discord.Client()

#sets prefix and loads intents
client = commands.Bot(command_prefix = "!", intents = discord.Intents.default())


#on ready message log in terminal
@client.event
async def on_ready():
    print('bot online')    


#hello command which btw is the only one that works rn
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

#ping ms command
@client.command()
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency * 1000)}ms')



#set status
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('being useless'))



client.run(token)
