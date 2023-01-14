import discord as discord

from discord.ext import commands
from pymongo.collection import Collection
from funcs.defs import *


class eventslogs(commands.Cog):
    
    def __init__(self, bot:commands.Bot):

        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):

        try:
            db: Collection = mod.find_one({'_id': message.guild.id})
            if db['ltxt']['True?'] == True:
                t = translates(message.guild)
                channel: discord.TextChannel = self.bot.get_channel(db['ltxt']['id'])
                e: discord.Embed = discord.Embed(
                    description = t["args"]["logs"]["messaged"].format(message.author.mention, message.channel.mention),
                    color = 0xff0000
                )
                e.add_field(name = f'{t["args"]["logs"]["msg"]}:', value = f'{message.content}', inline=False)
                e.set_author(name = f'{message.author.name}#{message.author.discriminator}', icon_url = message.author.display_avatar)
                try:
                    w: discord.Webhook = await self.bot.fetch_webhook(db['ltxt']['webhook'])
                    if w is None:
                        webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log')
                        await dbmoderation.logs('ltxt',True,message.guild,db['ltxt']['id'], webhook.id)
                        
                    await w.send(embed = e)
                except Exception as error:
                    await dbmoderation.logs('ltxt',False,message.guild,None, None)
        except:
            None

    @commands.Cog.listener()
    async def on_message_edit(self, antes: discord.Message, depois: discord.Message):
        
        try:
            db: Collection = mod.find_one({'_id':antes.guild.id})
            if db['ltxt']['True?'] == True:
                if antes.content == depois.content: return
                t = translates(antes.guild)
                channel: discord.TextChannel = self.bot.get_channel(db['ltxt']['id'])
                e: discord.Embed = discord.Embed(
                    description = t["args"]["logs"]["edit"].format(antes.author.mention,antes.channel.mention),
                    color = 0xfff000)
                e.add_field(name = f'{t["args"]["logs"]["old"]}:', value = f'{antes.content}', inline=False)
                e.add_field(name = f'{t["args"]["logs"]["new"]}:', value =  f'{depois.content}', inline=False)
                e.set_author(name = f'{antes.author.name}#{antes.author.discriminator}', icon_url = antes.author.display_avatar)
                try:
                    w: discord.Webhook = await self.bot.fetch_webhook(db['ltxt']['webhook'])
                    await w.send(embed=e)
                except:
                    try:
                        webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')
                        await dbmoderation.logs('ltxt',True,antes.guild,db['ltxt']['id'], webhook.id)
                        w: discord.Webhook = await self.bot.fetch_webhook(db['ltxt']['webhook'])
                        await w.send(embed = e)
                    except:
                        await dbmoderation.logs('ltxt',False, antes.guild,None, None)
        except:
            None

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, antes: discord.VoiceState, depois: discord.VoiceState):

        try:
            db: Collection = mod.find_one({'_id':member.guild.id})
            if db['lvoice']['True?'] == True:
                t: dict = translates(member.guild)
                channel: discord.TextChannel = self.bot.get_channel(db['lvoice']['id'])
                if antes.channel == None:
                    e: discord.Embed = discord.Embed(
                    description = f'{member.mention} {t["args"]["logs"]["enter"]} `{depois.channel}`',
                    color = 0x00ff19)
                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)
                    try:
                        w: discord.Webhook = await self.bot.fetch_webhook(db['lvoice']['webhook'])
                        await w.send(embed = e)
                    except:
                        webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')
                        await dbmoderation.logs('lvoice',True,member.guild,db['lvoice']['id'], webhook.id)
                        w: discord.Webhook = await self.bot.fetch_webhook(db['lvoice']['webhook'])
                        await w.send(embed = e)
                    return
                if depois.channel == None:
                    e: discord.Embed = discord.Embed(
                    description = f'{member.mention} {t["args"]["logs"]["exit"]} `{antes.channel}`',
                    color = 0xff0000)
                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)
                    try:
                        w: discord.Webhook = await self.bot.fetch_webhook(db['lvoice']['webhook'])
                        await w.send(embed = e)
                    except:
                        webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')
                        await dbmoderation.logs('lvoice',True,member.guild,db['lvoice']['id'], webhook.id)
                        w: discord.Webhook = await self.bot.fetch_webhook(db['lvoice']['webhook'])
                        await w.send(embed = e)
                    return
                if antes.channel != depois.channel:
                    e: discord.Embed = discord.Embed(
                    description = t['args']['logs']['semove'].format(member.mention, antes.channel.mention, depois.channel.mention),
                    color = 0xfff000)
                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)
                    try:
                        w: discord.Webhook = await self.bot.fetch_webhook(db['lvoice']['webhook'])
                        await w.send(embed = e)
                    except:
                        webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')
                        await dbmoderation.logs('lvoice',True,member.guild,db['lvoice']['id'], webhook.id)
                        w: discord.Webhook = await self.bot.fetch_webhook(db['lvoice']['webhook'])
                        await w.send(embed = e)
                    return
            if db['lmic']['True?'] == True:
                t: dict = translates(member.guild)
                if antes.self_mute:
                    e: discord.Embed = discord.Embed(
                    description = f'{member.mention} {t["args"]["logs"]["sedesmute"]} `{depois.channel}`',
                    color = 0x00ff19)
                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)
                    try:
                        w: discord.Webhook = await self.bot.fetch_webhook(db['lmic']['webhook'])
                        await w.send(embed = e)
                    except:
                        webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')
                        await dbmoderation.logs('lmic',True,member.guild,db['lmic']['id'], webhook.id)
                        w: discord.Webhook = await self.bot.fetch_webhook(db['lmic']['webhook'])
                        await w.send(embed = e)
                elif depois.self_mute:
                    e: discord.Embed = discord.Embed(
                    description = f'{member.mention} {t["args"]["logs"]["semute"]} `{depois.channel}`',
                    color = 0xfff000)
                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)
                    try:
                        w: discord.Webhook = await self.bot.fetch_webhook(db['lmic']['webhook'])
                        await w.send(embed = e)
                    except:
                        webhook: discord.Webhook = await channel.create_webhook(name = 'Markuus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')
                        await dbmoderation.logs('lmic',True,member.guild,db['lmic']['id'], webhook.id)
                        w: discord.Webhook = await self.bot.fetch_webhook(db['lmic']['webhook'])
                        await w.send(embed = e)
        except:
            None

def setup(bot:commands.Bot):
    bot.add_cog(eventslogs(bot))