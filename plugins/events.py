import discord

from discord.ext import commands
from db.moderation import dbmoderation, mod, advdb
from funcs.checks import ModuleDisable, NoVote
from funcs.defs import better_time, translates, upModules
from pymongo.collection import Collection

class events(commands.Cog):

    def __init__(self, bot: commands.Bot):

        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self, interaction: discord.Interaction, error):

        errorEmoji: discord.Emoji = self.bot.get_emoji(1044750438978818049)

        t: dict = translates(interaction.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await interaction.response.send_message(f'{errorEmoji} || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
        
        if isinstance(error, ModuleDisable):

            await interaction.response.send_message(f"{errorEmoji} || {error}", ephemeral = True)

        if isinstance(error, NoVote):

            await interaction.response.send_message(f"{errorEmoji} || {error}", ephemeral = True)
        
        if isinstance(error, commands.BotMissingPermissions):
            
            await interaction.response.send_message(f'{errorEmoji} || {t["args"]["mod"]["botnotpermission1"]} "Ban_Members" {t["args"]["mod"]["botnotpermission2"]}')

        if isinstance(error, commands.MissingPermissions):
            
            await interaction.response.send_message(f"{errorEmoji} || {t['args']['mod']['notpermission']}", ephemeral = True)

        if isinstance(error, commands.MemberNotFound):

            await interaction.response.send_message(f'{errorEmoji} || {t["args"]["mod"]["bannotfound"]}')

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):

        dbmoderation.lang('lang', 'en-us', guild)
        upModules(guild)
            
    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):

        mod.find_one_and_delete({'_id': guild.id})

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User):

        if advdb.count_documents({"_id": f'{guild.id}_{user.id}'}) == 1:
            advdb.find_one_and_delete({"_id": f'{guild.id}_{user.id}'})

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):

        try:
            db: Collection = mod.find_one({'_id': member.guild.id})
            if db['autorole']['True?'] == True:
                try:
                    await member.add_roles(discord.utils.get(member.guild.roles, id=db['autorole']['id']))
                except:
                    t: dict = translates(member.guild)
                    try:
                        l: discord.TextChannel = self.bot.get_channel(mod.find_one({'_id': member.guild.id})['chatlogs'])
                        await l.send(
                            f"{t['args']['error']['autorole']['notpermission']} {discord.utils.get(member.guild.roles, id=db['autorole']['id']).mention}")
                    except:
                        try:
                            await member.guild.owner.send(
                                f"{t['args']['error']['autorole']['notpermission']} ''{discord.utils.get(member.guild.roles, id=db['autorole']['id'])}'' {t['args']['error']['autorole']['notpermission2']}")
                        except:
                            await member.guild.text_channels[0].send(
                                f"{t['args']['error']['autorole']['notpermission']} {discord.utils.get(member.guild.roles, id=db['autorole']['id']).mention} {t['args']['error']['autorole']['notpermission2']}")
        except:
            None

    @commands.Cog.listener()
    async def on_ready(self):

        await self.bot.change_presence(activity=discord.Game(name="/help"))
        print(f'Eu entrei como {self.bot.user}')

def setup(bot: commands.Bot):
    bot.add_cog(events(bot))
