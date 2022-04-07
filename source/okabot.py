import os
import discord
my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if " reey" in message.content.lower():
    await message.channel.send("No! Not Kongreey Kongroo!")

  if "cong" in message.content.lower():
    await message.channel.send("No! Not Congroo Kongroo!")

client.run(os.getenv('TOKEN'))
my_secret = os.environ['TOKEN']

