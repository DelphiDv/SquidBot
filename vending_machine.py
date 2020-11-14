import discord
from discord.ext import commands
import os
import io
import random



@commands.command()
async def vending_machine(ctx):
    """Buy an item from the vending machine."""

    with open(r"C:\Users\jerem\OneDrive\Bureau\SquidBot\vending_machine.txt", "r", encoding="utf8") as vending_machine_file:
        the_prize = random.choice(vending_machine_file.readlines())
    
    with open(r"C:\Users\jerem\OneDrive\Bureau\SquidBot\titles.txt","r", encoding="utf8") as tf:
        the_title = random.choice(tf.readlines())

    embed=discord.Embed(title="**" + the_title + "**", color=0x47e18a)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/280298381807714304/776122672898768956/vending_machine.png")
    embed.add_field(name="_ _", value= the_prize, inline=False)
    embed.set_footer(text="SquidCorp™")
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(vending_machine)
