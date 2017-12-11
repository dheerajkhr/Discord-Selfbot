import discord
from discord.ext import commands

'''Check what friends are on the current server.'''

class ServerFriends:
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['sf'], pass_context=True)
    async def serverfriends(self, ctx):
        """Check friends on the current server."""
        await ctx.message.delete()
        friends = ""
        bool = None
        for user in ctx.guild.members:
            if len(friends + "<@{}>\n".format(str(user.id))) > 2000:
                bool = False
                break
            if user.relationship:
                if user.relationship.type == discord.RelationshipType.friend:
                    friends += "<@{}>\n".format(str(user.id))
        if not friends:
            await ctx.send("You have no friends on this server ☹")
        else:
            if len(friends) <= 1964 and bool == False:
                friends += "**Could not print the rest, sorry.**"
            elif bool == False:
                bool = True
            try:
                embed = discord.Embed(title="Friends on this server")
                embed.description = friends
                await ctx.send(embed=embed)
            except:
               await ctx.send("```{}```".format(friends))
            if bool == True:
                await ctx.send(self.bot.bot_prefix + "**Could not print the rest, sorry.**")
            
def setup(bot):
    bot.add_cog(ServerFriends(bot))
