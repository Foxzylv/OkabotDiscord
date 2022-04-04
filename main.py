import os
import discord
my_secret = os.environ['KeyTK']

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('El Psy Kongreey'):
   await message.channel.send('No! Not Kongreey Kongaroo!')

    if message.content.startswith('El Psy Congroo'):
     await message.channel.send('No! Not Congroo Kongroo!')

client.run(os.getenv('KeyTK'))
