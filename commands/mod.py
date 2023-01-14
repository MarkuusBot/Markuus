import discord as discord
import hexacolors

from discord.ext import commands
from discord import slash_command, option
from db.moderation import advdb
from funcs.checks import moduleCheck, vote
from classes.selectbuttons import *

class moderation(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(
        guild_only = True,
        name = 'setlang',
        description = 'Sets Markuus language',
        name_localizations = {
            'en-US': 'setlang',
            'en-GB': 'setlang',
            'es-ES': 'elegir_lenguaje',
            'pt-BR': 'definir_idioma',
            'fr': 'définir_la_langue'
        },
        description_localizations = {
            'en-US': 'Sets Markuus language',
            'en-GB': 'Sets Markuus language',
            'es-ES': 'Establece el idioma de Markuus',
            'pt-BR': 'Define o idioma do Markuus',
            'fr': 'Définit la langue Markuus'
        })
    @commands.has_guild_permissions(manage_guild = True)
    @moduleCheck('moderação')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def setlang(self, interction: discord.Interaction):

        t: dict = translates(interction.guild)

        await interction.response.send_message(t['args']['lang']['select'], view = discord.ui.View(setlang(self.bot, interction.user,t)), ephemeral = True)

    @slash_command(
        guild_only = True,
        name = 'setlogs',
        description = 'Sets Markuus logs',
        description_localizations = {
            'en-US': 'Sets Markuus logs',
            'en-GB': 'Sets Markuus logs',
            'es-ES': 'Establece registros de Markuus',
            'pt-BR': 'Define as logs do Markuus',
            'fr': 'Définit les journaux de Markuus'
        })
    @commands.has_guild_permissions(manage_guild = True)
    @moduleCheck('moderação')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def setlogs(self, interction: discord.Interaction):

        t: dict = translates(interction.guild)

        await interction.response.send_message('',view = discord.ui.View(setlog(self.bot,interction.user,t)), ephemeral = True)

    @slash_command(
        guild_only = True,
        name = 'autorole',
        description = 'Define um cargo para o auto role',
        description_localizations = {
            'en-US': 'Defines the role of autorole',
            'en-GB': 'Defines the role of autorole',
            'es-ES': 'Define el papel de autorole',
            'pt-BR': 'Define o cargo do autorole',
            'fr': 'Définit le rôle de l\'autorole'
        })
    @option(name = 'role', description = 'Escolha o cargo')
    @commands.has_guild_permissions(manage_guild = True)
    @moduleCheck('moderação')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def autorole(self, interction: discord.Interaction, role: discord.Role = None):

        t: dict = translates(interction.guild)
        db: Collection = mod.find_one({'_id':interction.guild.id})
        if role == None and db['autorole']['True?'] == True:
            dbmoderation.autorole('autorole',False,interction.guild,None)
            await interction.response.send_message(t['args']['mod']['unsetautorole'])
        elif role == None and db['autorole']['True?'] == False:
            await interction.response.send_message(t['args']['mod']['autoroleoff'])
        else:
            dbmoderation.autorole('autorole',True,interction.guild,role.id)
            await interction.response.send_message(f"{t['args']['mod']['setautorole']} {role.mention}")

    @slash_command(
        guild_only = True,
        name = 'kick',
        description = 'Kick a person from the server',
        name_localizations = {
            'en-US': 'kick',
            'en-GB': 'kick',
            'es-ES': 'expulsar',
            'pt-BR': 'expulsar',
            'fr': 'expulser'
        },
        description_localizations = {
            'en-US': 'Kick a person from the server',
            'en-GB': 'Kick a person from the server',
            'es-ES': 'Expulsar a una persona del servidor.',
            'pt-BR': 'Expulsa uma pessoa do server',
            'fr': 'Expulser une personne du serveur'
        })
    @option(name = 'member', description = 'Escolha o membro a expulsar')
    @option(name = 'reason', description = 'Motivo para expulsar')
    @commands.has_guild_permissions(kick_members = True)
    @commands.bot_has_guild_permissions(kick_members = True)
    @moduleCheck('moderação')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, interction: discord.Interaction, member: discord.Member, reason:str=None):

        t: dict = translates(interction.guild)

        if reason == None: reason:str = t["args"]["mod"]["notreason"]

        await interction.response.send_message(t["args"]["mod"]["confirmkick"].format(member.mention),view = buttonkick(self.bot,member,reason, interction.user))

    @slash_command(
        guild_only = True,
        name = 'ban',
        description = 'Bane um membro do server',
        name_localizations = {
            'en-US': 'ban',
            'en-GB': 'ban',
            'es-ES': 'prohibir',
            'pt-BR': 'banir',
            'fr': 'bannir'
        },
        description_localizations = {
            'en-US': 'Ban a server member',
            'en-GB': 'Ban a server member',
            'es-ES': 'Prohibir a un miembro del servidor.',
            'pt-BR': 'Bane um membro do servidor',
            'fr': 'Bannir un membre du serveur'
        })
    @option(name = 'member', description = 'Escolha um membro a banir')
    @option(name = 'reason', description = 'Motivo de banir')
    @commands.has_guild_permissions(ban_members = True)
    @commands.bot_has_guild_permissions(ban_members = True)
    @moduleCheck('moderação')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Ban(self, interction: discord.Interaction, member: discord.Member, reason:str=None):

        t: dict = translates(interction.guild)

        if reason == None: reason:str = t["args"]["mod"]["notreason"]

        await interction.response.send_message(t["args"]["mod"]["confirmban"].format(member.mention),view = buttonban(self.bot,member,reason,interction.user))

    @slash_command(name = 'clear',
        description = 'clear the chat',
        guild_only = True,
        name_localizations = {
            'en-US': 'clear',
            'en-GB': 'clear',
            'es-ES': 'limpio',
            'pt-BR': 'limpar',
            'fr': 'clair'
        },
        description_localizations = {
            'en-US': 'Clear the chat',
            'en-GB': 'Clear the chat',
            'es-ES': 'Borrar el chat.',
            'pt-BR': 'Limpa o chat',
            'fr': 'canal le clair'
        }
    )
    @option(name = 'qnt', description = 'Escolha uma quantidade de mensagem a limpar')
    @commands.has_guild_permissions(manage_channels = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    @moduleCheck('moderação')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clear(self, interction: discord.Interaction, qnt: int):

        t: dict = translates(interction.guild)
            
        if qnt > 1000: await interction.response.send_message(t["args"]["mod"]["limiteclear1"])
        elif qnt == 0: await interction.response.send_message(t["args"]["mod"]["limiteclear2"])
        elif qnt < 0: await interction.response.send_message(t["args"]["mod"]["limiteclear3"])
        else:
            purge = await interction.channel.purge(limit=qnt)
            await interction.response.send_message(t["args"]["mod"]["clearchat"].format(len(purge), interction.user.mention))

    @slash_command(name = 'unban',
        description = 'Desbane um membro',
        guild_only = True,
        name_localizations = {
            'en-US': 'unban',
            'en-GB': 'unban',
            'es-ES': 'desbanear',
            'pt-BR': 'desbanir',
            'fr': 'débannir'
        },
        description_localizations = {
            'en-US': 'Unban a server member',
            'en-GB': 'Unban a server member',
            'es-ES': 'Desbanear a un miembro del servidor.',
            'pt-BR': 'Desbane um membro do servidor',
            'fr': 'Débannir un membre du serveur'
        })
    @option(name = 'id', description = 'Id do membro')
    @option(name = 'reason', description = 'Motivo de desbanir')
    @commands.has_guild_permissions(ban_members = True)
    @commands.bot_has_guild_permissions(ban_members = True)
    @moduleCheck('moderação')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unban(self, interction: discord.Interaction, id, reason: str = None):

        t: dict = translates(interction.guild)

        if reason == None: reason: str = t["args"]["mod"]["notreason"]

        e: discord.Embed = discord.Embed(title = 'UnBan',

        description = t["args"]["mod"]["logunban"].format(int(id),interction.user,reason,int(id)))

        try:

            try:

                w: discord.Webhook = await self.bot.fetch_webhook(mod.find_one({'_id': interction.guild.id})['lmod']['webhook'])

                await w.send(embed = e)

                await interction.response.send_message(f'{id} {t["args"]["mod"]["unbansucess"]}')
                
            except:

                channel: discord.TextChannel = self.bot.get_channel(mod.find_one({'_id': interction.guild.id})['lmod']['id'])

                webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log')

                dbmoderation.logs('lmod',True,interction.guild,mod.find_one({'_id': interction.guild.id})['lmod']['id'], webhook.id)

                w: discord.Webhook = await self.bot.fetch_webhook(mod.find_one({'_id': interction.guild.id})['lmod']['webhook'])

                await w.send(embed = e)
            
        except:

            user: discord.User = await self.bot.fetch_user(int(id))

            await interction.guild.unban(user)

            await interction.response.send_message(embed = e)

    @slash_command(name = 'add_warning',
        description = 'add a warning',
        guild_only = True,
        name_localizations = {
            'en-US': 'add_warning',
            'en-GB': 'add_warning',
            'es-ES': 'añadir_advertencia',
            'pt-BR': 'adc_advertencia',
            'fr': 'ajouter_avertissement'
        },
        description_localizations = {
            'en-US': 'Add a warning',
            'en-GB': 'Add a warning',
            'es-ES': 'Añadir una advertencia.',
            'pt-BR': 'Adiciona uma adivetencia',
            'fr': 'Ajouter une aventure'
        })
    @option(name = 'member', description = 'Mencione o membro')
    @option(name = 'reason', description = 'Motivo da advertencia')
    @moduleCheck('moderação')
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_guild_permissions(kick_members = True)
    async def adv(self, interction: discord.Interaction, member: discord.Member, reason):

        t: dict = translates(interction.guild)

        e: discord.Embed = discord.Embed(

        title = t['args']['adv'],

        description = t['args']['mod']['adv'].format(member.mention,interction.user.mention,reason))

        e.set_footer(text = f'id: {member.id}')

        try:

            db: Collection = mod.find_one({'_id':interction.guild.id})

            if db['lmod']['True?'] == True:

                advdb.update_one( { "_id":f'{interction.guild.id}_{member.id}'}, {'$inc':{f'qnt':+1}}, upsert = True )

                dbmoderation.adcadvdb(interction.guild,interction.user,member,f"{t['args']['adv']}{advdb.find_one({ '_id':f'{interction.guild.id}_{member.id}'})['qnt']}",reason)

                await interction.response.send_message(t['args']['advsucess'].format(member.mention), ephemeral = True)

                channel: discord.TextChannel = self.bot.get_channel(db['lmod']['id'])

                try:

                    w: discord.Webhook = await self.bot.fetch_webhook(db['lmod']['webhook'])

                    await w.send(embed = e)
                
                except:

                    webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log')

                    dbmoderation.logs('lmod',True,interction.guild,db['lmod']['id'], webhook.id)

                    w: discord.Webhook = await self.bot.fetch_webhook(db['lmod']['webhook'])

                    await w.send(embed = e)
            
        except:

            advdb.update_one( { "_id":f'{interction.guild.id}_{member.id}'}, {'$inc':{f'qnt':+1}}, upsert = True )

            dbmoderation.adcadvdb(interction.guild,interction.user,member,f"{t['args']['adv']}{advdb.find_one({ '_id':f'{interction.guild.id}_{member.id}'})['qnt']}",reason)

    @slash_command(name = 'remove_warning',
        description = 'Remove a member\'s warning',
        guild_only = True,
        name_localizations = {
            'en-US': 'remove_warning',
            'en-GB': 'remove_warning',
            'es-ES': 'eliminar_advertencia',
            'pt-BR': 'rmv_advertencia',
            'fr': 'supprimer_avertissement'
        },
        description_localizations = {
            'en-US': 'Remove a member\'s warning',
            'en-GB': 'Remove a member\'s warning',
            'es-ES': 'Eliminar la advertencia de un miembro.',
            'pt-BR': 'Remove uma advertencia de um membro',
            'fr': 'Supprimer l\'avertissement d\'un membre'
        })
    @option(name = 'member', description = 'Mencione o membro')
    @moduleCheck('moderação')
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_guild_permissions(kick_members = True)
    async def rmvadv(self, interction: discord.Interaction, member: discord.Member):

        t: dict = translates(interction.guild)

        try:

            if advdb.find_one({ '_id':f'{interction.guild.id}_{member.id}'})['qnt'] == 0:

                await interction.response.send_message(t['args']['notadv'], ephemeral = True)

                return

            e: discord.Embed = discord.Embed(

            title = t['args']['rmvadv'],

            description = t['args']['mod']['rmvadv'].format(member.mention,interction.user.mention))

            e.set_footer(text = f'id: {member.id}')

            rankings: Collection = advdb.find_one({'_id': f'{interction.guild.id}_{member.id}'})

            hgc: Collection = rankings[f'{t["args"]["adv"]}{advdb.find_one({ "_id":f"{interction.guild.id}_{member.id}"})["qnt"]}']

            try:

                db: Collection = mod.find_one({'_id':interction.guild.id})

                if db['lmod']['True?'] == True:

                    advdb.update_one( { "_id":f'{interction.guild.id}_{member.id}'}, {'$inc':{f'qnt':-1}}, upsert = True )

                    dbmoderation.rmvadvdb(interction.guild,hgc[0],member,f"{t['args']['adv']}{advdb.find_one({ '_id':f'{interction.guild.id}_{member.id}'})['qnt']+1}",hgc[2])

                    await interction.response.send_message(t['args']['rmvadvsucess'].format(member.mention), ephemeral = True)

                    channel: discord.TextChannel = self.bot.get_channel(db['lmod']['id'])

                    try:

                        w: discord.Webhook = await self.bot.fetch_webhook(db['lmod']['webhook'])

                        await w.send(embed = e)
                    
                    except:

                        webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log')

                        dbmoderation.logs('lmod',True,interction.guild,db['lmod']['id'], webhook.id)

                        w: discord.Webhook = await self.bot.fetch_webhook(db['lmod']['webhook'])

                        await w.send(embed = e)
                
            except:

                advdb.update_one( { "_id":f'{interction.guild.id}_{member.id}'}, {'$inc':{f'qnt':-1}}, upsert = True )

                dbmoderation.rmvadvdb(interction.guild,hgc[0],member,f"{t['args']['adv']}{advdb.find_one({ '_id':f'{interction.guild.id}_{member.id}'})['qnt']+1}",hgc[2])

        except:

            await interction.response.send_message(t['args']['notadv'],ephemeral = True)

    @slash_command(name = 'force_move', 
        description = 'Move um membro para a sua call privada',
        guild_only = True
    )
    @option(name = 'membro', description = 'Escolha o membro para mover para uma call')
    @option(name = 'canal', description = 'Escolha o canal para mover o membro')
    @moduleCheck('moderação')
    @commands.cooldown(1,5, commands.BucketType.user)
    @vote()
    @commands.has_guild_permissions(move_members = True)
    async def fmv(self, interction: discord.Interaction, member: discord.Member, canal: discord.VoiceChannel):

        t: dict = translates(interction.guild)

        call: discord.VoiceChannel = self.bot.get_channel(canal.id)

        if member.voice == None:
            await interction.response.send_message(t['args']['mod']['notcall'].formmat(member.mention), ephemeral = True)
            return

        await member.move_to(call)

        await interction.response.send_message(t['args']['mod']['mvcall'].formart(member.mention, call.mention), ephemeral = True)

    @slash_command(name = 'force_disconnect', 
        description = 'Desconecta uma pessoa da call',
        guild_only = True
    )
    @option(name = 'member', description = 'Escolha o membro para desconectar da call')
    @moduleCheck('moderação')
    @commands.cooldown(1,5, commands.BucketType.user)
    @vote()
    @commands.has_guild_permissions(move_members = True)
    async def fdsc(self, interction: discord.Interaction, member: discord.Member):

        t: dict = translates(interction.guild)

        if member.voice == None:
            await interction.response.send_message(t['args']['mod']['notcall'].formmat(member.mention), ephemeral = True)
            return

        await member.move_to(None)

        await interction.response.send_message(t['args']['mod']['dsccall'].formart(member.mention), ephemeral = True)

    @slash_command(guild_only = True, name = 'embed', description = 'Envia uma embed em um chat desejado')
    @option(name = 'channel', description = 'Escolha o chat para enviar a embed')
    @option(name = 'title', description = 'Escreva o titulo da embed')
    @option(name = 'link_image', description = 'Escolha a imagem da embed')
    @option(name = 'mention', description = 'Mencione um cargo para mencionar na embed')
    @option(name = 'content', description = 'Escreva o conteudo da embed')
    @option(name = 'color', description = 'Escolha a cor da embed')
    @moduleCheck('moderação')
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_guild_permissions(manage_channels = True)
    async def embed(self, interction: discord.Interaction, channel: discord.TextChannel = None, title = None, img = None, mention: discord.Role = None, color = None, content = None):

        if channel == None: channel: discord.TextChannel = interction.channel
        if title == None: title: str = ''
        if img == None: img: str = ''
        if content == None: content: str = ''

        if color == None: color: int = hexacolors.stringColor('indigo')
        else:
            try: color: int =  hexacolors.stringColor(color)
            except:
                try: color: int =  hexacolors.hexadecimal(color)
                except: color: int =  hexacolors.autodetect(color)

        if mention == None: mention: str = ''
        else: mention = mention.mention

        e: discord.Embed = discord.Embed(title = title, description = content, colour = color)
        e.set_image(url = img)
        e.set_footer(text = f'{interction.guild.name}, author: {interction.user.name}', icon_url = interction.guild.icon)
        channel2: discord.TextChannel = self.bot.get_channel(channel.id)

        await channel2.send(mention,embed = e)

    @slash_command(guild_only = True,name = 'editembed', description = 'Edita uma embed já enviada')
    @option(name = 'channel', description = 'Envie o id do canal')
    @option(name = 'embedid', description = 'Envie o id da embed')
    @option(name = 'title', description = 'Escreva o titulo da embed')
    @option(name = 'img', description = 'Escolha a imagem da embed')
    @option(name = 'mention', description = 'Mencione um cargo para mencionar na embed')
    @option(name = 'content', description = 'Escreva o conteudo da embed')
    @option(name = 'color', description = 'Escolha a cor da embed')
    @moduleCheck('moderação')
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_guild_permissions(manage_channels = True)
    async def editembed(self, interction: discord.Interaction, embedid, title = None, img = None, mention: discord.Role = None, content = None,color = None, channel: discord.TextChannel = None):

        if channel == None: channel: discord.TextChannel = interction.channel

        if title == None: title: str = ''

        if img == None: img: str = ''
        
        if color == None:color: int = hexacolors.stringColor('indigo')
        else:
            try: color: int =  hexacolors.stringColor(color)
            except:
                try: color: int =  hexacolors.hexadecimal(color)
                except: color: int =  hexacolors.autodetect(color)

        if content == None: content: str = ''

        if mention == None:mention: str = ''
        else: mention = mention.mention

        mensagem = await channel.fetch_message(int(embedid))

        e: discord.Embed = discord.Embed(title = title, description = content, colour = color)
        e.set_image(url = img)
        e.set_footer(text = f'{interction.guild.name} author: {interction.user.name}', icon_url = interction.guild.icon)

        await mensagem.edit(mention,embed = e)

def setup(bot:commands.Bot):
    bot.add_cog(moderation(bot))