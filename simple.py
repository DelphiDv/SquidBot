import discord
from discord.ext import commands
import random
import asyncio
import aiosqlite

class simple(commands.Cog):
    """docstring"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def avatar(self, ctx, human: discord.Member = None):
        """Returns a user's avatar."""
        mem = (human or ctx.author)
        aemb = discord.Embed(
            title=f"Avatar for {mem}",
            color=0xBEF4C3
        )
        aemb.set_image(url=mem.avatar_url)
        await ctx.send(embed=aemb)
        
        
    @commands.command()
    async def blap(self, ctx, how: discord.Member = None):
        if how:   
            await ctx.send('> ' + how.mention + ' has been <:blap:685653048596758660> **BLAPPED** <:blap:685653048596758660>')
        else:
            await ctx.send('> ' + ctx.message.author.mention + ' has <:blap:685653048596758660> **BLAPPED** <:blap:685653048596758660> ')   
            
            
    @commands.command()
    async def bless(self, ctx, how: discord.Member = None):
        if how:   
            await ctx.send('> ' + how.mention + ' has been <:bless:685958638950678529> **blessed** <:bless:685958638950678529>')
        else:
            await ctx.send('Bless who?')
            
            
    @commands.command()
    async def icon(self, ctx):
        """Returns the server's icon."""
        iemb = discord.Embed(
            title=f"Guild icon for {ctx.guild.name}",
            color=0xBEF4C3
        )
        iemb.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=iemb)
        
        
    @commands.command()
    async def rng(self, ctx, nu1: int = 1, nu2: int = 100): # defaults 1 & 100
        """Simple random number generator."""
        await ctx.send(random.randint(nu1, nu2))

def setup(bot):
    bot.add_cog(simple(bot))
