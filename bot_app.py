import discord
import dotenv
import json
import os
dotenv.load_dotenv()
config = dotenv.dotenv_values()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    """
    :param message: The message from the server
    :type message: discord.Message
    :return:
    """
    if message.author == client.user:
        return
    server = message.guild
    author = message.author
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(config.get("CLIENT_TOKEN"))
