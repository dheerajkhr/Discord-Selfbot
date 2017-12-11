import aiohttp
import random
import discord
from datetime import datetime
from discord.ext import commands

'''Module for getting random Dad jokes'''


class DadJoke:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def dadjoke(self, ctx, joke_id : str = None):
        """Get a random dad joke"""
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Cog for appuselfbot for discord',
        }

        r = lambda: random.randint(0,255)

        base_url = "https://icanhazdadjoke.com"
        if joke_id:
            joke_url = "j/{0}".format(joke_id)
        else:
            joke_url = ""

        session = aiohttp.ClientSession(loop=self.bot.loop)
        resp = await session.get("{base_url}/{joke_url}".format(base_url=base_url, joke_url=joke_url), headers=headers)
        result = await resp.json()
        if result['status'] != 200:
            return

        embed_args = {
            'title': "Dad Joke",
            'url': "{base_url}/j/{id}".format(base_url=base_url, **result),
            'description': "{joke}".format(**result),
            'colour': discord.Colour.from_rgb(r(), r(), r()),
            'timestamp': datetime.utcnow(),
        }
        embed = discord.Embed(**embed_args)
        embed.set_footer(text="{id}".format(**result))

        await ctx.send(embed=embed)
        await ctx.message.delete()
        session.close()

def setup(bot):
    bot.add_cog(DadJoke(bot))
