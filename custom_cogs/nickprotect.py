import os
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO

'''Module for protecting your nickname in a server from being changed.'''


class NickProtect:
    def __init__(self, bot):
        self.bot = bot
        self.allowed = False
        if not os.path.exists('settings/nick_protect.json'):
            dataIO.save_json('settings/nick_protect.json', {})
        self.nick_data = dataIO.load_json('settings/nick_protect.json')

    @commands.command()
    async def nickprotect(self, ctx):
        """Toggle nickprotect in the current server."""
        if str(ctx.message.guild.id) in self.nick_data:
            self.nick_data[str(ctx.message.guild.id)] = not self.nick_data[str(ctx.message.guild.id)]
        else:
            self.nick_data[str(ctx.message.guild.id)] = True
        dataIO.save_json('settings/nick_protect.json', self.nick_data)
        status = "Enabled" if self.nick_data[str(ctx.message.guild.id)] else "Disabled"
        await ctx.send(self.bot.bot_prefix + '{} nickprotect for this server.'.format(status))

    async def on_member_update(self, before, after):
        if after.id != self.bot.user.id or before.id != self.bot.user.id or before.nick == after.nick:
            return
        if str(before.guild.id) not in self.nick_data:
            self.nick_data[str(before.guild.id)] = False
            dataIO.save_json('settings/nick_protect.json', self.nick_data)
        if self.nick_data[str(before.guild.id)] is True:
            if self.allowed:
                self.allowed = False
                return
            try:
                me = before.guild.get_member(self.bot.user.id)
                self.allowed = True
                await me.edit(nick=before.nick, password=None)
                print("Someone tried to change my nickname from \"{}\" to \"{}\" on server \"{}\"!".format(before.nick, after.nick, before.guild.name))
            except discord.Forbidden:
                print("Cannot protect nickname. Not enough permissions. \"{}\" on server \"{}\"".format(before.nick, before.guild.name))


def setup(bot):
    bot.add_cog(NickProtect(bot))
