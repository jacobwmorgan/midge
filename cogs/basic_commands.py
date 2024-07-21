from discord.ext import commands

class BasicCommands(commands.Cog, name="Basic Commands"):
    """
        Basic commands for the bot
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """
            Ping the bot to check if it is online
        """
        await ctx.send('Meow! :cat:')

async def setup(bot):
    """
        Adds the cog to the bot
    """
    print("Loading BasicCommands cog...")
    await bot.add_cog(BasicCommands(bot))
