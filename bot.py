""" 
    Main bot file

    This file is the main entry point for the bot. It loads the cogs and starts the bot.
"""
import logging
from logging import info

import asyncio
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

if 'TOKEN' not in os.environ:
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    
    
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
discord_token = os.getenv('TOKEN')
if discord_token is None:
    raise ValueError("Discord token not found in .env file")

@bot.event
async def on_ready():
    """
        Runs when the bot is ready
    """
    info("We have logged in as %s", bot.user)

@bot.event
async def on_command(ctx):
    """
        Logs every command that is run
    """
    info("Command %s invoked by %s", ctx.command, ctx.author)

async def load_extensions():
    """
        Loads all the cogs in the cogs directory
    """
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                info("Loaded cog: %s", filename)
            except Exception as e:
                info("Failed to load cog: %s \n Error: %s", filename, e)

async def main():
    """
        Loads Extensions and starts the bot
    """
    await load_extensions()
    await bot.start(discord_token)

if __name__ == '__main__':
    asyncio.run(main())
