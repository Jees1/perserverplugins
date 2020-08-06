import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class botPrivacy(commands.Cog):
    """
    A sample set of rules you can use when your first starting your server to save time.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["myprivacy"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def privacy(self, ctx):
        """Send the Privacy Policy of Drizzle Support"""
        embed = discord.Embed(
            title="Drizzle Support Privacy Policy"
        )
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.description = """
                You can view the Drizzle  Support Privacy Policy [here.](https://gist.github.com/Jees1/93f8b515e921ee4475d63fa0ed47ad82#file-privacypolicy-md)
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(botPrivacy(bot))
