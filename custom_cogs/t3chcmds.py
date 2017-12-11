import discord
from discord.ext import commands

'''Just a bunch of ascii faces and such.'''


class T3CHCmds:

    def __init__(self, bot):
        self.bot = bot
		
    @commands.command()
    async def xd(self, ctx):
        """Large XD made of XDs"""
        await ctx.message.delete()
        await ctx.send("XD      XD    XD  XD\n  XD  XD      XD      XD\n     XD           XD       XD\n  XD  XD      XD      XD\nXD      XD    XD  XD")

    @commands.command()
    async def lenny(self, ctx):
        """( ͡° ͜ʖ ͡°)"""
        await ctx.message.delete()
        await ctx.send("( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def shrug(self, ctx):
        """¯\_(ツ)_/¯"""
        await ctx.message.delete()
        await ctx.send("¯\_(ツ)_/¯")
    
    @commands.command()
    async def magic(self, ctx):
        """(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ"""
        await ctx.message.delete()
        await ctx.send("(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ")

    @commands.command()
    async def tableflip(self, ctx):
        """(ノಠ益ಠ)ノ彡┻━┻"""
        await ctx.message.delete()
        await ctx.send("(ノಠ益ಠ)ノ彡┻━┻")

    @commands.command()
    async def unflip(self, ctx):
        """ ┬─┬ ノ( ゜-゜ノ)"""
        await ctx.message.delete()
        await ctx.send(" ┬─┬ ノ( ゜-゜ノ)")

    @commands.command()
    async def wtf(self, ctx):
        """Ծ_Ծ"""
        await ctx.message.delete()
        await ctx.send("Ծ_Ծ")

    @commands.command()
    async def soon(self, ctx):
        """™"""
        await ctx.message.delete()
        await ctx.send("Soon™")

    @commands.command()
    async def lennyshrug(self, ctx):
        """¯\_( ͡° ͜ʖ ͡°)_/¯"""
        await ctx.message.delete()
        await ctx.send("¯\_( ͡° ͜ʖ ͡°)_/¯")

def setup(bot):
    bot.add_cog(T3CHCmds(bot))
