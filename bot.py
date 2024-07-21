import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """
        Runs when the bot is ready
    """
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_command(ctx):
    """
        Logs every command that is run
    """
    logging.info("Command %s invoked by %s", ctx.command, ctx.author)

async def load_extensions():
    """
        Loads all the cogs in the cogs directory
    """
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded cog: {filename}")
            except Exception as e:
                print(f"Failed to load cog: {filename}\n{e}")

async def main():
    """
        Loads Extensions and starts the bot
    """
    await load_extensions()
    await bot.start(os.getenv('DISCORD_BOT_TOKEN'))

if __name__ == '__main__':
    asyncio.run(main())
