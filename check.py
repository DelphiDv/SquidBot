from asyncio.base_events import Server
import discord
from discord import guild
from discord.ext import commands
import asyncio

from discord.ext.commands import bot
from discord.guild import Guild

client = discord.Client()

class check(commands.Cog):
    """docstring"""

    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()     
    @commands.command(hidden = True)
    async def check(self, ctx):
            await ctx.send(", ".join([f"{guild.name}" for guild in self.bot.guilds]))

    @commands.is_owner()
    @commands.command(hidden = True)
    async def checkid(self, ctx):
            await ctx.send(", ".join([f"{guild.name} {guild.id}" for guild in self.bot.guilds]))

    @commands.is_owner()
    @commands.command(hidden = True)
    async def leave(self, ctx, guild: discord.Guild):
            await guild.leave()
            await ctx.send("left the server")

def setup(bot):
    bot.add_cog(check(bot))
