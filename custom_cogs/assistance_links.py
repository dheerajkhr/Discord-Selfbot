import discord
import re
from discord.ext import commands

'''General commands to use for 3DS assistance.'''


class AssistanceLinks:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pinfo'])
    async def information(self, ctx):
        """About this cog"""
        await ctx.message.delete()
        embed = discord.Embed(title="What is this cog for?")
        embed.set_author(name="PhazonicRidley#1432 (main dev) and Griffin#2329 (fixer of mistakes -.-)")
        embed.description = "The purpose of this cog is to quickly provide useful links on the 3DS Homebrew discord server."
        embed.add_field(name="Where can I download this?", value="You can download it from the github [here](https://github.com/PhazonicRidley/Assistance-Links).")
        await ctx.send(embed=embed)

    @commands.command()
    async def ub9s(self, ctx):
        """Boot9Strap Update Link"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to Update Boot9Strap", color=1710847)
        embed.description = "You can use [this](https://3ds.guide/updating-b9s) guide to update b9s to the latest version."
        embed.set_author(name="Plailect")
        embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/16979510?v=48&s=500")
        await ctx.send(embed=embed)

    @commands.command(aliases=['atob'])
    async def ua9lh(self, ctx):
        """Arm9LoaderHax to Boot9Strap Update Link"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to Update from Arm9LoaderHax to Boot9Strap", color=16718362)
        embed.description = "You can use [this](https://3ds.guide/a9lh-to-b9s) guide to update from A9LH to B9S."
        embed.set_author(name="Plailect")
        embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/16979510?v=48&s=500")
        await ctx.send(embed=embed)

    @commands.command()
    async def region(self, ctx):
        """How to change 3DS Region"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to Change your 3DS' Region", color=16750848)
        embed.description = "You can use [this](https://3ds.guide/region-changing) guide to change your 3DS' region."
        embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/16979510?v=48&s=500")
        embed.set_author(name="Plailect")
        await ctx.send(embed=embed)

    @commands.command()
    async def luma(self, ctx, *, msg = ""):
        """Links to Luma3ds. You can input a version number after the command to output a specific version."""
        if msg == "hourly" or msg == "hourlies":
            embed = discord.Embed(title="Luma3DS Hourlies", color=65535)
            embed.description = "You can get the Luma3DS hourlies [here](https://astronautlevel2.github.io/Luma3DS). Please keep in mind these are not always stable, and you use these at your own risk."
            embed.set_thumbnail(url="https://gbatemp.net/attachments/Luma3DSalt-png.46691/")
            embed.set_author(name="Aurora Wright")
            return await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            if msg:
                pattern = re.compile("\d\.\d\.?\d?")
                if pattern.match(msg):
                    embed = discord.Embed(title="Luma3DS v" + msg, color=65535)
                    embed.description = "You can download Luma3DS v{} from [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v{}).".format(msg, msg)
                    embed.set_author(name = "Aurora Wright")
                    embed.set_thumbnail(url="https://gbatemp.net/attachments/Luma3DSalt-png.46691/")
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(self.bot.bot_prefix + "Wrong format of version given")
            else:
                embed = discord.Embed(title="Luma3DS Download Link", color=65535)
                embed.description = "You can download Luma3DS below."
                embed.set_author(name="Aurora Wright")
                embed.add_field(name="Latest Luma", value="You can always get the absolute latest version of Luma3DS [here](https://github.com/AuroraWright/Luma3DS/releases/latest). Please keep in mind you will need the latest version of B9S to be able to use it.")
                await ctx.send(embed=embed)

    @commands.command()
    async def terms(self,ctx):
        """Link to Zeta's website; the information tab"""
        await ctx.message.delete()
        embed = discord.Embed(title="3DS Hacking Terms", color=52224)
        embed.description ="You can read [here](https://zetadesigns.github.io/info.html) for information about 3DS hacking."
        embed.set_author(name="Zeta")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/186474714124910592/6c0bd4dc9c043fe35c4b5f08dcdfaa80.webp?width=250&height=250")
        await ctx.send(embed=embed)

    @commands.group()
    async def randomize(self,ctx):
        """Pokemon randomizing guides"""
        if ctx.invoked_subcommand is None:
            await ctx.message.delete()
            embed = discord.Embed(title="How to Randomize Pokemon Games", color=10079487)
            embed.description = "These guides will help you randomize your pokemon game."
            embed.set_author(name="Slade and Zeta")
            embed.add_field(name="Randomizing a Pokemon game (CIA)",value="Use [this](https://zetadesigns.github.io/randomizing-cia.html) guide if you want to randomize a pokemon game then install it.")
            embed.add_field(name="Randomizing a Pokemon game (LayeredFS)", value="Use [this](https://zetadesigns.github.io/randomizing-layeredfs.html) guide if want to randomize a pokemon game without reinstalling it.")
            embed.set_thumbnail(url="http://i.imgur.com/eJfVxZv.png")
            await ctx.send(embed=embed)

    @randomize.command()
    async def cia(self, ctx):
        """Randomize a Pokemon game via CIA"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to Randomize A Pokemon Game as a CIA", color=10079487)
        embed.set_author(name="Slade and Zeta")
        embed.description = "Use [this](https://zetadesigns.github.io/randomizing-cia.html) guide if you want to randomize a pokemon game then install it."
        embed.set_thumbnail(url="http://i.imgur.com/eJfVxZv.png")
        await ctx.send(embed=embed)

    @randomize.command()
    async def lfs(self, ctx):
        """Randomize a Pokemon game via CIA"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to Randomize A Pokemon Game Using LayeredFS", color=10079487)
        embed.set_author(name="Slade and Zeta")
        embed.description = "Use [this](https://zetadesigns.github.io/randomizing-layeredfs.html) guide if want to randomize a pokemon game without reinstalling it."
        embed.set_thumbnail(url="http://i.imgur.com/eJfVxZv.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def prism(self, ctx):
        """How to inject Pokemon Prism saves"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to Inject Pokemon Prism Saves", color=10079487)
        embed.description = "You can use [this](https://zetadesigns.github.io/injecting_prism.html) guide to inject pokemon prism saves."
        embed.set_thumbnail(url="http://i.imgur.com/eJfVxZv.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def ct(self,ctx):
        """Cthulhu/Cashe Tool guide and download link"""
        await ctx.message.delete()
        embed = discord.Embed(title="What is Cthulhu/CacheTool?", color=993399)
        embed.description = "Cthulhu is a multipurpose tool for home menu and activity log manipulation."
        embed.add_field(name="Where can I download Cthulhu/CacheTool?", value="You can download Cthulhu/CacheTool [here](https://github.com/Ryuzaki-MrL/CacheTool/releases/tag/1.3.2). You can also download it from \nFBI > TitleDB, where it is listed simply as \"Cthulhu\".")
        embed.add_field(name="How do I use it?", value="You can use [this](https://zetadesigns.github.io/cthulhu-usage.html) guide for basic use of Cthulhu/CacheTool.")
        embed.set_author(name="Slade and Zeta (guide), Lázaro Vieira (Cthulhu)")
        await ctx.send(embed=embed)

    @commands.command(aliases=['fcp'])
    async def flashcartpic(self,ctx):
        """Compatibility list for what flashcarts do and do not work for ntrboot"""
        await ctx.message.delete()
        embed = discord.Embed(title="Compatibility List for NTRBoot")
        embed.description = "Only the flashcarts on the left can currently be used for NTRBoot. If your flashcart does not look exactly like one of those, it can not currently be used for NTRBoot."
        embed.set_image(url="https://raw.githubusercontent.com/PhazonicRidley/Assistance-Links/master/Flashcard%20pic.jpg")
        embed.set_author(name="EdTheNerd (Creator), Jisagi (Editor)")
        await ctx.send(embed=embed)

    @commands.command(aliases=['gm9'])
    async def godmode9(self,ctx):
        """Godmod9 download link"""
        await ctx.message.delete()
        embed = discord.Embed(title="GodMode9 Download Link", color=13395711)
        embed.description = "Click [here](https://github.com/d0k3/GodMode9/releases) for the latest release of GodMode9"
        embed.set_author(name="d0k3")
        embed.set_thumbnail(url="https://avatars2.githubusercontent.com/u/12467483?v=4&s=460")
        await ctx.send(embed=embed)

    @commands.command()
    async def fbi(self,ctx):
        """FBI download link"""
        await ctx.message.delete()
        embed = discord.Embed(title="FBI Download Link", color=16777215)
        embed.description = "Click [here](https://github.com/Steveice10/FBI/releases) for the latest version of FBI."
        embed.set_author(name="Steveice10")
        embed.set_thumbnail(url="https://avatars2.githubusercontent.com/u/1269164?v=4&s=460")
        await ctx.send(embed=embed)

    @commands.command(aliases=['db9s'])
    async def boot9strap(self, ctx):
        """Boot9strap Download Link"""
        await ctx.message.delete()
        embed = discord.Embed(title="Boot9strap Download Link", color=59110)
        embed.description = "Click [here](https://github.com/SciresM/boot9strap/releases/download/1.2/boot9strap-1.2.zip) for a direct link for the normal version of boot9strap."
        embed.set_author(name="SciresM")
        await ctx.send(embed=embed)

    @commands.command(aliases=['theme'])
    async def anemone(self,ctx):
        """Anemone download link"""
        await ctx.message.delete()
        embed = discord.Embed(title="How can I Install Custom Themes?", color=9699539)
        embed.description = "You can get Anemone [here](https://github.com/astronautlevel2/Anemone3DS/releases/latest). You can get themes from [Theme Plaza](https://themeplaza.eu/themes) or the [3dsthem.es Archive](http://3dsthemesarchive.site/?type=themes)."
        embed.set_author(name="astronautlevel2 and daedreth")
        embed.set_thumbnail(url="https://github.com/astronautlevel2/Anemone3DS/raw/master/meta/banner.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def jksm(self,ctx):
        """JKSM Download Links"""
        await ctx.message.delete()
        embed = discord.Embed(title="JKSM Download Links", color=16777215)
        embed.description = "You can download the CIA version of JSKM [here](https://github.com/J-D-K/JKSM/raw/master/JKSM.cia), the 3dsx/hax version [here](https://github.com/J-D-K/JKSM/raw/master/JKSM.3dsx), or the Rosalina compatible 3dsx [here](https://github.com/Phalk/JKSM/releases/latest)."
        embed.set_author(name="J-D-K")
        await ctx.send(embed=embed)

    @commands.command(aliases=['sc'])
    async def stockchart(self,ctx):
        """CFW Installation Options"""
        await ctx.message.delete()
        embed = discord.Embed(title="What are my Options for Installing CFW?")
        embed.description = "Here is a visual chart on your CFW installing options for 11.4 and up:"
        embed.set_image(url="https://cdn.discordapp.com/attachments/346830960668573697/366625577085435924/3DS_11.4_Flowchart.png")
        embed.set_author(name="Aluminite")
        await ctx.send(embed=embed)

    @commands.command(aliases=['cards'])
    async def ndscard(self,ctx):
        """Information on flashcarts"""
        await ctx.message.delete()
        embed = discord.Embed(title="Where Should I buy my Flashcards from?", color=58995)
        embed.description = "We recommend that you buy flashcards from [this](http://www.nds-card.com/) site. They are trusted and reliable. Please note that they must be paid via PayPal or Western Union.\nIf you are buying a flashcard for NTRBoot, the [R4i GOLD 3DS RTS](http://www.nds-card.com/proshow.asp?PageNo=2&ProID=149) is recommended."
        await ctx.send(embed=embed)

    @commands.command(aliases=['pins'])
    async def readpins(self,ctx):
        """READ!! THE!! PINS!!"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to Check Pins")
        embed.add_field(name="On PC:", value="Press Ctrl+P (Cmd+P on Mac) or press the pin icon at the top right of the window.")
        embed.add_field(name="On iOS/Android:", value="Tap the channel name at the top (or the three dots next to it on some phones) and press Pinned Messages.")
        embed.set_image(url="https://raw.githubusercontent.com/PhazonicRidley/Assistance-Links/master/pins.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=['ni'])
    async def ntrinfo(self,ctx):
        """Best cards for NTRBoot"""
        await ctx.message.delete()
        embed = discord.Embed(title="Flashcart Purchase Guide")
        embed.add_field(name="Which flashcarts are recommended for NTRBoot on an unhacked 11.4+ 3DS?", value="The cheapest NTRBoot compatible DS flashcart is the [R4 SDHC Gold Pro 2017](http://nds-card.com/ProShow.asp?ProID=490) which costs $10. After that, the general purpose recommended 3DS flashcart which also supports NTRBoot is the [R4i 3DS RTS Gold](http://nds-card.com/ProShow.asp?ProID=149) which costs $20")
        embed.add_field(name="So which do I buy?", value="The SDHC 2017 is, unfortunately, a timebomb. This means that in a couple years, the card will stop working (unless you set the date back to 2017). This does not affect NTRBoot usage. The RTS Gold is not a timebomb, so it's the better choice if you want one to play games with.") 
        await ctx.send(embed=embed)

    @commands.command()
    async def ntrflasher(self,ctx):
        """Ntrboot Flasher"""
        await ctx.message.delete()
        embed = discord.Embed(title="NTRBoot Flasher", color=26112)
        embed.description = "If you are looking to install CFW on your system using NTRBoot with only one console, you will need to download [this](https://github.com/kitling/ntrboot_flasher) flasher and extract it to the root of your flashcart's microSD card."
        await ctx.send(embed=embed)

    @commands.command(aliases=['bw'])
    async def banwaveinfo(self,ctx):
        """More Banwave Info"""
        await ctx.message.delete()
        embed = discord.Embed(title="Banwave Info")
        embed.description = "There has been a banwave by Nintendo. While unbanning is not supported here, these steps may help you *prevent* a ban. For more info, please see pinned message in <#225556031428755456>."
        embed.add_field(name="How to **Possibly** Prevent your 3DS from being Banned", value= """**1.** TURN OFF WIFI\n**2.** Go to Friend List, click Settings in the corner of the screen, go to settings, and DISABLE Share Currently Playing Game. and blank your Favorite Game.\n**3.** Go to System Settings -> Internet Settings -> SpotPass -> Sending of System Information; turn it OFF.\n**4.** Optionally, avoid running homebrew from, or installing it to, the Home Menu, as a CIA. Use Rosalina or the Homebrew Launcher instead.""")
        embed.set_image(url="https://cdn.discordapp.com/attachments/225556031428755456/324359937201405952/avoid-the-noid-he-ruins-pizzas.png")
        await ctx.send(embed=embed)

    """@commands.command()
    async def fcp2(self,ctx):
        """"""A second flashcard pic""""""
        await ctx.message.delete()
        embed = discord.Embed(title="Compatibility List for NTRBoot")
        embed.description = "Here is more of a breakdown of the flashcards that can be used for NTRBoot."
        embed.set_author(name="xCasey")
        embed.set_image(url="")
        await ctx.send(embed=embed)""" #Commented out until a non-discord link is given

    @commands.command()
    async def ftpd(self,ctx):
        """A download link to ftpd"""
        await ctx.message.delete()
        embed = discord.Embed(title="FTPD, a FTP Server for the 3DS", color=16757759)
        embed.description = "Click [here](https://github.com/mtheall/ftpd) to download FTPD."
        embed.set_author(name="mtheall")
        embed.set_thumbnail(url="https://avatars2.githubusercontent.com/u/896483?s=460&v=4")
        await ctx.send(embed=embed)

    @commands.command(aliases=['tbi'])
    async def timebombinfo(self,ctx):
        """Some info on Timebomb flashcards"""
        await ctx.message.delete()
        embed = discord.Embed(title="What is a Timebomb(ed) Flashcart?")
        embed.description = "A timebomb flashcart is a flashcart that will stop working after a certain year. You can bypass this by changing your console's date backwards."
        await ctx.send(embed=embed)

    """@commands.command()
    async def asschan(self,ctx):
        """"""Tell people to stay on topic in the help chats""""""
        await ctx.message.delete()
        embed = discord.Embed(title="You seem to be in an assistance channel!", color=16777215)
        embed.description = "Please leave memes, shitposts, and other non assistance to the other channels."
        await ctx.send(embed=embed)""" #Commented out because jfc this is really idiotic.

    @commands.command(aliases=['eol'])
    async def endoflife(self,ctx):
        """Inform on Frii Exploits"""
        await ctx.message.delete()
        embed = discord.Embed(title="When can I Hack my 3DS for Free?")
        embed.description = "Assume not until 3DS End of Life in 2019, as 3DS hackers such as yellows8, nedwill, and smealum are keeping their exploits secret to prevent patching."
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['mg'])
    async def magnetguide(self,ctx):
        """NTRBoot Magnet Guide"""
        await ctx.message.delete()
        embed = discord.Embed(title="Where do I put the Magnet?", color=0)
        embed.description = "Place your magnet in the area marked by the X in the below image"
        embed.set_image(url="https://cdn.discordapp.com/attachments/377995740372533249/378014117664915456/ekEYDsalQyaFjzjjlXnUow.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=['hm'])
    async def hardmods(self,ctx):
        """List of hardmodders"""
        await ctx.message.delete()
        embed = discord.Embed(title="How can I get my 3DS Hardmodded?")
        embed.description = "You can do it yourself, though this is not advised as you risk destroying your 3DS without proper experience. The other option is to request a hardmod from one of the trusted hardmodders [here](http://pastebin.com/wNr42PtH)."
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AssistanceLinks(bot))
