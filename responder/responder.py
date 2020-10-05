from discord.ext import commands
import asyncio
class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if "happy birthday" in message.content.lower():
          await message.channel.send("ye happy birthday")
          asyncio.sleep(1)
def setup(bot):
    bot.add_cog(MyCog(bot))
