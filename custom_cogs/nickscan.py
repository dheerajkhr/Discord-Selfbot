import discord
from discord.ext import commands

"""Get a list of all your nicknames!"""

class NickScan:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['ns'])
    async def nickscan(self, ctx):
        """Get a list of all your nicknames!"""
        await ctx.message.delete()
        nick = ""
        bool = None
        for guild in self.bot.guilds:
            if len(nick + "**Server:** `{}` **Nick:** `{}`\n".format(guild.name, guild.get_member(self.bot.user.id).nick)) > 2000:
                bool = False
                break
            if guild.get_member(self.bot.user.id).nick:
                nick += "**Server:** `{}` **Nick:** `{}`\n".format(guild.name, guild.get_member(self.bot.user.id).nick)
        if not nick:
            await ctx.send(self.bot.bot_prefix + "You dont have any nicknames set!")
        else:
            if len(nick) <= 1964 and bool == False:
                nick += "**Could not print the rest, sorry.**"
            elif bool == False:
                bool = True
            try:
                embed = discord.Embed(title="Servers I Have Nicknames In")
                embed.description = nick
                await ctx.send(embed=embed)
            except:
                await ctx.send("```{}```".format(nick))
            if bool == True:
                await ctx.send(self.bot.bot_prefix + "**Could not print the rest, sorry.**")
                
def setup(bot):
    bot.add_cog(NickScan(bot))
