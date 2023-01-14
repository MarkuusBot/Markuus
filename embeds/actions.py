import discord, hexacolors
from discord.ext import commands
import requests
from classes.buttons import HugButton, KissButton, SlapButton, biteButton, patButton, lickButton, punchButton
from funcs.defs import translates

async def kissEmbed(selfbot: commands.Bot, Interaction: discord.Interaction, author: discord.Member, member: discord.Member):

    requestKissGif: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=kiss&format=gif').json()["url"]

    t: dict = translates(Interaction.guild)

    match member.id:

        case selfbot.user.id:

            await Interaction.response.send_message(f'{t["args"]["actions"]["notkiss"]}')
        
        case author.id:

            e: discord.Embed = discord.Embed(title = t["args"]["actions"]["kiss"],
                description=t["args"]["actions"]["actionkissself"].format(author.mention),
                color = hexacolors.stringColor('pink')
            )
            e.set_image(url = requestKissGif)

            await Interaction.response.send_message(embed = e)
        
        case _:

            e: discord.Embed = discord.Embed(title = t["args"]["actions"]["kiss"],
                description=t["args"]["actions"]["actionkiss"].format(author.mention, member.mention),
                color = hexacolors.stringColor('pink')
            )
            e.set_image(url = requestKissGif)

            e.set_footer(text = t["args"]["actions"]["return"])

            await Interaction.response.send_message(content = member.mention ,embed = e, view = KissButton(member,Interaction.user))

async def slapEmbed(selfbot: commands.Bot, Interaction: discord.Interaction, author: discord.Member, member: discord.Member):

    requestSlapGif: requests = requests.get("https://api.otakugifs.xyz/gif?reaction=slap&format=gif").json()["url"]

    t: dict = translates(Interaction.guild)

    match member.id:

        case selfbot.user.id:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["slap"],
                description = t["args"]["actions"]["actionslap"].format(member.mention, author.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestSlapGif)

            await Interaction.response.send_message(embed = e)
        
        case author.id:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["slap"],
                description = t["args"]["actions"]["actionslapself"].format(author.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestSlapGif)

            await Interaction.response.send_message(embed = e)
        
        case _:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["slap"],
                description = t["args"]["actions"]["actionslap"].format(author.mention,member.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestSlapGif)
            
            e.set_footer(text = t["args"]["actions"]["return"])

            await Interaction.response.send_message(content = member.mention ,embed = e, view = SlapButton(member, author))

async def hugEmbed(selfbot: commands.Bot, Interaction: discord.Interaction, author: discord.Member, member: discord.Member):

    requestHugGif: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=hug&format=gif').json()["url"]

    t: dict = translates(Interaction.guild)

    match member.id:

        case selfbot.user.id:

            await Interaction.response.defer()

            e: discord.Embed = discord.Embed(title = t["args"]["actions"]["hug"],
            description = t["args"]["actions"]["actionhug"].format(Interaction.user.mention, member.mention),
            color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestHugGif)
            e.set_footer(text = t["args"]["actions"]["return"])

            await Interaction.followup.send(embed = e, view = HugButton(member, Interaction.user))

            e: discord.Embed = discord.Embed(title = t["args"]["actions"]["hug"],
            description = t["args"]["actions"]["actionhug"].format(member.mention,Interaction.user.mention),
            color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestHugGif)
            e.set_footer(text = t["args"]["actions"]["return"])

            await Interaction.followup.send(embed = e)
        
        case author.id:

            e: discord.Embed = discord.Embed(title = t["args"]["actions"]["hug"],
            description = t["args"]["actions"]["actionhugself"].format(selfbot.user.mention,Interaction.user.mention),
            color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestHugGif)

            await Interaction.response.send_message(embed = e)

        case _:

            e: discord.Embed = discord.Embed(title = t["args"]["actions"]["hug"],
            description = t["args"]["actions"]["actionhug"].format(Interaction.user.mention, member.mention),
            color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestHugGif)
            e.set_footer(text = t["args"]["actions"]["return"])

            await Interaction.response.send_message(content = member.mention ,embed = e, view = HugButton(member, Interaction.user))

async def punchEmbed(selfbot: commands.Bot, Interaction: discord.Interaction, author: discord.Member, member: discord.Member):

    t: dict = translates(Interaction.guild)

    requestPunchGif: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=punch&format=gif').json()["url"]

    match member.id:

        case selfbot.user.id:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["punch"],
                description = t["args"]["actions"]["actionpunch"].format(member.mention, author.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestPunchGif)

            await Interaction.response.send_message(embed = e)
        
        case author.id:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["punch"],
                description = t["args"]["actions"]["actionpunchself"].format(author.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestPunchGif)

            await Interaction.response.send_message(embed = e)
        
        case _:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["punch"],
                description = t["args"]["actions"]["actionpunch"].format(author.mention,member.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestPunchGif)
            
            e.set_footer(text = t["args"]["actions"]["return"])

            await Interaction.response.send_message(content = member.mention ,embed = e, view = punchButton(member, author))

async def biteEmbed(selfbot: commands.Bot, Interaction: discord.Interaction, author: discord.Member, member: discord.Member):

    requestBiteGif: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=bite&format=gif').json()["url"]

    t: dict = translates(Interaction.guild)

    match member.id:

        case selfbot.user.id:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["slap"],
                description = t["args"]["actions"]["actionslap"].format(member.mention, author.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requests.get('https://api.otakugifs.xyz/gif?reaction=slap&format=gif').json()["url"])

            await Interaction.response.send_message(embed = e)
        
        case author.id:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["bite"],
                description = t["args"]["actions"]["actionbiteself"].format(author.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestBiteGif)

            await Interaction.response.send_message(embed = e)
        
        case _:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["bite"],
                description = t["args"]["actions"]["actionbite"].format(author.mention, member.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestBiteGif)

            await Interaction.response.send_message(content = member.mention ,embed = e, view = biteButton(member, author))

async def lickEmbed(selfbot: commands.Bot, Interaction: discord.Interaction, author: discord.Member, member: discord.Member):

    requestLickGif: requests = requests.get("https://api.otakugifs.xyz/gif?reaction=lick&format=gif").json()["url"]

    t: dict = translates(Interaction.guild)

    match member.id:

        case selfbot.user.id:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["slap"],
                description = t["args"]["actions"]["actionslap"].format(member.mention, author.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requests.get('https://api.otakugifs.xyz/gif?reaction=slap&format=gif').json()["url"])

            await Interaction.response.send_message(embed = e)
        
        case author.id:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["lick"],
                description = t["args"]["actions"]["actionlickself"].format(author.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestLickGif)

            await Interaction.response.send_message(embed = e)
        
        case _:

            e: discord.Embed = discord.Embed(
                title = t["args"]["actions"]["lick"],
                description = t["args"]["actions"]["actionlick"].format(author.mention, member.mention),
                color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestLickGif)

            await Interaction.response.send_message(content = member.mention ,embed = e, view = lickButton(member, author))

async def cafuneEmbed(selfbot: commands.Bot, Interaction: discord.Interaction, author: discord.Member, member: discord.Member):

    requestpatGif: requests = requests.get("https://api.otakugifs.xyz/gif?reaction=pat&format=gif").json()["url"]

    t: dict = translates(Interaction.guild)

    match member.id:

        case selfbot.user.id:

            await Interaction.response.defer()

            e: discord.Embed = discord.Embed(title = t["args"]["actions"]["pat"],
            description = t["args"]["actions"]["actionpat"].format(Interaction.user.mention, member.mention),
            color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestpatGif)
            e.set_footer(text = t["args"]["actions"]["return"])

            await Interaction.followup.send(embed = e, view = patButton(member, Interaction.user))

            e: discord.Embed = discord.Embed(title = t["args"]["actions"]["pat"],
            description = t["args"]["actions"]["actionpat"].format(member.mention,Interaction.user.mention),
            color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestpatGif)
            e.set_footer(text = t["args"]["actions"]["return"])

            await Interaction.followup.send(embed = e)
        
        case author.id:

            e: discord.Embed = discord.Embed(title = t["args"]["actions"]["pat"],
            description = t["args"]["actions"]["actionpatself"].format(selfbot.user.mention,Interaction.user.mention),
            color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestpatGif)

            await Interaction.response.send_message(embed = e)

        case _:

            e: discord.Embed = discord.Embed(title = t["args"]["actions"]["pat"],
            description = t["args"]["actions"]["actionpat"].format(Interaction.user.mention, member.mention),
            color = hexacolors.stringColor('indigo')
            )
            e.set_image(url = requestpatGif)
            e.set_footer(text = t["args"]["actions"]["return"])

            await Interaction.response.send_message(content = member.mention ,embed = e, view = patButton(member, Interaction.user))