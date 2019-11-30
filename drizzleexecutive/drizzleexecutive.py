import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class drizzleExecutive(commands.Cog):
    """
    A sample set of rules you can use when your first starting your server to save time.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["executive"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def executives(self, ctx):
        """Send the executives of Drizzle Hotels"""
        embed = discord.Embed(
            title="Drizzle Hotel Executives"
        )
        embed.description = """
                > Head of Discord Moderation - Jees1 (<@349899849937846273>)
                > Head QOTD - Nick (<@561923789152190466>)
                > Head of Alliances - Max | temporarily (<@553384447462998040>)
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(drizzleExecutive(bot))
