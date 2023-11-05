import discord
from discord.ext import commands
import uuid
import requests
import shutil
import os
from settings import CBotSettings as CBotSettings

# Init checks to ensure bot functionality.
if not os.path.isdir(CBotSettings.ArchiveRoot):
    print(f"The archive root ({CBotSettings.ArchiveRoot}) does not exist. Created it!")
    os.mkdir(CBotSettings.ArchiveRoot)
for folder in CBotSettings.ArchiveChannels:
    if not os.path.isdir(f"{CBotSettings.ArchiveRoot}/{folder}"):
        print(f"The archive category ({CBotSettings.ArchiveRoot}/{folder}) does not exist. Created it!")
        os.mkdir(f"{CBotSettings.ArchiveRoot}/{folder}")


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot launched as: {client.user}")

@client.event
async def on_message(message):
    # Archiver
    if CBotSettings.ArchiveImages == True:
        # Archiver
        try:
            RandomFileName = str(uuid.uuid4())
            SourceChannel = str(message.channel)
            print(SourceChannel)
            print(message.attachments[0].content_type)
            if message.attachments[0].content_type == "image/png":
                await message.attachments[0].save(RandomFileName + ".png")
                shutil.move(RandomFileName + ".png", CBotSettings.ArchiveRoot + "/" + SourceChannel)
            if message.attachments[0].content_type == "image/jpeg":
                await message.attachments[0].save(RandomFileName + ".jpeg")
                shutil.move(RandomFileName + ".jpeg", CBotSettings.ArchiveRoot + "/" + SourceChannel)
            if message.attachments[0].content_type == "image/jpg":
                await message.attachments[0].save(RandomFileName + ".jpg")
                shutil.move(RandomFileName + ".jpg", CBotSettings.ArchiveRoot + "/" + SourceChannel)
            if message.attachments[0].content_type == "image/webm":
                await message.attachments[0].save(RandomFileName + ".webm")
                shutil.move(RandomFileName + ".webm", CBotSettings.ArchiveRoot + "/" + SourceChannel)
            if message.attachments[0].content_type == "image/gif":
                await message.attachments[0].save(RandomFileName + ".gif")
                shutil.move(RandomFileName + ".gif", CBotSettings.ArchiveRoot + "/" + SourceChannel)
        except Exception as e:
            print("An error occured: " + e)
    if message.author == client.user:
        return
    #### Call commands here! ####
    if message.content.startswith(f'{CBotSettings.CommandSymbol}ping'):
        await message.channel.send("Pong!")


# Run the bot!
client.run(f'{CBotSettings.TOKEN}')