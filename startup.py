# the main file to run Zenith
import discord
from discord import app_commands
from discord.ext.commands.bot import _default, when_mentioned
import logging
import logging.handlers

intents = discord.Intents.default()
client = discord.Client(intents = intents)
tree = app_commands.CommandTree(client)

# establish bot
@client.event
async def on_ready():
    await tree.sync(guild = discord.Object(id = '1056974651634483240'))
    print(client.user, "is ready under ID", client.user.id)

# help command (read from help.txt) TODO send as DM (wtf)
@tree.command(name="help", description="Displays the help menu.")
async def help_command(ctx):
    author = ctx.author        
    await author.send("test")
    with open("help.txt") as helpFile:
        message = helpFile.read

# random command to keep discord tag
@tree.command(name='random', description="Displays the help menu.")
async def random_command(ctx):
    await ctx.send("Hello, keep your discord badge!")        
        
        

# run bot with token
client.run('')

# configure logger
handler = logging.FileHandler(filename='Zenithlog.txt', encoding='utf-8', mode='w')