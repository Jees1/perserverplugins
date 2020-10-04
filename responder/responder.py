from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        message.channel.send(message.content)

def setup(bot):
    bot.add_cog(MyCog(bot))
