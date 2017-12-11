import discord
from random import randint
from discord.ext import commands

convert={" ": "+"}

'''Turn every message into image, modified from Appu's Allembeds cog'''


class AllImg:

    def __init__(self, bot):
        self.bot = bot
        self.enabled = False
        
    @commands.command(pass_context=True, aliases=["allimg", "tgi"])
    async def toggleimg(self, ctx):
        """Turns every message into image"""
        self.enabled = not self.enabled
        await ctx.send(self.bot.bot_prefix + "Successfully toggled turning all messages to embeds to `{}`!".format(self.enabled))
        
    async def on_message(self, message):
        
        result = ""
        
        if message.author == self.bot.user:
            if not message.embeds and self.enabled:

                result = message.content.translate(str.maketrans(convert))
                image = "https://dummyimage.com/1280x480/36393E/ffffff.png&text={}".format(result)
                #await message.delete()
                embed = discord.Embed(color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
                embed.set_image(url=image)
                await message.edit(content="", embed=embed)
                
                
    @commands.command()
    async def toimg(self, ctx, *, msg):
        """Make your Text To Image.

        Usage:
        >toimg  <message id>
            
        >toimg <Your String>
            
        >toimg 
            Displays this.
        """
        
        result = ""

        if msg:
            if msg.isdigit():
                async for message in self.bot.logs_from(ctx.message.channel, 100):
                    if str(message.id) == msg:
                        msg = message.content
                        break
        else:
            switch = False
            async for message in self.bot.logs_from(ctx.message.channel, 2):
                if switch:
                    msg = message.content
                else:
                    switch = True

        result = msg.translate(str.maketrans(convert))
        image = "https://dummyimage.com/1280x480/36393E/ffffff.png&text={}".format(result)
        embed = discord.Embed(color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
        embed.set_image(url=image)
        await ctx.message.delete()
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(AllImg(bot))
