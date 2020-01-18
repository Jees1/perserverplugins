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
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.description = """
                - | Executive Committees (<@!553384447462998040>, <@!405781220090314763>, <@!298014369533657090>, <@!526102961969954816>)\nHead of Discord Moderation - Jees1 (<@!349899849937846273>)\nHead of Alliances - UpsetDarkKiller (<@!466723493837537280>)
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(drizzleExecutive(bot))
