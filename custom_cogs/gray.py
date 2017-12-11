from discord.ext import commands
from random import randint
import random
import discord


class Gray:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def check(self, ctx, text):
        """Checks A Link""" 
        msg = '```diff\n+ Result : ```'+'https://spoopy.link/' + str(text)
        await ctx.message.delete()
        if len(msg) > 2000:
            await ctx.send('Link Too Long')
        else:
            await ctx.send(msg)

    @commands.command(pass_context=True)
    async def hug(self, ctx, member: discord.Member=None):
        """Hug your waifu!"""
        author = ctx.message.author.mention

        hug = "**{} gave {} a hug!**"
        hugself= "**{} Hugs himself TT**"
        
        choices = ['http://i.imgur.com/sW3RvRN.gif', 'http://i.imgur.com/gdE2w1x.gif', 'http://i.imgur.com/zpbtWVE.gif', 'http://i.imgur.com/ZQivdm1.gif', 'http://i.imgur.com/MWZUMNX.gif', 'https://i.imgur.com/8futZnQ.gif' ,'https://i.imgur.com/viWWVub.gif', 'https://i.imgur.com/S27E05M.gif', 'https://i.imgur.com/mXGKeyN.gif' ,'https://i.imgur.com/mxaqyUu.gif', 'https://i.imgur.com/dLUetXa.gif', 'https://i.imgur.com/hM1LcZf.gif']
        
        image = random.choice(choices)
        
        
        if member:
            mention = member.mention
            embed = discord.Embed(description=hug.format(author, mention), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        else:
            embed = discord.Embed(description=hugself.format(author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
        
        embed.set_image(url=image)
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def kiss(self, ctx, member: discord.Member=None):
        """Kiss your waifu!"""
        
        author = ctx.message.author.mention
        
        kiss = "**{0} gave {1} a kiss!**"
        kissself= "**{} Kissed himself :kiss: **"
        
        choices = ['http://i.imgur.com/0D0Mijk.gif', 'https://i.imgur.com/4VePCc4.gif', 'http://i.imgur.com/3wv088f.gif', 'https://i.imgur.com/dG73Bmb.gif', '', 'https://i.imgur.com/KVLXsPN.gif', 'https://i.imgur.com/5Hx4D9n.gif', 'https://i.imgur.com/j9Gvrrd.gif', 'https://i.imgur.com/jEmrZGS.gif', 'https://i.imgur.com/kn9awse.gif', 'https://i.imgur.com/LLM3iPA.gif' 'https://i.imgur.com/uoaOqXO.gif', 'https://i.imgur.com/dJWlgnr.gif', 'https://i.imgur.com/G8Mbg1Z.gif', 'https://i.imgur.com/evjODur.gif', 'https://i.imgur.com/tumv7DY.gif', 'https://i.imgur.com/4fGLidc.gif']
        
        image = random.choice(choices)
        
        if member:
            mention = member.mention
            embed = discord.Embed(description=kiss.format(author, mention), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        else:
            embed = discord.Embed(description=kissself.format(author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
        
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def lick(self, ctx, member: discord.Member=None):
        """Lick your waifu!"""
        author = ctx.message.author.mention
        
        lick = "**{0} licked {1}!**"
        lickself="{} licked himself :thinking: "
        
        choices = ['https://i.imgur.com/zIDBM1i.gif', 'https://i.imgur.com/sPvTcLf.gif', 'https://i.imgur.com/CxMooY1.gif', 'https://i.imgur.com/VRstYFu.gif', 'https://i.imgur.com/GP6brBA.gif', 'https://i.imgur.com/WTgUmla.gif', 'https://i.imgur.com/44jdPuq.gif', 'https://i.imgur.com/i25AW7V.gif', 'https://i.imgur.com/ftuM6Ep.gif', 'https://i.imgur.com/LR8xv7v.gif', 'http://i.imgur.com/jMSv255.gif', 'https://i.imgur.com/wJ5iDyB.gif']
        
        image = random.choice(choices)
        
        if member:
            mention = member.mention
            embed = discord.Embed(description=lick.format(author, mention), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        else:
            embed = discord.Embed(description=lickself.format(author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        embed.set_image(url=image)
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def pat(self, ctx, member: discord.Member=None):
        """Pat your senpai/waifu!"""
        author = ctx.message.author.mention
        
        pat = "**{} got patted by {}!**"
        patself="{} patted himelf :hugging: "
        
        choices = ['http://i.imgur.com/10VrpFZ.gif', 'http://i.imgur.com/x0u35IU.gif', 'http://i.imgur.com/0gTbTNR.gif', 'http://i.imgur.com/hlLCiAt.gif', 'http://i.imgur.com/sAANBDj.gif', 'https://i.imgur.com/wtxwpm1.gif', 'https://i.imgur.com/rQdg0Xr.gif', 'https://i.imgur.com/3eR7weH.gif', 'https://i.imgur.com/cK8Ro3x.gif', 'https://i.imgur.com/g1H0dHv.gif', 'https://i.imgur.com/qtHlt3n.gif', 'https://i.imgur.com/K3fad03.gif', 'https://i.imgur.com/bzzodCZ.gif', 'https://i.imgur.com/usxXmP0.gif', 'https://i.imgur.com/mLyG5LV.gif', 'https://i.imgur.com/sIOXrRK.gif']
        
        image = random.choice(choices)
        
        if member:
            mention = member.mention
            embed = discord.Embed(description=pat.format(mention,author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        else:
            embed = discord.Embed(description=patself.format(author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        embed.set_image(url=image)
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def slap(self, ctx, member: discord.Member=None):
        """Slap your senpai/waifu!"""     
        author = ctx.message.author.mention
        
        slap = "**{} got slapped by {}**"
        slapself = "**{} slapped himelf**"
        
        choices = ['https://i.imgur.com/EO8udG1.gif', 'https://i.imgur.com/lMmn1wy.gif', 'https://i.imgur.com/TuSUTg5.gif', 'https://i.imgur.com/9Ql97mO.gif', 'https://i.imgur.com/Qkv0q8n.gif', 'https://i.imgur.com/VBGqeIU.gif', 'https://i.imgur.com/uPZwGFQ.gif', 'https://i.imgur.com/Su0X9iF.gif', 'https://i.imgur.com/eNiOIMB.gif',  'https://i.imgur.com/gsAGyoI.gif', 'https://i.imgur.com/sF1BQg2.gif', 'https://i.imgur.com/zTiJjev.gif']
        
        image = random.choice(choices)
        
        if member:
            mention = member.mention
            embed = discord.Embed(description=slap.format(mention,author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        else:
            embed = discord.Embed(description=slapself.format(author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
        
        embed.set_image(url=image)
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Gray(bot))
