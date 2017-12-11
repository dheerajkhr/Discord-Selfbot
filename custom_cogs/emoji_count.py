import discord
import json
from PythonGists import PythonGists
from discord.ext import commands

'''Module to count emojis of every server you are a part of.'''


class EmojiCount:

    def __init__(self, bot):
        self.bot = bot

    async def simple_embed(self, text, title="", color=discord.Color.default()):
        embed = discord.Embed(title=title, color=color)
        embed.description = text
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=["emojicount"])
    async def emotecount(self, ctx):
        """Lists information on the module and links to the module"""
        large_msg = False
        msg = ""
        totalecount = 0
        for g in self.bot.guilds:
            ecount = 0
            for e in g.emojis:
                ecount = ecount + 1
                totalecount = totalecount + 1
            msg = msg + (g.name + ": " + str(ecount)) + "\n"
        await ctx.message.delete()
        if len(msg) > 1900:
            msg = PythonGists.Gist(description='Emoji Count for ' + ctx.message.author.name, content=msg, name='emoji.txt')
            large_msg = True
        color = None
        with open('settings/optional_config.json', 'r+') as fp:
            opt = json.load(fp)
            if opt['embed_color'] != "":
                color = opt['embed_color']
        if color:
            if color.startswith('#'):
                color = color[1:]
            if not color.startswith('0x'):
                color = '0x' + color
        if(color):
            embed = discord.Embed(title="Emoji count for " + ctx.message.author.name, color = int(color, 16))
        else:
            embed = discord.Embed(title="Emoji count for " + ctx.message.author.name)
        if large_msg:
            embed.add_field(name="Individual Server Emote Count", value="[Gist of Server Emote Count]("+msg+")", inline = False)
        else:
            embed.add_field(name="Individual Server Emote Count", value=msg, inline = False)
        embed.add_field(name="Total Emote Count", value=str(totalecount), inline = False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(EmojiCount(bot))