import asyncio
import discord
import datetime
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class neededStaff(commands.Cog):
    """
    Staff are needed at the hotel/training!
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def hotel(self, ctx):
        """Request staff to the hotel easily."""
        channel = self.bot.get_channel(620497762072526879)
        embed = discord.Embed(
            title="Staff Request"
        )
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.add_field(name="Information", value=f"Staff are needed at the hotel! Please provide assistance if you could.", inline=False)
        embed.add_field(name="Link", value=f"[Hotel](https://www.roblox.com/games/1325088285)", inline=False)
        embed.color = self.bot.main_color
        embed.timestamp=datetime.datetime.utcnow()
        embed.set_footer(text="Drizzle Systems")
        embed.set_thumbnail(url="https://t1.rbxcdn.com/a84278c3d729448d813c17b87a679cd6")
        await ctx.send("<a:check:742680789262663710> | Staff successfully requested.")
        return await channel.send("@here", embed=embed)
    
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def training(self, ctx):
        """Request staff to the hotel easily."""
        channel = self.bot.get_channel(620497762072526879)
        embed = discord.Embed(
            title="Staff Request"
        )
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.add_field(name="Information", value=f"Staff are needed at the Training Center! Please come on down if you can.", inline=False)
        embed.add_field(name="Link", value=f"[Hotel](https://www.roblox.com/games/1474744297)", inline=False)
        embed.color = self.bot.main_color
        embed.timestamp=datetime.datetime.utcnow()
        embed.set_footer(text="Drizzle Systems")
        embed.set_thumbnail(url="https://t6.rbxcdn.com/517fd3659bb2d45247006fc29870871f")
        await ctx.send("<a:check:742680789262663710> | Staff successfully requested.")
        return await channel.send("@here", embed=embed)    
    

def setup(bot):
    bot.add_cog(neededStaff(bot))
