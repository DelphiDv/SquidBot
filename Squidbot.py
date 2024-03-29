from discord.ext.commands.errors import DisabledCommand
import squidconfig
import discord
import os
import re
import time
import threading
import asyncio
from collections import defaultdict
from discord.ext import commands
from discord import Attachment
import logging
from utils import SquidBed
import random
import markovify
import nltk
import sys
import aiosqlite
from discord import Intents

script_path = os.path.dirname(__file__)
logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO)
intents = discord.Intents.default()
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=squidconfig.prefix,intents=intents)
bot.logger = logger
API_TOKEN = squidconfig.token
BOT_NAME  = 'Squid_OS'
activity = discord.Activity(name="Swimming trough space-time", type=discord.ActivityType.playing)

@bot.event
async def on_ready():
    await bot.change_presence(activity=activity)
    print('[LOGIN SUCCESSFUL]')
    print('----------------------')
    print(f'BOT: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('----------------------')

    await bot.load_extension('inspire')
    await bot.load_extension('simple')
    await bot.load_extension('check')
    await bot.load_extension('joke')
    await bot.load_extension('vending_machine')
    await bot.load_extension('squidball')
 
 
@bot.command()
async def ping(ctx):
    """ Respond with the bot's reponse time. """
    await ctx.send(f"Ping! Took **{round(bot.latency * 1000, 2)}** ms")

with open(script_path + "/data/mind.txt", encoding="utf8") as f:
    text = f.readlines()
model = markovify.Text(text, state_size=1, well_formed = False, retain_original=False,)
max_overlap_ratio = 40
max_overlap_total = 3
print('----------------------')
print('Model Loaded!')
print('----------------------')




#respond when tagged
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    elif BOT_NAME in message.content.lower() or bot.user.mentioned_in(message):
        await message.channel.send(model.make_sentence(tries=50))





bot.run(API_TOKEN)
asyncio.run(bot.db.close())
