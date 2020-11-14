import discord
from discord.ext import commands
import asyncio


class check(commands.Cog):
    """docstring"""

    def __init__(self, bot):
        self.bot = bot
                
        
    @commands.command()
    async def servers(self, ctx):
        await ctx.send(", ".join([f"{guild.name} {guild.id}" for guild in self.bot.guilds]))


def setup(bot):
    bot.add_cog(check(bot))
