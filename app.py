# Ask for connection token before connecting
con = input("Discord Token:")
# Import modules
import discord
import asyncio
from discord.ext import commands
# Construct bot
description = "A discord bot that does things for now"
bot = commands.Bot(command_prefix="!", description=description)
# Print a message on successful connection using bot.onevent
@bot.event
async def on_ready():
    print("Connected to discord using {0}".format(con))
# Run the Bastard
bot.run(con)