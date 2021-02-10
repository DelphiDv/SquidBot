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

logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO)



bot = commands.Bot(command_prefix=squidconfig.prefix)
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

bot.load_extension('simple')
bot.load_extension('check')
bot.load_extension('joke')
bot.load_extension('vending_machine')
bot.load_extension('inspire')     
 
@bot.command()
async def ping(ctx):
    """ Respond with the bot's reponse time. """
    await ctx.send(f"Ping! Took **{round(bot.latency * 1000, 2)}** ms")



bot.run(API_TOKEN)
