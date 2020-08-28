import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class neededStaff(commands.Cog):
    """
    Staff are needed at the hotel/training!
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def neededstaff(self, ctx):
        """Send the Privacy Policy of Drizzle Support"""
        emoji = '✅'
        await message.add_reaction(emoji)
        channel = self.bot.get_channel(620497762072526879)
        embed = discord.Embed(
            title="Staff Request"
        )
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.description = """
                Hey, Staff! We are in need of staff at the hotel.
            """
        embed.add_field(name="Information", value=f"Staff are needed, coming and assisting will be greatly appreciated.", inline=False)
        embed.add_field(name="Link", value=f"https://www.roblox.com/games/1325088285", inline=False)
        embed.color = self.bot.main_color
        return await channel.send("@here", embed=embed)

def setup(bot):
    bot.add_cog(neededStaff(bot))
