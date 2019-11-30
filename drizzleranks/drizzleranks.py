import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class drizzleRanks(commands.Cog):
    """
    A sample set of rules you can use when your first starting your server to save time.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["groupranks"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def ranks(self, ctx):
        """Send the ranks of Drizzle Hotels"""
        embed = discord.Embed(
            title="Drizzle Hotel Ranks"
        )
        embed.description = """
                > - | Owner __255__
                > - | Co-Owner __254__
                > - | Development Team __253__
                > - | Group Managers __252__
                > - | Overseers __251__
                > Chairperson __250__
                > Vice-Chairperson __13__
                > Executive __12__
                > Public Relations Officer __11__
                > Board of Directors __10__
                > Shift Manager __9__
                > Supervisor __8__
                > Security __7__
                > Receptionist __6__
                > Trainee __5__
                > Allied Represantive __4__
                > - | Noted Guest __3__
                > X | Suspended __2__
                > Hotel Guest __1__
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(drizzleRanks(bot))
