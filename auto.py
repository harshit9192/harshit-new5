import discord
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix='+h12')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def spam(ctx) :
    while True :
        await ctx.send(random.choice(['Hey', 'ILY', 'Smexy asf', 'op bhaii', 'dayyum brodaa', 'tora mai ke bur', 'chala ja beti', 'kadbe chuyaaa', 'ok', 'Jab tak', 'hmm', 'okay man!'])) 
        await asyncio.sleep(20)

client.run('NzI0NTI4NTg2MTE5MTg0NDA0.X9FMJw.2NojjkNiqqiEi4AF-wsMXzSwirw', bot = False)
