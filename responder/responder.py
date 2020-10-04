from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.event
async def on_message(message):

if "wow" in message.content:
    await message.channel.send("oh wow")

def setup(bot):
    bot.add_cog(MyCog(bot))
