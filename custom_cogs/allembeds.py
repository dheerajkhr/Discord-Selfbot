import discord
from discord.ext import commands

'''Turn every message into an embed.'''


class AllEmbeds:

    def __init__(self, bot):
        self.bot = bot
        self.enabled = False
        
    @commands.command(pass_context=True, aliases=["allembed", "allembeds", "toggleembed"])
    async def toggleembeds(self, ctx):
        """Turns ever message you send into an embed"""
        self.enabled = not self.enabled
        await ctx.send(self.bot.bot_prefix + "Successfully toggled turning all messages to embeds!")
        
    async def on_message(self, message):
        if message.author == self.bot.user:
            if not message.embeds and self.enabled:
                await message.edit(content="", embed=discord.Embed(description=message.content))


def setup(bot):
    bot.add_cog(AllEmbeds(bot))
