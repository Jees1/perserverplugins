from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if " word " in message.content:
          print("Something")
          #or
          await message.channel.send("Something")

def setup(bot):
    bot.add_cog(MyCog(bot))
