import asyncio
import random
import time
from typing import List, Optional
import os
import discord
from discord.ext import commands
script_path = os.path.dirname(__file__)

with open(script_path + "/data/answers.txt", "r", encoding="utf8") as answer:
    answer_list = answer.readlines()
    
@commands.command()
async def squidball(ctx: commands.Context, *, question: str):
        embed=discord.Embed(title="Oh great Squid!", description= ctx.author.mention + ' asks ' + question, color=0x47e18a)
        embed.set_author(name="SquidBall")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/8_ball_icon.svg/1200px-8_ball_icon.svg.png")
        embed.add_field(name="The great SquidBall says:", value= random.choice(answer_list), inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(squidball)
