#run bot with this syntax
# python3 bot.py
#or use code runner ext command (ctrl, alt, n)

#run venv (virtual environment): source .venv/bin/activate

#token hiding libraries
import os
from dotenv import load_dotenv

#import libraries
from discord.ext import commands
import discord




client = discord.Client()

#sets prefix
bot = commands.Bot(command_prefix = "!")

#shows bot online
@client.event
async def on_ready():
    print('bot online')

#makes bot status
@client.event
async def on_ready():
    await bot.change_presence(activity = discord.Game('being useless'))


@client.command()
async def ping():
    await client.say('Pong!')




#bot token must be last line 
client.run('token')
