import discord
from discord.ext import commands
import random
import asyncio


class other(commands.Cog):
    """funny commands"""

    def __init__(self, bot):
        self.bot = bot
        
               
    @commands.command()
    async def delete_server(self, ctx):
        """Use in case of the feds finding #true-nsfw"""
        await ctx.author.kick()







def setup(bot):
    bot.add_cog(other(bot))
