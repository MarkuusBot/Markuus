import requests
import hexacolors
import discord as discord

from PIL import ImageDraw, ImageFont, Image
from PIL.ImageFont import FreeTypeFont
from io import BytesIO
from db.moderation import mod
from discord.ext import commands
from funcs.defs import better_time, translates
from funcs.checks import moduleCheck, vote, NoVote
from discord import Asset, slash_command, option

class images(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(name = 'wanted',
        guild_only = True,
        description = 'Create a wanted poster',
        name_localizations = {
            'en-US': 'wanted',
            'en-GB': 'wanted',
            'es-ES': 'búsqueda',
            'pt-BR': 'procurado',
            'fr': 'recherché'
        },
        description_localizations = {
            'en-US': 'Create a wanted poster',
            'en-GB': 'Create a wanted poster',
            'es-ES': 'Crear un cartel de búsqueda',
            'pt-BR': 'Cria um cartaz de procurado',
            'fr': 'Créer une affiche recherchée'
        }
    )
    @option(name = 'member', description = 'Mencione um membro')
    @vote()
    @moduleCheck('diverção')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def procurado(self, Interaction: discord.Interaction, member: discord.Member = None):

        if member == None: member = Interaction.user

        if mod.find_one({'_id':Interaction.guild.id})['lang'] != 'pt-br':

            procurado: Image = Image.open('./images/images/wanted.jpg')

            asset: Asset = member.avatar.replace(size = 128)

            data: BytesIO = BytesIO(await asset.read())

            pfp: Image = Image.open(data)

            pfp = pfp.resize((398,307))

            procurado.paste(pfp, (34,217))

            procurado.save('./images/img/Procurado.jpg')

            await Interaction.response.send_message(file = discord.File('./images/img/Procurado.jpg'))

            return

        procurado: Image = Image.open('./images/images/procurado.png')

        asset: Asset = member.avatar.replace(size = 128)

        data: BytesIO = BytesIO(await asset.read())

        pfp: Image = Image.open(data)

        pfp = pfp.resize((193,149))

        procurado.paste(pfp, (18,71))

        procurado.save('./images/img/Procurado.jpg')

        await Interaction.response.send_message(file = discord.File('./images/img/Procurado.jpg'))

    @slash_command(name = 'achievement_minecraft',
        guild_only = True,
        description = 'Create a achievement of minecraft',
        name_localizations = {
            'pt-BR': 'conquista_minecraft',
        },
        description_localizations = {
            'pt-BR': 'Cria uma conquista do minecraft',
        }
    )
    @option(name = 'item', description = 'Escolha o item da conquista')
    @option(name = 'line1', description = 'Escreva o titulo da conquista')
    @option(name = 'line2', description = 'Escreva a conquista')
    @vote()
    @moduleCheck('diverção')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def conquistamine(self ,Interaction: discord.Interaction, line1, line2):

        conquista1: Image = Image.open('./images/images/mineconquista.png').convert("RGBA")
    
        draw: ImageDraw = ImageDraw.Draw(conquista1)

        icons: Image = Image.open('./images/images/iconsminecraft/logo.png')

        icons = icons.resize((40,40)).convert("RGBA")

        font: FreeTypeFont = ImageFont.truetype("./images/fonts/Minecraft.ttf",size=18)

        draw.text((70,15), line1 ,font = font,fill=(255,255,0))

        draw.text((70,35), line2 ,font = font)

        conquista1.paste(icons,(20,20))

        conquista1.save('./images/img/conquista.png')

        await Interaction.response.send_message(file = discord.File('./images/img/conquista.png'))  

    @slash_command(name = 'perfection',
        guild_only = True,
        description = 'Cria um memme de "perfeição"',
        )
    @option(name = 'member', description = 'Mencione um membro')
    @vote()
    @moduleCheck('diverção')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def perfeição(self, Interaction: discord.Interaction, member: discord.Member = None):

        t: dict = translates(Interaction.guild)

        if member == None: member = Interaction.user

        perfeição: Image = Image.open('./images/images/perfeicao.jpeg')

        draw: ImageDraw = ImageDraw.Draw(perfeição)

        font: FreeTypeFont = ImageFont.truetype("./images/fonts/LeagueGothic-Regular-VariableFont_wdth.ttf",size=20)

        draw.text((9,6), t['args']['images']['perfection'] , fill= (0,0,0) ,font = font)
        
        asset: Asset = member.avatar.replace(size = 128)

        data: BytesIO = BytesIO(await asset.read())

        pfp: Image = Image.open(data)

        pfp = pfp.resize((150,150))

        perfeição.paste(pfp, (144,52))
        
        perfeição.save('./images/img/perfeicao.png')

        await Interaction.response.send_message(file = discord.File('./images/img/perfeicao.png'))

    @slash_command(name = 'cat',
        guild_only = True,
        description = 'Envia uma imagem de gato aleatoria',
        )
    @moduleCheck('diverção')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cat(self,Interaction: discord.Interaction):

        t: dict = translates(Interaction.guild)

        r: requests = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']

        cat: discord.Embed = discord.Embed(title = f"🐱{t['args']['images']['cat']}",
        color = hexacolors.stringColor('indigo'))
        cat.set_image(url = r)

        await Interaction.response.send_message(embed = cat)
    
    @slash_command(name = 'body_minecraft',
        guild_only = True,
        description = 'Envia o corpo de um player',
        )
    @option(name = 'player', description = 'Nickname')
    @moduleCheck('diverção')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def body(self, Interaction: discord.Interaction, player):

        t: dict = translates(Interaction.guild)

        try:

            r: requests = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await Interaction.response.send_message(f'https://crafatar.com/renders/body/{r.json()["id"]}/?size=128&overlay')
        
        except:

            await Interaction.response.send_message(t['args']['miecraft']['errorbody'])

    @slash_command(name = 'head_minecraft',
        guild_only = True,
        description = 'Envia a cabeça de um player',
        )
    @option(name = 'player', description = 'Nickname')
    @moduleCheck('diverção')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def head(self, Interaction: discord.Interaction, player):

        t: dict = translates(Interaction.guild)

        try:

            r: requests = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await Interaction.response.send_message(f'https://crafatar.com/renders/head/{r.json()["id"]}/?size=128&overlay')

        except:

            await Interaction.response.send_message(t['args']['miecraft']['errorhead'])

    @slash_command(name = 'skin_minecraft',
        guild_only = True,
        description = 'Envia uma skin de um player',
        )
    @option(name = 'player', description = 'Nickname')
    @moduleCheck('diverção')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def skin(self, Interaction: discord.Interaction, player):

        t: dict = translates(Interaction.guild)

        try:

            r: requests = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await Interaction.response.send_message(f'https://crafatar.com/skins/{r.json()["id"]}')
        
        except:

            await Interaction.response.send_message(t['args']['miecraft']['errorskin'])

    @slash_command(name = 'avatar_player_minecraft',
        guild_only = True,
        description = 'Envia a cabeça de um player',
        )
    @option(name = 'player', description = 'Nickname')
    @moduleCheck('diverção')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def avatar(self, Interaction: discord.Interaction, player):

        t: dict = translates(Interaction.guild)

        try:

            r: requests = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await Interaction.response.send_message(f'https://crafatar.com/avatars/{r.json()["id"]}/?size=128&overlay')
        
        except:

            await Interaction.response.send_message(t['args']['miecraft']['erroravatar'])

def setup(bot: commands.Bot) -> None:
    bot.add_cog(images(bot))