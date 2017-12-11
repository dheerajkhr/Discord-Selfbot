import discord
from discord.ext import commands

'''My Ace Attorney commands'''


class AceAttorney:

    def __init__(self, bot):
        self.bot = bot
		
    @commands.command(pass_context=True)
    async def holy(self, ctx):
        """Edgeworth's Response (image)"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="https://i.imgur.com/KBWpDpW.png")
        await ctx.send(embed=embed)
        embed.set_image(url="https://i.imgur.com/BixOUBV.png")
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['ht'], pass_context=True)
    async def holytext(self, ctx):
        """Edgeworth's Response (text)"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.title = "Miles Edgeworth"
        embed.description = "This one single statement is so full of contradictions... For a moment there, I thought I was going to collapse."
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def press(self, ctx):
        """HOLD IT!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/umt4Pr2.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def object(self, ctx):
        """OBJECTION!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/0GTlFg0.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def take(self, ctx):
        """TAKE THAT!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/qPIwEaq.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def silence(self, ctx):
        """SHUT THE FUCK UP!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/AxbuzZ9.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def gotcha(self, ctx):
        """GOTCHA!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/29ZvDWm.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def enough(self, ctx):
        """ENOUGH!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/paNw1dh.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def fast(self, ctx):
        """NOT SO FAST!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/Nab2PLO.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def got(self, ctx):
        """GOT IT!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/J3X6Fbd.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def eureka(self, ctx):
        """EUREKA!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/O8gVn3q.png")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def guilty(self, ctx):
        """GUILTY!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/1kq5gau.gif")
        await ctx.send(embed=embed)

    @commands.command(aliases=['ng'], pass_context=True)
    async def notguilty(self, ctx):
        """NOT GUILTY!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/KeggKe4.gif")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def satorha(self, ctx):
        """Satorha!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/FMEzpJ7.png")
        await ctx.send(embed=embed)
	
    @commands.command(pass_context=True)
    async def hang(self, ctx):
        """Hang on!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/UQUjdnb.png")
        await ctx.send(embed=embed)
	
    @commands.command(pass_context=True)
    async def look(self, ctx):
        """Have a look!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/kcR7d5W.png")
        await ctx.send(embed=embed)
    
    @commands.command(pass_context=True)
    async def welcome(self, ctx):
        """Welcome!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/ZDQnh9D.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def insolence(self, ctx):
        """Such insolence!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/OIlktYf.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def shut(self, ctx):
        """Shut up!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://http://i.imgur.com/fk9ewJZ.png")
        await ctx.send(embed=embed)
	
    @commands.command(pass_context=True)
    async def over(self, ctx):
        """Overruled!"""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url="http://i.imgur.com/pCLJvzU.png")
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(AceAttorney(bot))