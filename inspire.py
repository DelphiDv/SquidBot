import discord
from discord.ext import commands
import random
import asyncio
import urllib.request
import io

class inspire(commands.Cog):
    """docstring"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['inspirobot', 'inspiro', 'inspiration'])
    async def inspire(self, ctx, enabled=False):
        """ Pulls a motivational image from inspirobot.me. """
        await ctx.channel.trigger_typing()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
        api_url = "http://inspirobot.me/api?generate=true"
        path_response = urllib.request.urlopen(urllib.request.Request(api_url,headers={"User-Agent":user_agent}))
        image = urllib.request.urlopen(urllib.request.Request(path_response.read().decode("utf-8"),headers={"User-Agent":user_agent}))
        data = io.BytesIO(image.read())
        await ctx.send(file=discord.File(data,"inspirobot.jpg"))
    
def setup(bot):
    bot.add_cog(inspire(bot))