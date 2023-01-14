import discord
import hexacolors
from discord.ext import commands
from funcs.defs import translates

async def  help0(selfbot: commands.Bot, Interaction: discord.Interaction):

    t: dict = translates(Interaction.guild)

    m: discord.Embed = discord.Embed(title = t['help']['extras']['commands'],
                description = t['help']['mod']['description'],
                color = hexacolors.stringColor('indigo'))

    m.add_field(
        name = t['help']['mod']['name1'],
        value = t['help']['mod']['content'],
        inline = False)
    m.set_thumbnail(url = f'{selfbot.user.avatar}')

    await Interaction.response.edit_message(embed = m)

async def help1(selfbot: commands.Bot, Interaction: discord.Interaction):

    t: dict = translates(Interaction.guild)

    g: discord.Embed = discord.Embed(title = t['help']['extras']['commands'],
                color = hexacolors.stringColor('indigo'))

    g.add_field(
        name = t['help']['general']['description'],
        value = t['help']['general']['content'],
        inline = False)
    g.set_thumbnail(url = f'{selfbot.user.avatar}')

    await Interaction.response.edit_message(embed=g)

async def help2(selfbot: commands.Bot, Interaction: discord.Interaction):

    t: dict = translates(Interaction.guild)

    e: discord.Embed = discord.Embed(title = t['help']['extras']['commands'],
                color = hexacolors.stringColor('indigo'))

    e.add_field(
        name = t['help']['economy']['description'], 
        value = t['help']['economy']['content'],
        inline = False)
    e.set_thumbnail(url = f'{selfbot.user.avatar}')

    await Interaction.response.edit_message(embed=e)

async def help3(selfbot: commands.Bot, Interaction: discord.Interaction):

    t: dict = translates(Interaction.guild)

    s: discord.Embed = discord.Embed(title = t['help']['extras']['commands'],
                color = hexacolors.stringColor('indigo'))

    s.add_field(
        name = t['help']['suport']['description'], 
        value = t['help']['suport']['content'],
        inline = False)
    s.set_thumbnail(url = f'{selfbot.user.avatar}')

    await Interaction.response.edit_message(embed=s)

async def help4(selfbot: commands.Bot, Interaction: discord.Interaction):

    t: dict = translates(Interaction.guild)

    i: discord.Embed = discord.Embed(title = t['help']['extras']['commands'],
                color = hexacolors.stringColor('indigo'))

    i.add_field(
        name= t['help']['image']['description'], 
        value = t['help']['image']['content'],
        inline = False)
    i.set_thumbnail(url = f'{selfbot.user.avatar}')

    await Interaction.response.edit_message(embed=i)

async def help5(selfbot: commands.Bot, Interaction: discord.Interaction):


    t: dict = translates(Interaction.guild)

    a: discord.Embed = discord.Embed(title = t['help']['extras']['commands'],
                color = hexacolors.stringColor('indigo'))

    a.add_field(
        name= t['help']['actions']['description'], 
        value = t['help']['actions']['content'],
        inline = False)
    a.set_thumbnail(url = f'{selfbot.user.avatar}')

    await Interaction.response.edit_message(embed=a)

