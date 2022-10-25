import json
import os
import random

import discord
from dotenv import load_dotenv

# Load our .env variables
load_dotenv()

# Bot token, get this from https://discord.com/developers
token = os.getenv('DISCORD_TOKEN')
if token is None:
    print("Missing DISCORD_TOKEN in .env")
    exit(1)

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

# Get the quotes
quotesFile = open("quotes.json")
quotes = json.load(quotesFile)['quotes']
# Event listener, this fires whenever the bot detects a new message.  It provides the message as input.]


@bot.event
async def on_message(message):
    # Don't do anything if the message is from the bot
    if message.author == bot.user:
        return
    # If the message has vizzy t, reply with a quote from the one true king
    if "vizzy t" in message.content.lower():
        # Reply to the message expressing your support for Python
        replyMessage = random.choice(quotes)
        # Some quotes use the author's name
        if "{}" in replyMessage:
            replyMessage.format(message.author)
        await message.reply(replyMessage)


# Event listener, this fires when the bot connects to Discord and is online
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Start the bot
bot.run(token)
