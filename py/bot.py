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
embedcolor = 0x00d5ff
import time
import random




#!start code


#on ready message log in terminal
@client.event
async def on_ready():
    print('bot online')  
    await client.change_presence(activity = discord.Game('!h for help')) 



#hello command
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




#onjoin mention in joins channel and dm welcome
#! doesnt curretnly work
@client.event
async def on_member_join(member):
    await member.send("Welcome!")




#!admin commands (kick ban ect)
#ban command
@client.command()
@commands.has_role('Admin')
async def ban(ctx, user: discord.Member, *, reason = None):
    await user.ban()
    ctx.send(f'{user} was banned for {reason}')


#kick command
@client.command()
@commands.has_role('Admin')
async def kick(ctx, user: discord.Member, *, reason = None):
    await user.kick()
    ctx.send(f'{user} has been kicked for {reason}')




#unban command
@client.command()
@commands.has_role('Unban')
async def unban(ctx, *, member_id: int):
    await ctx.guild.unban(discord.Object(id=member_id))


#admin function list
@client.command()
@commands.has_role('Admin')
async def admincmd(ctx):
    embed=discord.Embed(title="Admin Commands", description="***DO NOT LEAK***", color=embedcolor)
    embed.add_field(name="!ban", value="bans user (!ban username#1111)", inline=False)
    embed.add_field(name="!unban", value="special permissions needed for this command (!unban userid)", inline=True)
    embed.add_field(name="!kick", value="kicks user (!kick username#1111)", inline=False)
    await ctx.author.send(embed=embed)

        
# TODO: FIX COMMAND
@client.command()
@commands.has_role('Admin')
async def timeout(ctx, member):
    await member.timeout()



#! end admin commands


#! fun commands
#TODO add fun commands


#dice roll 6 sided
@client.command()
async def roll6(ctx):
    numbers6 = ['1', '2', '3', '4', '5', '6']
    await ctx.send(random.choice(numbers6))

#dice roll 38
@client.command()
async def roll38(ctx):
    await ctx.send(random.randrange(1, 38))


#coin toss
@client.command()
async def coinflip(ctx):
    sides = ['Heads', 'Tails']
    await ctx.send(random.choice(sides))

#creator command
@client.command()
async def creator(ctx):
    myid = 612985717609725972
    await ctx.send(f'my creator is <@{myid}>, he created me with great power')
    time.sleep(1)
    await ctx.send('please dont ping him constantly it will make him upset')

#owner command:
@client.command()
async def serverowner(ctx):
    id = 612985717609725972
    await ctx.send(f'<@{id}> is the server owner')
    time.sleep(1)
    await ctx.send('please dont ping him constantly it will make him upset')


#! end of fun commands

#! meme commands ignore:::
#demorolizor 2.0
import random
@client.command()
async def humble(ctx, *, args):
    list1 = ['shut up no one asked', 'imagine being better then everyone', 'cool, dont care', 'idgaf', 'wow interesting']
    if args == 'brag':
            await ctx.send(random.choice(list1))
    else:
        await ctx.send('try another term')


#help (no)
@client.command()
async def helppls(ctx):
    embed=discord.Embed(title="No", description="Figure it out  yourself", color=0x00d5ff)
    embed.set_footer(text="or leave that works too")
    await ctx.send(embed=embed)


#whois command
@client.command()
async def whois(ctx, *, args):
    await ctx.send('their a bitch and they get no bitches')



#! end of meme commands

#command not found error message
@client.event
async def on_command_error(ctx, error):
    if ctx.author == client.user:
        return

    if isinstance(error, commands.CommandNotFound): 
        embed=discord.Embed(color=0x00d5ff)
        embed.add_field(name="Error", value="Unknown Command", inline=False)
        await ctx.send(embed=embed)


#!convert c to f here
@client.command()
async def convertc(ctx, *, arg):
    #take arg temperature and convert it
    output = int(arg) * 2 + 30
    await ctx.send(f"The temperature in Fahrenheit is {output} degrees")
    time.sleep(1)
    await ctx.send('by the way this is not entirely accurate because of the use of the simplistic formula')


#better help command
@client.command()
async def h(ctx, *, arg=None):
    if arg == 'admin':
        embed=discord.Embed(title="Admin Commands Request", description="run !admincmd for admin commands", color=embedcolor)
        await ctx.author.send(embed=embed)
    elif arg == 'weather':
        embed=discord.Embed(title="Weather Help", description="Run: !weather", color=embedcolor)
        embed.add_field(name="city not found:", value="check spelling", inline=False)
        embed.add_field(name="wrong city:", value="add a comma and the state abbreviation after the city", inline=True)
        embed.add_field(name="wrong temp unit:", value="run !convertc temperature", inline=False)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Basic Commands", color=embedcolor)
        embed.add_field(name="!ping", value="returns bot latency", inline=False)
        embed.add_field(name="!hello", value="bot says hello back", inline=True)
        embed.add_field(name="!dice6", value="rolls a 6 sided die", inline=False)
        embed.add_field(name="!dice38 ", value="rolls a 38 sided die", inline=False)
        embed.add_field(name="!coinflip", value="flips a coin", inline=True)
        await ctx.send(embed=embed)






#last line (token using dotenv)
client.run(token)
