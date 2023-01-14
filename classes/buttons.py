import discord
import requests
import hexacolors

from discord import Interaction, ButtonStyle
from discord.ui import button,Button, View
from .inputText import perfil
from db.economy import *
from funcs.defs import translates

class changeavatar(discord.ui.View):

    def __init__(self, ctx: discord.User, member: discord.Member):

        self.member: discord.Member = member

        self.ctx: discord.User = ctx

        super().__init__(timeout = 180, disable_on_timeout = True)

    @discord.ui.button(label = 'User Avatar',style = discord.ButtonStyle.blurple)
    async def useravatar(self, button: discord.ui.Button, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)

        if interaction.user.id != self.ctx.id:
            return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

        member = self.member
        embed: discord.Embed = discord.Embed(title = f'Avatar {member}', 
        description = f'[{t["args"]["avatar"]["click1"]}]({member.avatar}) {t["args"]["avatar"]["click2"]}')
        embed.set_image(url = f'{member.avatar}')
        await interaction.response.edit_message(embed = embed, view = guildavatar(self.ctx,member))

class guildavatar(discord.ui.View):

    def __init__(self, ctx: discord.User, member: discord.Member):

        self.member: discord.Member = member

        self.ctx: discord.User = ctx

        super().__init__(timeout = 180, disable_on_timeout = True)

    @discord.ui.button(label = 'guild Avatar',style = discord.ButtonStyle.blurple)
    async def useravatar(self, button: discord.ui.Button, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)

        if interaction.user.id != self.ctx.id:
            return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

        member = self.member
        embed: discord.Embed = discord.Embed(title = f'Avatar {member}', 
        description = f'[{t["args"]["avatar"]["click1"]}]({member.guild_avatar}) {t["args"]["avatar"]["click2"]}')
        embed.set_image(url = f'{member.guild_avatar}')
        await interaction.response.edit_message(embed = embed, view = changeavatar(self.ctx,member))

class profile(View):
    
    def __init__(self,ctx):

        self.ctx: discord.Member = ctx

        super().__init__(timeout = 300)

    @button(label = 'Edit', style = ButtonStyle.blurple)
    async def perfil(self, button: Button, interaction: Interaction):

        if interaction.user.id == self.ctx.id:
            await interaction.response.send_modal(perfil(interaction.user))

class KissButton(View):
    
    def __init__(self, member, ctx):

        self.member: discord.Member = member

        self.ctx: discord.Member = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def kiss(self, button: Button, interaction: Interaction):
        
        try:
            t: dict = translates(interaction.guild)
            if interaction.user.id != self.member.id:
                return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)
            res: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=kiss&format=gif').json()
            kiss2: discord.Embed = discord.Embed(title = t["args"]["actions"]["kiss"],
            description = t["args"]["actions"]["actionkiss"].format(self.member.mention, self.ctx.mention) ,
            color = hexacolors.stringColor('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()
        except Exception as error:
            print(error)

class HugButton(View):
    
    def __init__(self, member, ctx):

        self.member: discord.Member = member

        self.ctx: discord.Member = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def abraço(self, button: Button, interaction: Interaction):

        try:
            t: dict = translates(interaction.guild)
            if interaction.user.id != self.member.id:
                return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)
            t: dict = translates(interaction.guild)
            res: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=hug&format=gif').json()
            kiss2: discord.Embed = discord.Embed(title = t["args"]["actions"]["hug"],
            description = t["args"]["actions"]["actionhug"].format(self.member.mention, self.ctx.mention),
            color = hexacolors.stringColor('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()
        except Exception as error:
            print(error)

class SlapButton(View):
    
    def __init__(self, member, ctx):

        self.member: discord.Member = member

        self.ctx: discord.Member = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def tapa(self, button: Button, interaction: Interaction):
        
        try:
            t: dict = translates(interaction.guild)
            if interaction.user.id != self.member.id:
                return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)
            res: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=slap&format=gif').json()
            kiss2: discord.Embed = discord.Embed(title = t["args"]["actions"]["slap"],
            description = t["args"]["actions"]["actionslap"].format(self.member.mention, self.ctx.mention),
            color = hexacolors.stringColor('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()
        except Exception as error:
            print(error)

class punchButton(View):
    
    def __init__(self, member, ctx):

        self.member: discord.Member = member

        self.ctx: discord.Member = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def soco(self, button: Button, interaction: Interaction):
        
        try:
            t: dict = translates(interaction.guild)
            if interaction.user.id != self.member.id:
                return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)
            res: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=punch&format=gif').json()
            kiss2: discord.Embed = discord.Embed(title = t["args"]["actions"]["punch"],
            description = t["args"]["actions"]["actionpunch"].format(self.member.mention,self.ctx.mention),
            color = hexacolors.stringColor('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()
        except Exception as error:
            print(error)

class biteButton(View):
    
    def __init__(self, member, ctx):

        self.member: discord.Member = member

        self.ctx: discord.Member = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def moder(self, button: Button, interaction: Interaction):
        
        try:
            t: dict = translates(interaction.guild)
            if interaction.user.id != self.member.id:
                return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)
            res: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=bite&format=gif').json()
            kiss2: discord.Embed = discord.Embed(title = t["args"]["actions"]["bite"],
            description = t["args"]["actions"]["actionbite"].format(self.member.mention, self.ctx.mention),
            color = hexacolors.stringColor('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()
        except Exception as error:
            print(error)

class patButton(View):
    
    def __init__(self, member, ctx):

        self.member: discord.Member = member

        self.ctx: discord.Member = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def cafune(self, button: Button, interaction: Interaction):
        
        try:
            t: dict = translates(interaction.guild)
            if interaction.user.id != self.member.id:
                return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)
            res: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=pat&format=gif').json()
            kiss2: discord.Embed = discord.Embed(title = t["args"]["actions"]["pat"],
            description = t["args"]["actions"]["actionpat"].format(self.member.mention, self.ctx.mention),
            color = hexacolors.stringColor('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()
        except Exception as error:
            print(error)

class lickButton(View):
    
    def __init__(self, member, ctx):

        self.member: discord.Member = member

        self.ctx: discord.Member = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def lambida(self, button: Button, interaction: Interaction):
        
        try:
            t: dict = translates(interaction.guild)
            if interaction.user.id != self.member.id:
                return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)
            res: requests = requests.get('https://api.otakugifs.xyz/gif?reaction=lick&format=gif').json()
            kiss2: discord.Embed = discord.Embed(title = t["args"]["actions"]["lick"],
            description = t["args"]["actions"]["actionlick"].format(self.member.mention,self.ctx.mention),
            color = hexacolors.stringColor('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()
        except Exception as error:
            print(error)