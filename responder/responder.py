from discord.ext import commands
import asyncio
class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
cooldown = True
    @commands.Cog.listener()
    async def on_message(self, message):
     if cooldown == True:
        if "happy birthday" in message.content.lower():
          cooldown = False
          await message.channel.send("ye happy birthday")
          asyncio.sleep(1)
          cooldown = True
def setup(bot):
    bot.add_cog(MyCog(bot))
