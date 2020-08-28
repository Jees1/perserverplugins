import asyncio
import discord
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
    async def neededstaff(self, ctx):
        """Request staff to the hotel easily."""
        channel = self.bot.get_channel(620497762072526879)
        embed = discord.Embed(
            title="Staff Request"
        )
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.add_field(name="Information", value=f"Staff are needed at the hotel! Please come on down if you can.", inline=False)
        embed.add_field(name="Link", value=f"[Click Here](https://www.roblox.com/games/1325088285)", inline=False)
        embed.color = self.bot.main_color
        embed.set_thumbnail(url="https://t5.rbxcdn.com/35d321e763a07069d09beebf4324f0fd")
        await ctx.send("<a:check:742680789262663710> | Staff successfully requested.")
        return await channel.send("@here", embed=embed)

def setup(bot):
    bot.add_cog(neededStaff(bot))
