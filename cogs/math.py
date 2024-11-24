# Zenith's math commands
import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents = intents)
tree = app_commands.CommandTree(client)

# basic operation (add, subtract, multiply, divide)
@tree.command(name = "calc", description = "Calculate a simple operation.")
async def calc_command(ctx):
    # TODO logic for operation (get asked operation, compute under PEMDAS?)

