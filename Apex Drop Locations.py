#bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord Server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    apex_drop_locations = ['Bridge', 'Dome', 'Epicenter', 'Trials', 'Countdown', 'Fragment East', 'Fragment West', 'Geyser', 'Harvest', 'Hill Valley', 'Launch Site', 'Lava City', 'Lava Fissure', 'Mining Pass', 'Overlook', 'Rain Tunnel', 'Refinery', 'Staging', 'Skyhook', 'Sorting Factory', 'Springs End', 'Survey Camp', 'Thermal Station', 'Tree', 'Train Yard']

    if message.content == '!drop':
        response = random.choice(apex_drop_locations)
        await message.channel.send(response)


client.run(TOKEN)