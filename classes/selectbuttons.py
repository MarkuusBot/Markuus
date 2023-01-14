import discord
from discord import Interaction
from discord.ext import commands
from discord.ui import View, Select
from embeds.help import help0, help1, help2, help3, help4, help5
from funcs.defs import translates
from db.moderation import mod, dbmoderation
from pymongo.collection import Collection

class buttonkick(View):
    
    def __init__(self, bot, membro, motivo, ctx):

        self.membro: discord.Member = membro
        self.bot: commands.Bot = bot
        self.motivo: str = motivo
        self.ctx = ctx

        super().__init__(timeout = 180)

    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple)
    async def confirmkick(self, button: discord.Button, interaction: Interaction):

        t: dict = translates(interaction.guild)

        if interaction.user.id != self.ctx.id: 
            return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

        match self.membro:

            case self.ctx:

                await interaction.response.send_message('Non')

                return

            case self.bot.user:

                await interaction.response.send_message('non2')

                return
            
            case _:

                try:

                    e: discord.Embed = discord.Embed(title = 'kick', description = t["args"]["mod"]["logkick"].format(self.membro.name, self.ctx.mention,self.motivo,self.membro.id))

                    await interaction.message.delete()

                    await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["kicksucess"]}', ephemeral = True)

                    await interaction.guild.kick(user = self.membro ,reason = self.motivo)

                    channel: discord.TextChannel = self.bot.get_channel(mod.find_one({'_id': interaction.guild.id})['lmod']['id'])

                    try:

                        w: discord.Webhook = await self.bot.fetch_webhook(mod.find_one({'_id': interaction.guild.id})['lmod']['webhook'])

                        await w.send(embed = e)
                    
                    except:

                        webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log')

                        dbmoderation.logs('lmod',True,interaction.guild,mod.find_one({'_id': interaction.guild.id})['lmod']['id'], webhook.id)

                        w: discord.Webhook = await self.bot.fetch_webhook(mod.find_one({'_id': interaction.guild.id})['lmod']['webhook'])

                        await w.send(embed = e)

                    self.stop()

                except:

                    e: discord.Embed = discord.Embed(title = 'kick', description = t["args"]["mod"]["logkick"].format(self.membro.name, self.ctx.mention,self.motivo,self.membro.id))

                    await interaction.channel.send(embed = e)

                    await interaction.message.delete()

                    await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["kicksucess"]}\n{t["args"]["mod"]["lognotfound"]}', ephemeral = True)

                    await interaction.guild.kick(user = self.membro ,reason = self.motivo)

                    self.stop()

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denykick(self, button: discord.ui.Button, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)

        if interaction.user.id != self.ctx.id:
            return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

        await interaction.message.delete()

        self.stop()

class buttonban(View):
    
    def __init__(self, bot, membro, motivo, ctx):

        self.membro: discord.Member = membro

        self.bot: commands.Bot = bot

        self.motivo: str = motivo

        self.ctx: discord.Member = ctx

        super().__init__(timeout = 180)

    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple)
    async def confirmban(self, button: discord.Button, interaction: Interaction):

        t: dict = translates(interaction.guild)

        if interaction.user.id != self.ctx.id:
            return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

        match self.membro.id:

            case self.ctx.id:

                await interaction.response.send_message('Non')

                return

            case self.bot.user.id:

                await interaction.response.send_message('non2')

                return
            
            case _:

                try:

                    e: discord.Embed = discord.Embed(title = 'Ban', description =  t["args"]["mod"]["logban"].format(self.membro.name, self.ctx.mention,self.motivo,self.membro.id))

                    await interaction.message.delete()

                    await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["bansucess"]}', ephemeral = True)

                    await interaction.guild.ban(user = self.membro ,reason = self.motivo)

                    channel: discord.TextChannel = self.bot.get_channel(mod.find_one({'_id': interaction.guild.id})['lmod']['id'])

                    try:

                        w: discord.Webhook = await self.bot.fetch_webhook(mod.find_one({'_id': interaction.guild.id})['lmod']['webhook'])

                        await w.send(embed = e)
                    
                    except:

                        webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log')

                        dbmoderation.logs('lmod',True,interaction.guild,mod.find_one({'_id': interaction.guild.id})['lmod']['id'], webhook.id)

                        w: discord.Webhook = await self.bot.fetch_webhook(mod.find_one({'_id': interaction.guild.id})['lmod']['webhook'])

                        await w.send(embed = e)

                    self.stop()

                except:

                    e: discord.Embed = discord.Embed(title = 'Ban', description = t["args"]["mod"]["logban"].format(self.membro.name, self.ctx.mention,self.motivo,self.membro.id))

                    await interaction.channel.send(embed = e)

                    await interaction.message.delete()

                    await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["bansucess"]}\n{t["args"]["mod"]["lognotfound"]}', ephemeral = True)

                    await interaction.guild.ban(user = self.membro ,reason = self.motivo)

                    self.stop()

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denyban(self, button: discord.ui.Button, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)

        if interaction.user.id != self.ctx.id:
            return await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

        await interaction.message.delete()

        self.stop()

class selecthelp(Select):

    def __init__(self, bot, ctx, t):

        self.bot: commands.Bot = bot

        self.ctx = ctx

        self.t: dict = t

        super().__init__(
        placeholder = t['help']['extras']['commands'],
        options = [
            discord.SelectOption(
                label =  t['help']['mod']['name1'],
                description =  t['help']['mod']['name2'],
                value = '0'
            ),
            discord.SelectOption(
                label =  t['help']['general']['name'],
                description =  t['help']['general']['description'],
                value = '1'
            ),
            discord.SelectOption(
                label = t['help']['economy']['name'],
                description = t['help']['general']['description'],
                value = '2'
            ),
            discord.SelectOption(
                label = t['help']['suport']['name'],
                description = t['help']['suport']['description'],
                value = '3'
            ),
            discord.SelectOption(
                label = t['help']['image']['name'],
                description = t['help']['image']['description'],
                value = '4'
            ),
            discord.SelectOption(
                label = t['help']['actions']['name'],
                description = t['help']['actions']['description'],
                value = '5'
            )
        ]
    )
    async def callback(self, interaction: discord.Interaction):

        if interaction.user.id != self.ctx.id:
            return await interaction.response.send_message(f'{self.t["args"]["mod"]["notpermission"]}', ephemeral = True)
        
        match self.values[0]:

            case '0': await help0(self.bot, interaction)
            case '1': await help1(self.bot, interaction)
            case '2': await help2(self.bot, interaction)
            case '3': await help3(self.bot, interaction)
            case '4': await help4(self.bot, interaction)
            case '5': await help5(self.bot, interaction)

class setlang(Select):

    def __init__(self, bot, ctx, t):

        self.bot: commands.Bot = bot

        self.ctx = ctx

        self.t: dict = t

        super().__init__(
        placeholder= t['args']['lang']['lang'],
        options = [
            discord.SelectOption(
                label = 'pt-BR',
                description = t['args']['lang']['ptbr'],
                value = 'pt-br'
            ),
            discord.SelectOption(
                label = 'en-US',
                description = t['args']['lang']['eng'],
                value = 'en-us'
            ),
            discord.SelectOption(
                label = 'fr-FR',
                description = t['args']['lang']['fr'],
                value = 'fr-fr'
            ),
            discord.SelectOption(
                label = 'es-ES',
                description = t['args']['lang']['es'],
                value = 'es-es'
            )
        ])
    async def callback(self, interaction: discord.Interaction):

        match self.values[0]: 

            case 'pt-br':

                if self.values[0] == mod.find_one({'_id':interaction.guild.id})['lang']:

                    await interaction.response.send_message(self.t['args']['lang']['langequal'], ephemeral = True)

                    return

                dbmoderation.lang('lang',self.values[0],interaction.guild)

                await interaction.response.send_message('Okay, agora falarei português', ephemeral = True)

            case 'en-us':

                if self.values[0] == mod.find_one({'_id':interaction.guild.id})['lang']:

                    await interaction.response.send_message(self.t['args']['lang']['langequal'], ephemeral = True)

                    return

                dbmoderation.lang('lang',self.values[0],interaction.guild)

                await interaction.response.send_message('ok now i will speak english', ephemeral = True)

            case 'fr-fr':

                if self.values[0] == mod.find_one({'_id':interaction.guild.id})['lang']:

                    await interaction.response.send_message(self.t['args']['lang']['langequal'], ephemeral = True)

                    return

                dbmoderation.lang('lang',self.values[0],interaction.guild)

                await interaction.response.send_message('Bon, maintenant je vais parler français', ephemeral = True)

            case 'es-es':

                if self.values[0] == mod.find_one({'_id':interaction.guild.id})['lang']:

                    await interaction.response.send_message(self.t['args']['lang']['langequal'], ephemeral = True)

                    return

                dbmoderation.lang('lang',self.values[0],interaction.guild)

                await interaction.response.send_message('Bien, ahora hablaré español.', ephemeral = True)

class actvate(Select):

    def __init__(self, bot, ctx, guild, log):

        self.bot: commands.Bot = bot

        self.ctx = ctx

        self.log: str = log

        t: dict = translates(guild)

        super().__init__(

            placeholder= t['args']['mod'][log],
            
            options = [

                discord.SelectOption(

                    label = t['args']['act'],
                    value = 'ativar'

                ),

                discord.SelectOption(

                    label = t['args']['dsb'],
                    value = 'desativar'

                ),

            ]
        )
    async def callback(self, interaction: discord.Interaction):

        t: dict = translates(interaction.guild)

        db: Collection = mod.find_one({'_id': interaction.guild.id})

        match self.values[0]:

            case 'ativar':

                await interaction.response.send_message(t['args']['sendid'], ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                id = interaction.guild.get_channel(int(msg50.content))

                await msg50.delete()

                await interaction.channel.send(t['args']['sucessdef'], delete_after = 3)

                try:

                    if db[self.log]['webhook'] != None:

                        w: discord.Webhook = await self.bot.fetch_webhook(db[self.log]['webhook'])

                        await w.edit(channel = id)

                        dbmoderation.logs(self.log,True,interaction.guild,id.id, db[self.log]['webhook'])
                
                except:

                    webhook = await id.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')

                    dbmoderation.logs(self.log,True,interaction.guild,id.id, webhook.id)     
            
            case 'desativar':

                await interaction.response.send_message(t['args']['undef'], ephemeral = True)

                dbmoderation.logs(self.log,False,interaction.guild,None,None)

class setlog(Select):

    def __init__(self, bot, ctx, t):

        self.bot: commands.Bot = bot

        self.ctx = ctx

        self.t: dict = t

        super().__init__(
            placeholder= t['args']['mod']['log'],

            options = [

                discord.SelectOption(

                    label = 'Mod',
                    description = t['args']['mod']['lmod'],
                    value = 'mod'

                ),

                discord.SelectOption(

                    label = 'Vc',
                    description = t['args']['mod']['lvoice'],
                    value = 'voice'

                ),

                discord.SelectOption(

                    label = 'Txt',
                    description = t['args']['mod']['ltxt'],
                    value = 'txt'

                ),
                discord.SelectOption(

                    label = 'Mic',
                    description = t['args']['mod']['lmic'],
                    value = 'mic'

                ),

            ]
        )
    async def callback(self, interaction : discord.Interaction):

        match self.values[0]:

            case 'mod': await interaction.response.send_message(view = discord.ui.View(actvate(self.bot, interaction.user,interaction.guild,'lmod')), ephemeral = True)
            case 'voice': await interaction.response.send_message(view = discord.ui.View(actvate(self.bot, interaction.user,interaction.guild,'lvoice')), ephemeral = True)
            case 'txt': await interaction.response.send_message(view = discord.ui.View(actvate(self.bot, interaction.user,interaction.guild,'ltxt')), ephemeral = True)
            case 'mic': await interaction.response.send_message(view = discord.ui.View(actvate(self.bot, interaction.user,interaction.guild,'lmic')), ephemeral = True)