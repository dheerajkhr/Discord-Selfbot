import os
from discord.ext import commands
from cogs.utils.dataIO import dataIO

"""Cog used to mute specific servers which spam unblockable pings"""

class ServerMute:

    def __init__(self, bot):
        self.bot = bot
        if not os.path.exists('settings/server_mute.json'):
            dataIO.save_json('settings/server_mute.json', [])
        self.mute_data = dataIO.load_json('settings/server_mute.json')

    @commands.command(pass_context=True)
    async def servermute(self, ctx, guild_id=""):
        """Toggle mute a server from sending you pings
        Use without argument to mute the current server
        """

        guild_id = int(guild_id) if guild_id else ctx.guild.id
        if guild_id in self.mute_data:
            self.mute_data.remove(guild_id)
            status = "Unmuted"
        else:
            self.mute_data.append(guild_id)
            status = "Muted"
        dataIO.save_json('settings/server_mute.json', self.mute_data)
        await ctx.send(self.bot.bot_prefix + "{} server".format(status))

    async def on_message(self, message):
        if message.guild and message.guild.id in self.mute_data:
            if message.mention_everyone or self.bot.user in message.mentions or bool(set(message.guild.get_member(self.bot.user.id).roles) & set(message.role_mentions)):
                await message.ack()

def setup(bot):
    bot.add_cog(ServerMute(bot))
