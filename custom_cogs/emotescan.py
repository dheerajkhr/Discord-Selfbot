import discord
from discord.ext import commands

'''Scan a server for your emote'''

class EmoteScan:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['es'])
    async def emojiscan(self, ctx, msg):
        """Scan all servers for a certain emote"""
        await ctx.message.delete()
        bool = None
        servers = ""
        emote = msg.split(":")[1] if msg.startswith("<") else msg
        for guild in self.bot.guilds:
            if len(servers + "{}\n".format(guild.name)) > 2000:
                bool = False
                break
            for emoji in guild.emojis:
                if emoji.name == emote:
                    servers += guild.name + "\n"
        if servers is None:
            await ctx.send(self.bot.bot_prefix + "That emote is not on any of your servers.")
        else:
            if len(servers) <= 1964 and bool == False:
                servers += "**Could not print the rest, sorry.**"
            elif bool == False:
                bool = True
            try:
                embed = discord.Embed(title="Servers with the {} emote".format(msg))
                embed.description = servers
                await ctx.send(embed=embed)
            except:
                await ctx.send("```{}```".format(servers))
            if bool == True:
                await ctx.send(self.bot.bot_prefix + "**Could not print the rest, sorry**")
                

def setup(bot):
    bot.add_cog(EmoteScan(bot))
