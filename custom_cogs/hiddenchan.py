import discord
from discord.ext import commands

'''Display Hidden Channels'''

class HiddenChan:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['hc'], pass_context=True)
    async def hiddenchan(self, ctx):
        """Show hidden channels"""
        await ctx.message.delete()
        bool = None
        if type(ctx.channel) == discord.channel.DMChannel:
            return await ctx.send(self.bot.bot_prefix + "This command *obviously* doesn't work in a DM, you peasant.")
        channels = ""
        nechannels = ""
        hidden = 0
        total = len(ctx.guild.text_channels)
        embed = discord.Embed(title="Hidden channels in {}".format(ctx.message.guild))
        for x in ctx.guild.text_channels:
            if len(channels + "{} - {}\n\n".format(x.name, x.topic)) > 2000:
                bool = False
                break
            elif not x.permissions_for(ctx.author).read_messages:
                channels += "**#{}**".format(x.name)
                nechannels += "#{}".format(x.name)
                if x.topic == "None" or not x.topic:
                    channels += "\n\n"
                    nechannels += "\n\n"
                else:
                    channels += " - {}\n\n".format(x.topic)
                    nechannels += " - {}\n\n".format(x.topic)
                hidden += 1
        if not channels:
            await ctx.send(self.bot.bot_prefix + "There are no channels you cannot see!")
        else:
            if len(channels) <= 1964 and bool == False:
                channels += "**Could not print the rest, sorry.**"
                nechannels += "**Could not print the rest, sorry.**"
            elif bool == False:
                bool = True
            embed.description = channels
            footer = "{} out of {} channels are hidden".format(hidden, total)
            embed.set_footer(text=footer)
            try:
                await ctx.send(embed=embed)
            except:
                await ctx.send("```{}\n\n{}```".format(nechannels, footer))
            if bool == True:
                await ctx.send(self.bot.bot_prefix + "**Could not print the rest, sorry.**")
        
def setup(bot):
    bot.add_cog(HiddenChan(bot))
