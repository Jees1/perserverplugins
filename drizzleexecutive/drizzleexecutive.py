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
                You can view the Drizzle  Support Privacy Policy [here.](https://gist.github.com/Jees1/93f8b515e921ee4475d63fa0ed47ad82#file-privacypolicy-md)
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(drizzleExecutive(bot))
