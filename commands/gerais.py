import discord, time, random, platform, hexacolors

from discord.ext import commands
from discord import slash_command, option
from classes.buttons import profile, changeavatar
from funcs.checks import moduleCheck
from funcs.defs import translates
from classes.selectbuttons import selecthelp
from db.economy import dbeconomy, bank
from db.moderation import mod
from db.members import perf, dbmember
from pymongo.collection import Collection

class gerais(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot: commands.Bot = bot

    @slash_command(
        guild_only = True,
        name = 'hello_world',
        description = 'Markuus test command',
        name_localizations = {
            'en-US': 'hello_world',
            'en-GB': 'hello_world',
            'es-ES': 'hola_mundo',
            'pt-BR': 'ola_mundo',
            'fr': 'bonjour_le_monde'
        },
        description_localizations = {
            'en-US': 'Markuus test command',
            'en-GB': 'Markuus test command',
            'es-ES': 'Comando de prueba de Markuus',
            'pt-BR': 'Comando de teste do Markuus',
            'fr': 'Commande de test Markuus'
        }
    )
    @moduleCheck('gerais')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def hello(self, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)

        await interaction.response.send_message(t["args"]["hello"])

    @slash_command(name = 'help',
        guild_only = True,
        description = 'Help command Markuus',
        name_localizations = {
            'en-US': 'help',
            'en-GB': 'help',
            'es-ES': 'ayuda',
            'pt-BR': 'ajuda',
            'fr': 'aider'
        },
        description_localizations = {
            'en-US': 'Help command Markuus',
            'en-GB': 'Help command Markuus',
            'es-ES': 'Comando de ayuda de Markuus',
            'pt-BR': 'Comando de ajuda do Markuus',
            'fr': 'Commande de aider Markuus'
        })
    @moduleCheck('gerais')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)

        h: discord.Embed = discord.Embed(
            title =  t['help']['extras']['commands'],
            description = t['help']['extras']['init'],
            color = hexacolors.stringColor('indigo')
        )
        h.set_thumbnail(url = self.bot.user.avatar)

        await interaction.response.send_message(embed = h, view = discord.ui.View(selecthelp(self.bot,interaction.user,t)))

    @slash_command(name = 'random',
        guild_only = True,
        description = 'Choose a random number for you',
        name_localizations = {
            'en-US': 'random',
            'en-GB': 'random',
            'es-ES': 'aleatorio',
            'pt-BR': 'aleatorio',
            'fr': 'aléatoire'
        },
        description_localizations = {
            'en-US': 'Choose a random number for you',
            'en-GB': 'Choose a random number for you',
            'es-ES': 'Elija un número aleatorio para usted',
            'pt-BR': 'Escolhe um numero aleatorio para você',
            'fr': 'Choisissez un nombre aléatoire pour vous'
        })
    @option(name = 'number', description = 'Coloque um numero')
    @moduleCheck('gerais')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def aleatorio(self, interaction: discord.Interaction,number: int):

        t: dict = translates(interaction.guild)
        
        dado: int = random.randint(1,number)

        await interaction.response.send_message(f'{t["args"]["random"]} {dado}')

    @slash_command(
        guild_only = True,
        name = 'ping',
        description = 'Shows my ping and discord api',
        description_localizations = {
            'en-US': 'Shows my ping and discord api',
            'en-GB': 'Shows my ping and discord api',
            'es-ES': 'Mostrar mi api de ping y discord',
            'pt-BR': 'Mostra o meu ping e da api do discord',
            'fr': 'Afficher mon ping et discord api'
        })
    @moduleCheck('gerais')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, interaction: discord.Interaction):
        
        start_time: time = time.time()

        t: dict = translates(interaction.guild)

        Ping:int = round(self.bot.latency * 1000)

        end_time: time = time.time()

        p4: discord.Embed = discord.Embed(title = 'Ping', 

        description = f'{t["args"]["ping"]}: {Ping}ms\nAPI: {round((end_time - start_time) * 1000)}ms', color = hexacolors.stringColor('indigo'))

        await interaction.response.send_message(embed = p4)

    @slash_command(
        guild_only = True,
        name = 'servers',
        description = "Tells how many servers I'm on",
        description_localizations = {
            'en-US': "Tells how many servers I'm on",
            'en-GB': "Tells how many servers I'm on",
            'es-ES': 'Dime en cuántos servidores estoy',
            'pt-BR': 'Diz em quantos servers eu estou',
            'fr': 'Dites-moi sur combien de serveurs je suis'
        })
    @moduleCheck('gerais')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servers(self, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)

        await interaction.response.send_message(t["args"]["servers"]["s"].format(str(len(self.bot.guilds))))

    @slash_command(
        guild_only = True,
        name = 'server_info',
        description = 'Pulls information from the server',
        description_localizations = {
            'en-US': "Pulls information from the server",
            'en-GB': "Pulls information from the server",
            'es-ES': 'Extraer la información del servidor',
            'pt-BR': 'Puxa as informações do server',
            'fr': 'Obtenir les informations du serveur'
        })
    @moduleCheck('gerais')
    @commands.cooldown(1, 5, commands.BucketType.user)
    @option(name = 'server', description = 'Envie o id do server')
    async def serverInfo(self, interaction: discord.Interaction, server: discord.Guild = None):

        t: dict = translates(interaction.guild)
        emojiServerWoner: discord.Emoji = self.bot.get_emoji(1044755634228301874)
        if server == None: server = interaction.guild
        
        if mod.find_one({'_id':interaction.guild.id})['lang'] != 'pt-br': servercreate: str = server.created_at.strftime(f"%Y %m %d")
        else: servercreate: str = server.created_at.strftime(f"%d %m %Y")

        embed: discord.Embed = discord.Embed(title = f'**{server.name}**',
        color = hexacolors.stringColor('indigo'))

        embed.add_field(name = f':scroll: {t["args"]["si"]["name"]}:', value = server.name, inline = True)
        embed.add_field(name = f':computer:  {t["args"]["si"]["id"]}:', value = server.id, inline = True)

        embed.add_field(name = '════════════', value = '════════════', inline = False)

        embed.add_field(name = f':busts_in_silhouette: {t["args"]["si"]["members"]}:', value = server.member_count, inline = True)
        embed.add_field(name = f':speech_balloon: {t["args"]["si"]["channels"]}:({len(server.text_channels)+len(server.voice_channels)})',
        value = f':keyboard: {t["args"]["si"]["text"]}: {len(server.text_channels)}\n :loud_sound: {t["args"]["si"]["voice"]}:{len(server.voice_channels)}',
        inline = True)

        embed.add_field(name = '════════════', value = '════════════', inline = False)

        embed.add_field(name = f':shield: {t["args"]["si"]["verify"]}:',
        value = '{}'.format(str(server.verification_level).upper()),
        inline = True)
        embed.add_field(name = f'{emojiServerWoner} {t["args"]["si"]["own"]}:', 
        value = '<@{0}>\n ({0})'.format(server.owner_id),
        inline = True)

        embed.add_field(name = '════════════', value = '════════════', inline = False)

        embed.add_field(name = f':calendar_spiral:{t["args"]["si"]["create"]}:', 
        value = servercreate,
        inline = True)

        if server.icon != None: embed.set_thumbnail(url=server.icon)

        await interaction.response.send_message(embed = embed)

    @slash_command(
        guild_only = True,
        name = 'user_info', 
        description = "pulls a member's information or their",
        description_localizations = {
            'en-US': "Pulls a member's information or their",
            'en-GB': "Pulls a member's information or their",
            'es-ES': 'Extrae la información de un miembro o su',
            'pt-BR': 'Puxa as informações de algum membro ou as suas',
            'fr': "Obtenir les informations d'un membre ou leur"
        })
    @moduleCheck('gerais')
    @commands.cooldown(1, 5, commands.BucketType.user)
    @option(name = 'member', description = 'Escolha um membro')
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):

        idemoji: discord.Emoji = self.bot.get_emoji(1045112581062393946)
        roleemoji: discord.Emoji = self.bot.get_emoji(1045369720666333224)
        dolaremoji: discord.Emoji = self.bot.get_emoji(1045370164306247811)
        inviteemoji: discord.Emoji = self.bot.get_emoji(1044747249378414612)

        t: dict = translates(interaction.guild)

        if member == None: member = interaction.user

        dbeconomy.update_bank(member,0)

        user: Collection = bank.find_one({"_id": member.id})

        embed: discord.Embed = discord.Embed(colour=hexacolors.stringColor('indigo'))

        embed.set_author(name=f"User Info - {member}"),

        embed.set_thumbnail(url=member.display_avatar),

        if mod.find_one({'_id':interaction.guild.id})['lang'] != 'pt-br':

            membercreate = member.created_at.strftime(f"%Y %m %d")

            memberjoin = member.joined_at.strftime(f"%Y %m %d")

        else:

            membercreate = member.created_at.strftime(f"%d %m %Y")

            memberjoin = member.joined_at.strftime(f"%d %m %Y")

        embed.add_field(name = f'{idemoji}{t["args"]["ui"]["name"]}:',
        value = member.display_name, inline = True)
        embed.add_field(name = f'{idemoji}ID:', value = member.id, inline = True)

        embed.add_field(name = '════════════', value = '════════════', inline = False)

        embed.add_field(name = f'📅{t["args"]["ui"]["cc"]}:', value = membercreate, inline = True)
        embed.add_field(name = f'{inviteemoji}{t["args"]["ui"]["js"]}:', value = memberjoin, inline = True)

        embed.add_field(name = '════════════', value = '════════════', inline = False)

        embed.add_field(name = f'{roleemoji}{t["args"]["ui"]["toprole"]}:', value = member.top_role.mention, inline = True)
        embed.add_field(name = f'{dolaremoji}edinhos', value = user["edinhos"], inline = True)

        await interaction.response.send_message(embed=embed)

    @slash_command(guild_only = True,name = 'avatar', description = 'Envia o avatar de um membro')
    @moduleCheck('gerais')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Ecolha um membro')
    async def avatar(self, interaction: discord.Interaction, member: discord.Member = None):

        t: dict = translates(interaction.guild)

        if member == None: member = interaction.user

        if member.guild_avatar != None:

            embed: discord.Embed = discord.Embed(title = f'Avatar {member}', 

            description = f'[{t["args"]["avatar"]["click1"]}]({member.guild_avatar}) {t["args"]["avatar"]["click2"]}')

            embed.set_image(url = f'{member.guild_avatar}')

            await interaction.response.send_message(embed = embed, view = changeavatar(member))

            return

        if member.avatar == None:

            embed: discord.Embed = discord.Embed(title = f'Avatar {member}', 

            description = f'[{t["args"]["avatar"]["click1"]}]({member.default_avatar}) {t["args"]["avatar"]["click2"]}')

            embed.set_image(url = f'{member.default_avatar}')

            await interaction.response.send_message(embed = embed)

            return
        
        else:

            embed: discord.Embed = discord.Embed(title = f'Avatar {member}', 

            description = f'[{t["args"]["avatar"]["click1"]}]({member.avatar}) {t["args"]["avatar"]["click2"]}')
            embed.set_image(url = f'{member.avatar}')

            await interaction.response.send_message(embed = embed)

            return

    @slash_command(guild_only = True,name = 'invite', description = 'Encia o link para me convidar para seu server')
    @moduleCheck('gerais')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def invite(self, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)
        
        e: discord.Embed = discord.Embed(title = t['args']['invite']['invite'], 

        description = f'[{t["args"]["invite"]["dsc"]}](https://discord.com/api/oauth2/authorize?client_id=1012121641947517068&permissions=140408933430&scope=bot)')

        e.set_thumbnail(url = self.bot.user.avatar)

        await interaction.response.send_message(embed=e)

    @slash_command(guild_only = True,name = 'vote', description = 'Envia o link para votar em mim no top.gg')
    @moduleCheck('gerais')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def Vote(self, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)

        e1: discord.Emoji = self.bot.get_emoji(972895959191289886)

        server: str = '[Server Suport](https://discord.com/invite/USMVRUcDGa)'

        top: str = '[Top.gg](https://top.gg/bot/1012121641947517068)'

        inv: str = '[Invite](https://discord.com/api/oauth2/authorize?client_id=1012121641947517068&permissions=140408933430&scope=bot)'

        topgg: discord.Embed = discord.Embed(title = 'Vote', 

        description = t['args']['topgg']['dsc'].format(interaction.user.mention))

        topgg.add_field(
            name = f':grey_question: {t["args"]["topgg"]["duvids"]}', 
            value = server, 
            inline = False
        )
        
        topgg.add_field(
            name = f'{e1} {t["args"]["topgg"]["cresc"]}',
            value = top, inline = False
        )

        topgg.add_field(
            name = f':partying_face: {t["args"]["topgg"]["invite"]}', 
            value = inv, inline = False
        )

        topgg.set_thumbnail(url = self.bot.user.avatar.url)

        await interaction.response.send_message(embed = topgg)

    @slash_command(guild_only = True,name = 'bot_info', description = 'Envia algumas informações minha')
    @moduleCheck('gerais')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def botinfo(self, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)

        python: discord.Emoji = self.bot.get_emoji(1044744844234461275)
        discorde: discord.Emoji = self.bot.get_emoji(1044749602257125517)
        Vs: discord.Emoji = self.bot.get_emoji(1045113609488965662)
        name: discord.Emoji = self.bot.get_emoji(1045112581062393946)

        e: discord.Embed = discord.Embed(title = t["args"]["botinfo"]["mif"])
        e.set_thumbnail(url = self.bot.user.avatar.url)
        e.add_field(name = f'{name} {t["args"]["botinfo"]["name"]}', value = self.bot.user.name, inline = True)
        e.add_field(name = f'{Vs} {t["args"]["botinfo"]["language"]}', value = f'{python} Python', inline = True)
        e.add_field(name = '════════════', value = '════════════', inline = False)
        e.add_field(name = f'{discorde} {t["args"]["botinfo"]["version"]}', value = discord.__version__, inline = True)
        e.add_field(name = f'{python} {t["args"]["botinfo"]["pyversion"]}', value = platform.python_version(), inline = True)
        e.add_field(name = '════════════', value = '════════════', inline = False)
        e.add_field(name = f':calendar_spiral: {t["args"]["botinfo"]["ii"]}', value = '2019', inline = True)
        e.add_field(name = f':calendar_spiral: {t["args"]["botinfo"]["rz"]}', value = '2022', inline = True)
        e.add_field(name = '════════════', value = '════════════', inline = False)
        e.add_field(name = 'Commands', value = len(self.bot.application_commands), inline = True)

        await interaction.response.send_message(embed = e)
        
    @slash_command(guild_only = True,name = 'emoji_info', description = 'Envia algumas informações de um emoji')
    @moduleCheck('gerais')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'emoji', description = 'Escolha um emoji')
    async def EmojiInfo(self, interaction: discord.Interaction, emoji: discord.Emoji):

        t: dict = translates(interaction.guild)

        e1: discord.Emoji = self.bot.get_emoji(1045112581062393946)

        embed: discord.Embed = discord.Embed(title = f'{emoji} Emoji Info')
        embed.set_thumbnail(url = emoji.url)
        embed.add_field(name = f':notepad_spiral: {t["args"]["emoji"]["name"]}', value = emoji.name, inline = True)
        embed.add_field(name = f'{e1} {t["args"]["emoji"]["id"]}', value = emoji.id, inline = True)
        embed.add_field(name = f':goggles: {t["args"]["emoji"]["mention"]}', value = f'`<:{emoji.name}:{emoji.id}>`', inline = True)
        embed.add_field(name = f':chains: Url', value = emoji.url, inline = True)
        embed.add_field(name = f':date: {t["args"]["emoji"]["adition"]}', value = emoji.created_at.strftime('%d %m %Y'), inline = True)
        embed.add_field(name = f':mag_right: {t["args"]["emoji"]["server"]}', value = emoji.guild, inline = True)

        await interaction.response.send_message(embed = embed)

    @slash_command(guild_only = True,name = 'profile', description = 'Envia seu perfil')
    @option(name = 'member', description = 'Envia o perfil de um membro')
    @moduleCheck('gerais')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def profile(self, interaction: discord.Interaction, member: discord.Member = None):

        if member == None: member = interaction.user

        if perf.count_documents({'_id': member.id}) == 0:

            dbmember.upPerfil(member,'r0','Idade',None)
            dbmember.upPerfil(member,'r1','Genero',None)
            dbmember.upPerfil(member,'r2',"País",None)
            dbmember.upPerfil(member,'r3','Cidade',None)
            dbmember.upPerfil(member,'r4', 'Descrição do perfil',"Markuus é um otimo Bot")
            dbmember.upPerfil(member,'r5', 'Casado com',None)
        
        i2 = 0

        embed: discord.Embed = discord.Embed(title = 'Perfil')
        embed.set_thumbnail(url = member.display_avatar)

        while True:

            per: Collection = perf.find_one({'_id': member.id})

            if per[f'r{i2}']['value'] != None: embed.add_field(name = per[f'r{i2}']['name'], value = per[f'r{i2}']['value'])

            if per[f'r0']['value'] == None and per[f'r1']['value'] == None\
            and per[f'r2']['value'] == None and per[f'r3']['value'] == None\
            and per[f'r4']['value'] == None and per[f'r5']['value'] == None:
                embed.add_field(name = 'error', value = 'Você não possue registro')
                break

            if i2 == 5: break
            else: i2 += 1
        
        if member.id == interaction.user.id: await interaction.response.send_message(embed = embed, view = profile(interaction.user))

        else: await interaction.response.send_message(embed = embed)

def setup(bot:commands.Bot):
    bot.add_cog(gerais(bot))