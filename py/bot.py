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
client = commands.Bot(command_prefix = "!", intents = discord.Intents.default(), help_command=None)


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
        #below command is needed because on_message overrides all commands and stops them from running see 4.4.22 readme for info
    await client.process_commands(message)




#* added to help command
#ping ms command
@client.command(help='pings bot; shows latency')
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency * 1000)}ms')

#list command
# TODO once commands are added add to list
# * added embed status     
@client.command(help='lists all available commands')
async def list(ctx):
    embed=discord.Embed(title="Command List", color=0x00ccff)
    embed.add_field(name="ping", value="Pings bot; shows latency", inline=False)
    embed.add_field(name="list", value="Lists available commands", inline=False)
    embed.add_field(name="dm_list", value="DMs user list of commands (helps keep channels clear)", inline=False)
    await ctx.send(embed=embed)


#! not working ignore
@client.command(help='dms command list')
async def dm_list(ctx):
    user = client.get_user()
    await ctx.send('Command list:\n Ping: pings bot with latency \n dm_list: dms list (funny, your using that command right now) \n ')

#onjoin mention in joins channel and dm welcome
#! doesnt curretnly work
@client.event
async def on_member_join(message):
    user = client.get_user()
    channel = client.get_channel(960580449254649996)
    await message.send('{member} has joined the server!')
    await user.send('welcome to the server')


#help command
class CustomHelpCommand(commands.HelpCommand):

    def __init__(self):
        super().__init__()

    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command))
        embed.add_field(name="Help", value=command.help)
        await self.get_destination().send(command.name)
#closes the class (i think)        
client.help_command = CustomHelpCommand()

#command not found error message
# TODO add if client.user




#set status
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('being useless'))




client.run(token)
