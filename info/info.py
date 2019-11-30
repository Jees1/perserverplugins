import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class info(commands.Cog):
    """
    A sample set of rules you can use when your first starting your server to save time.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["credits"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def info(self, ctx):
        """Send the executives of Drizzle Hotels"""
        embed = discord.Embed(
            title="Drizzle Hotel Executives"
        )
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.description = """
            Hello
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))