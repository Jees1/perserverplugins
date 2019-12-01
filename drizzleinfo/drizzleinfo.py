import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class drizzleinfo(commands.Cog):
    """
    A sample set of rules you can use when your first starting your server to save time.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["credits"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def drizzleinfo(self, ctx):
        """Send the credits of the bot."""
        embed = discord.Embed(
            title="Credits of the bot"
        )
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.description = """
                *This bot was setup for Drizzle Hotels for the cause of Moderators communicating with our users privately.*

**Credits:**
Kyb3r,
Taki,
Stephen,
Piyush,
DazVise,
Jees1.

**Who to contact for bugs?**
Contact Jees1 (<@349899849937846273>) for bugs.
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(drizzleinfo(bot))
