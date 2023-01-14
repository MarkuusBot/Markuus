import random
import discord

from discord.ext import commands
from discord import slash_command, option
from embeds.actions import biteEmbed, cafuneEmbed, hugEmbed, kissEmbed, lickEmbed, punchEmbed, slapEmbed
from funcs.checks import moduleCheck
from funcs.defs import translates

class actions(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:

        self.bot: commands.Bot  = bot

    @slash_command(name = 'flip_coin', 
        description = 'Flip a coin', 
        guild_only = True,
        name_localizations = {
            'en-US': 'flip_coin',
            'en-GB': 'flip_coin',
            'es-ES': 'tirar_la_moneda',
            'pt-BR': 'girar_moeda',
            'fr': 'pièce_de_monnaie'
        },
        description_localizations = {
            'en-US': 'Play heads or tails',
            'en-GB': 'Play heads or tails',
            'es-ES': 'Juega cara o cruz',
            'pt-BR': 'Joga cara ou coroa',
            'fr': 'Jouer à pile ou face'
        })
    @moduleCheck('diverção')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def flipcoin(self, Interaction: discord.Interaction) -> None:

        t: dict = translates(Interaction.guild)

        c: int = random.choice([1,2])

        match c:
            case 1: await Interaction.response.send_message(t['args']['actions']['flip1'])
            case 2: await Interaction.response.send_message(t['args']['actions']['flip2'])

    @slash_command(name = 'hug',
        description = 'hug one member',
        guild_only = True,
        name_localizations = {
            'en-US': 'hug',
            'en-GB': 'hug',
            'es-ES': 'abrazo',
            'pt-BR': 'abraço',
            'fr': 'câliner'
        },
        description_localizations = {
            'en-US': 'Hug a member',
            'en-GB': 'Hug a member',
            'es-ES': 'Abrazar a un miembro',
            'pt-BR': 'Abraça um membro',
            'fr': 'Embrasser un membre'
        })
    @moduleCheck('diverção')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Select one member')
    async def hug(self, Interaction: discord.Interaction, member: discord.Member) -> None:

        await hugEmbed(self.bot, Interaction, Interaction.user, member)

    @slash_command(name = 'kiss',
        description = 'kiss one member',
        guild_only = True,
        name_localizations = {
            'en-US': 'kiss',
            'en-GB': 'kiss',
            'es-ES': 'beso',
            'pt-BR': 'beijar',
            'fr': 'embrasser'
        },
        description_localizations = {
            'en-US': 'Kiss a member',
            'en-GB': 'Kiss a member',
            'es-ES': 'Beso a un miembro',
            'pt-BR': 'Beija um membro',
            'fr': 'Embrasser un membre'
        })
    @moduleCheck('diverção')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Select one member')
    async def kiss(self, Interaction: discord.Interaction, member: discord.Member) -> None:

        await kissEmbed(self.bot,Interaction,Interaction.user, member)

    @slash_command(name = 'slap',
        description = 'Slap one member',
        guild_only = True,
        name_localizations = {
            'en-US': 'slap',
            'en-GB': 'slap',
            'es-ES': 'bofetada',
            'pt-BR': 'tapa',
            'fr': 'gifler'
        },
        description_localizations = {
            'en-US': 'slap a member',
            'en-GB': 'slap a member',
            'es-ES': 'bofetada a un miembro',
            'pt-BR': 'Estapeia um membro',
            'fr': 'Gifler un membre'
        })
    @moduleCheck('diverção')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Select one member')
    async def slap(self, Interaction: discord.Interaction, member: discord.Member) -> None:

        await slapEmbed(self.bot, Interaction, Interaction.user, member)

    @slash_command(name = 'punch',
        description = 'Punch one member',
        guild_only = True,
        name_localizations = {
            'en-US': 'punch',
            'en-GB': 'punch',
            'es-ES': 'golpear',
            'pt-BR': 'socar',
            'fr': 'gifler'
        },
        description_localizations = {
            'en-US': 'Punch a member',
            'en-GB': 'Punch a member',
            'es-ES': 'Golpea a un miembro',
            'pt-BR': 'Soca um membro',
            'fr': 'Gifler un membre'
        })
    @moduleCheck('diverção')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Select one member')
    async def punch(self, Interaction: discord.Interaction, member: discord.Member) -> None:

        await punchEmbed(self.bot, Interaction, Interaction.user, member)

    @slash_command(name = 'bite',
        description = 'Bite one member',
        guild_only = True,
        name_localizations = {
            'en-US': 'bite',
            'en-GB': 'bite',
            'es-ES': 'morder',
            'pt-BR': 'morder',
            'fr': 'mordre'
        },
        description_localizations = {
            'en-US': 'Bite a member',
            'en-GB': 'Bite a member',
            'es-ES': 'Morder a un miembro',
            'pt-BR': 'Morde um membro',
            'fr': 'Mordre un membre'
        })
    @moduleCheck('diverção')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Select one member')
    async def bite(self, Interaction: discord.Interaction, member: discord.Member) -> None:

        await biteEmbed(self.bot, Interaction, Interaction.user, member)

    @slash_command(name = 'lick',
        description = 'Lick a member',
        guild_only = True,
        name_localizations = {
            'en-US': 'lick',
            'en-GB': 'lick',
            'es-ES': 'lamer',
            'pt-BR': 'lamber',
            'fr': 'lécher'
        },
        description_localizations = {
            'en-US': 'Lick a member',
            'en-GB': 'Lick a member',
            'es-ES': 'Lamer a un miembro',
            'pt-BR': 'Lambe um membro',
            'fr': 'Lécher un membre'
        })
    @moduleCheck('diverção')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Mention member')
    async def lick(self, Interaction: discord.Interaction, member: discord.Member) -> None:

        await lickEmbed(self.bot, Interaction, Interaction.user, member)

    @slash_command(name = 'cafune',description = 'Faz um cafune em alguem',guild_only = True)
    @moduleCheck('diverção')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Mencione um member')
    async def pat(self, Interaction: discord.Interaction, member: discord.Member) -> None:

        await cafuneEmbed(self.bot, Interaction, Interaction.user, member)

def setup(bot:commands.Bot):
    bot.add_cog(actions(bot))