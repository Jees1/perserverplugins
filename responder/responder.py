from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bots

    @commands.Cog.listener()
    async def on_message(self, message):
if (message.author.bot):
        return
        if "cool" in message.content.lower():
          await message.channel.send("cool indeed")
def setup(bots):
    bots.add_cog(MyCog(bots))
