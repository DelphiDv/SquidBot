import discord
from discord.ext import commands
import os
import io
import random
import asyncio
script_path = os.path.dirname(__file__)


@commands.command()
async def vending_machine(ctx):
    """Buy an item from the vending machine."""

    with open(script_path + "/vending_machine.txt", "r", encoding="utf8") as vending_machine_file:
        the_prize = random.choice(vending_machine_file.readlines())
    
    with open(script_path + "/titles.txt","r", encoding="utf8") as tf:
        the_title = random.choice(tf.readlines())
    embed = discord.Embed(title="_You insert a coin in the vending machine..._", color=0x47e18a)
    message = await ctx.send(content="", embed=embed)
    
    await asyncio.sleep(3) # DRAMATIC TENSION
    
    embed2=discord.Embed(title="**" + the_title + "**", color=0x47e18a)
    embed2.set_thumbnail(url="https://media.discordapp.net/attachments/280298381807714304/776122672898768956/vending_machine.png")
    embed2.add_field(name="_ _", value= the_prize, inline=False)
    embed2.set_footer(text="VoidCorp™")
    await message.edit(content="", embed=embed2)


def setup(bot):
    bot.add_command(vending_machine)
