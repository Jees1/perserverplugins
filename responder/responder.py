@client.event
async def on_message(message):

if "wow" in message.content:
    await message.channel.send("oh wow")
