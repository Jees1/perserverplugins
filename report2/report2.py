import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import asyncio


class Reports(commands.Cog):
    """
    Easy report system right here!
    """
    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def report(self, ctx):
        """
        Report a player.
        """

        staffChannel = self.bot.get_channel(742712457084272651)
        guestChannel = self.bot.get_channel(742712346312573020)
        texta = """**React with the type of your report:**
1️⃣ | Staff Report
2️⃣ | User Report
❌ | Cancel
"""
        
        embedTimeout = discord.Embed(description="❌ | You took too long! Command cancelled", color=3066993)
        embed1 = discord.Embed(description=texta, color=self.bot.main_color)
        embed1.set_footer(text="React with ❌ to cancel")
        reactionmsg = await ctx.send(embed = embed1)
        for emoji in ('1️⃣', '2️⃣', '❌'):
          await reactionmsg.add_reaction(emoji)
        
        def checkmsg(msg: discord.Message):
          return msg.channel == ctx.channel and msg.author == ctx.author

        def check(r, u):
          return u == ctx.author
        try:
          reaction, user = await self.bot.wait_for("reaction_add", timeout=20.0, check=check)
        except asyncio.TimeoutError:
          return await reactionmsg.edit(embed = embedTimeout)

        if str(reaction.emoji) == '1️⃣':
          await reactionmsg.clear_reactions()

          text = "Alright, we'll do a staff report. What is the username of the user you're reporting? You have 2 minutes to reply."
          await reactionmsg.edit(embed = discord.Embed(description=text, color=self.bot.main_color))

          try:
            username = await self.bot.wait_for('message', check=checkmsg, timeout=120)
          except asyncio.TimeoutError:
            
            return await reactionmsg.edit(embed = embedTimeout)
          await username.delete()

          text = "What is the rank of the suspect? You have 2 minutes to reply."
          await reactionmsg.edit(embed = discord.Embed(description=text, color=self.bot.main_color))

          try:
            rank = await self.bot.wait_for('message', check=checkmsg, timeout=120)
          except asyncio.TimeoutError:
            return await reactionmsg.edit(embed = embedTimeout)
          await rank.delete()
          
          text = "What is the reason for this report? You have 2 minutes to reply."
          await reactionmsg.edit(embed = discord.Embed(description=text, color=self.bot.main_color,))

          try:
            reason = await self.bot.wait_for('message', check=checkmsg, timeout=120)
          except asyncio.TimeoutError:
            return await reactionmsg.edit(embed = embedTimeout)
          await reason.delete()

          text = "Please provide proof of this happening. You can upload a video/image or use a link to an image or video. The report will be sent right after. You have 10 minutes to reply."
          await reactionmsg.edit(embed = discord.Embed(description=text, color=self.bot.main_color))

          try:
            proof = await self.bot.wait_for('message', check=checkmsg, timeout=600)
          except asyncio.TimeoutError:
            return await reactionmsg.edit(embed = embedTimeout)
          my_files = [await x.to_file() for x in proof.attachments]
          await proof.delete()

          reportEmbed = discord.Embed(title="New Staff Report", description=f"Username: {username.content}\nRank: {rank.content}\nReason: {reason.content}\nProof: {proof.content}", color=self.bot.main_color)

          await staffChannel.send(embed = reportEmbed, files = my_files)
          text = "The report has successfully been sent!"
          await reactionmsg.edit(embed = discord.Embed(description=text, color=3066993))

        if str(reaction.emoji) == '2️⃣':
          text = "Alright, we'll do a normal user report. What is the username of the user you're reporting?"
          await reactionmsg.edit(embed = discord.Embed(description=text, color=self.bot.main_color))

        if str(reaction.emoji) == '❌':
          cancelEmbed = discord.Embed(description="❌ | Cancelled report", color=15158332)
          await reactionmsg.edit(embed=cancelEmbed)
          return await reactionmsg.clear_reactions() 

def setup(bot):
    bot.add_cog(Reports(bot))
