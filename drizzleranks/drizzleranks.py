Iimport asyncio
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
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.description = """
                - | Owner __255__\n- | Co-Owner __254__\n- | Development Team __253__\n- | Group Managers __252__\n- | Overseers __251__\nChairperson __250__\nVice-Chairperson __13__\nExecutive __12__\nPublic Relations Officer __11__\nBoard of Directors __10__\nShift Manager __9__\nSupervisor __8__\nSecurity __7__\nReceptionist __6__\nTrainee __5__\nAllied Represantive __4__\n- | Noted Guest __3__\nX | Suspended __2__\nHotel Guest __1__
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(drizzleRanks(bot))
