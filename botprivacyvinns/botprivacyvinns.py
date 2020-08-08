import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class botPrivacy(commands.Cog):
    """
    The privacy policy of Drizzle Support
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["myprivacy"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def privacy(self, ctx):
        """Send the Privacy Policy of Vinns Support"""
        embed = discord.Embed(
            title="Vinns Support Privacy Policy"
        )
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.description = """
                You can view the Vinns Support Privacy Policy [here.](https://gist.github.com/Jees1/554ce5bf8f4f74b2d341dc64e5ab41b0#file-privacypolicy-md)
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(botPrivacy(bot))
