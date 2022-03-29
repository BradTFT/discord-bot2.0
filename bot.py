#run bot with this syntax
# python3 bot.py

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTU3Njg4OTQyMDU0OTk4MDQ4.YkCbVA.lEweRlEyNq2APbaLmvDhAs3Vhq8')
