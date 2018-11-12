from discord.ext import commands


class Discriminator:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def discriminator(self, ctx, *, current_discriminator='discriminator'):
        '''Checks all users the bot has access to if they share a discriminator, then posts all the resulting discriminators.

        It is possible to optionally specify a discriminator to match, otherwise your own discriminator is used.'''
        # CREDITS: Appu's selfbot discord for the original script.
        if current_discriminator is 'discriminator' or not (current_discriminator.isdigit() and len(current_discriminator) is 4):
            current_discriminator = ctx.author.discriminator
        all_users = ', '.join(list(set([str(m) for m in self.bot.get_all_members() if m.discriminator == current_discriminator])))
        if all_users:
            await ctx.send(content='All users I could find with discriminator {0}: \n```{1}```'.format(current_discriminator, all_users))
        else:
            await ctx.send(content='Could not find any users with discriminator {0}'.format(current_discriminator))


def setup(bot):
    bot.add_cog(Discriminator(bot))
