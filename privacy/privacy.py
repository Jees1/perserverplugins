import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class privacy(commands.Cog):
    """
    Show the link to the Drizzle Support Privacy Policy.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["privacy"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def privacy(self, ctx):
        """"""
        embed = discord.Embed(
            title="Drizzle Support Privacy Policy"
        )
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.description = """
                You can view information about your privacy [here.](https://gist.github.com/Jees1/93f8b515e921ee4475d63fa0ed47ad82#file-privacypolicy-md)
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(privacy(bot))
