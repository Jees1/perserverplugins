import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from core import checks
from core.models import PermissionLevel


class movemention(commands.Cog):
    """
    Ping a role on move!
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["movemention"])
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def moveping(self, ctx, *,role: discord.Role):
        """Ping a role on move!"""
        if role is None:
            await ctx.send('Please write a *correct role name*')
        try:
          await ctx.send(f"<@&{role.id}>")
        
        except discord.Forbidden:
         await ctx.send('I do not have permission to delete this role')
        
def setup(bot):
    bot.add_cog(movemention(bot))
