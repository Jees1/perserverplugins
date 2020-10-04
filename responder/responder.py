from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
async def on_message(message):
    if "word" in message.content:
          await channel.send("hi")

def setup(bot):
    bot.add_cog(MyCog(bot))
