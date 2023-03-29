import discord
from discord.ext import commands
import random
import asyncio



class joke(commands.Cog):
    """funny commands"""
    def __init__(self, bot):
        self.bot = bot
        
               
    @commands.command()
    async def delete_server(self, ctx):
        """Use in case of the feds finding #true-nsfw"""
        await ctx.author.kick()








async def setup(bot):
    await bot.add_command(joke(bot))