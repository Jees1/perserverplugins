import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import asyncio


class Suggest(commands.Cog):
    """
    Let's you send a suggestion to a designated channel.
    """
    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def suggest(self, ctx, *, suggestion):
        """
        Suggest something!

        **Usage**:
        -suggest Add coffee to the bar.
        """
        try:
          discChannel = self.bot.get_channel(686858225743822883)
          trainingChannel = self.bot.get_channel(686253519350923280)
          hotelChannel = self.bot.get_channel(777656824098062385)
          texta = """**React with the type of your suggestion:**
  <:Discord:795240449103233024> | Discord Suggestion
  🏨 | Hotel Suggestion
  <:studio:639558945584840743> | Training Center Suggestion
  ❌ | Cancel Command"""
          embed1 = discord.Embed(description=texta, color=self.bot.main_color)
          reactionmsg = await ctx.send(content = f"<@!{ctx.author.id}>", embed = embed1)
          for emoji in ('<:Discord:795240449103233024>', '🏨', '<:studio:639558945584840743>', '❌'):
            await reactionmsg.add_reaction(emoji)
          suggestEmbed = discord.Embed(description=suggestion, color=self.bot.main_color)
          suggestEmbed.set_footer(text="Vinns Hotel Suggestions | -suggest")
          suggestEmbed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
          embedTimeout = discord.Embed(description="❌ | You took too long! Command cancelled", color=15158332)

          def check(r, u):
            return u == ctx.author
          try:
            reaction, user = await self.bot.wait_for("reaction_add", check=check, timeout=60)
          except asyncio.TimeoutError:
            await reactionmsg.edit(embed = embedTimeout)
          if str(reaction.emoji) == '<:Discord:795240449103233024>':
            sugmsg = await discChannel.send(embed=suggestEmbed)
            editEmbed = discord.Embed(description=f"✅ | Successfully sent your suggestion to <#{discChannel.id}>", color=3066993)
            await reactionmsg.edit(embed=editEmbed)
          if str(reaction.emoji) == '🏨':
            sugmsg = await hotelChannel.send(embed=suggestEmbed)
            editEmbed = discord.Embed(description=f"✅ | Successfully sent your suggestion to <#{hotelChannel.id}>", color=3066993)
            await reactionmsg.edit(embed=editEmbed)

          if str(reaction.emoji) == '<:studio:639558945584840743>':
            sugmsg = await trainingChannel.send(embed=suggestEmbed)
            editEmbed = discord.Embed(description=f"✅ | Successfully sent your suggestion to <#{trainingChannel.id}>", color=3066993)
            await reactionmsg.edit(embed=editEmbed)
          if str(reaction.emoji) == '❌':
            editEmbed = discord.Embed(description="❌ | Cancelled command.", color=15158332)
            await reactionmsg.edit(embed=editEmbed)
          await reactionmsg.clear_reactions()
          for emoji in ('✅', '❌'):
            await sugmsg.add_reaction(emoji)
        except discord.ext.commands.CommandOnCooldown

def setup(bot):
    bot.add_cog(Suggest(bot))
