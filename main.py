import random
import discord
from discord import app_commands
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


intents = discord.Intents.all()
intents.message_content = True

client = commands.Bot(intents = intents, command_prefix=CBotSettings.CommandSymbol)

@client.event
async def on_ready():
    print(f"Bot authenticated as: {client.user}")
    print("Syncing commands...")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)!")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@client.event
async def on_message(message):
    # Archiver
    if CBotSettings.ArchiveImages == True:
        # Archiver
        try:
            RandomFileName = str(uuid.uuid4())
            SourceChannel = str(message.channel)
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
            #print("An error occured: " + e)
            pass
    if message.author == client.user:
        return

### COMMANDS ###

@client.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! Get to gooning already!~", ephemeral=True)

@client.tree.command(name="cunny", description="You like small girls I see~")
async def cunny(interaction: discord.Interaction, category: str):
    media = os.listdir(CBotSettings.ArchiveRoot + "/" + category)
    random_media = random.choice(media)
    random_media_str = os.path.basename(random_media)
    await interaction.response.send_message(f"Get nasty!~", file=discord.File(f"{CBotSettings.ArchiveRoot}/{category}/{random_media_str}"), ephemeral=True)

@client.tree.command(name="totals", description="How many are there?!~")
async def totals(interaction: discord.Interaction):
    cpt = sum([len(files) for r, d, files in os.walk(f"{CBotSettings.ArchiveRoot}")])
    await interaction.response.send_message(f"We've archived {cpt} delicious tiny ones in total~")

# Run the bot!
client.run(f'{CBotSettings.TOKEN}')