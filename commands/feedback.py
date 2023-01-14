import discord as discord

from discord.ext import commands
from discord import slash_command, option
from db.moderation import dbmoderation, mod
from funcs.defs import translates

class feedback(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot: commands.Bot = bot

    @slash_command(name = "modules",
        description = "Enable modules and disable",
        guild_only = True,
        name_localizations = {
            "en-US": "modules",
            "en-GB": "modules",
            "es-ES": "módulos",
            "pt-BR": "módulos",
            "fr": "modules"
        },
        description_localizations = {
            "en-US": "Activate and deactivate a module",
            "en-GB": "Activate and deactivate a module",
            "es-ES": "Activar y desactivar un módulo",
            "pt-BR": "Ativa e desativa um modulo",
            "fr": "Activer et désactiver un module"
        }
    )
    @option(name = "module",
        description = "Select the module",
        choices = ["economia/economy","moderação/moderation", "gerais/generals", "diverção/fun"],
        name_localizations = {
            "en-US": "module",
            "en-GB": "module",
            "es-ES": "módulo",
            "pt-BR": "módulo",
            "fr": "module"
        },
        description_localizations = {
            "en-US": "Select the module",
            "en-GB": "Select the module",
            "es-ES": "seleccione el módulo",
            "pt-BR": "Selecione o modulo",
            "fr": "sélectionner le module"
        }
    )
    @option(name = "action",
        choices = ["enable","disable"])
    async def modules(self, interaction: discord.Interaction, module: str, action: str):

        t: dict = translates(interaction.guild)

        match module: 
            case "economia/economy": module: str = "economia"
            case "moderação/moderation": module: str = "moderação"
            case "gerais/generals": module: str = "gerais"
            case "diverção/fun": module: str = "diverção"

        match action:

            case "enable":

                if mod.find_one({"_id": interaction.guild.id})["modules"][module] == True:
                    await interaction.response.send_message(t['args']['modulealreadyenable'])
                else:
                    dbmoderation.modules(interaction.guild, module, True)
                    await interaction.response.send_message(t["args"]['moduleenablesucess'])
            
            case "disable":

                if mod.find_one({"_id": interaction.guild.id})["modules"][module] == False:
                    await interaction.response.send_message(t['args']['modulealreadydisable'])
            
                else:
                    dbmoderation.modules(interaction.guild, module, False)
                    await interaction.response.send_message(t["args"]['moduledisablesucess'])

    @slash_command(name = "sugest",
        description = "Send a suggestion to my owner",
        guild_only = True,
        name_localizations = {
            "en-US": "sugest",
            "en-GB": "sugest",
            "es-ES": "sugerencia",
            "pt-BR": "sugestão",
            "fr": "suggestion"
        },
        description_localizations = {
            "en-US": "Send a suggestion to my owner",
            "en-GB": "Send a suggestion to my owner",
            "es-ES": "Enviar una sugerencia a mi dueño",
            "pt-BR": "Envia uma sugestão para meu dono",
            "fr": "Envoyer une suggestion à mon propriétaire"
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = "sugest", description = "Escreva a sugestão")
    @commands.cooldown(1,5, commands.BucketType.user)
    async def sugest(self, interaction: discord.Interaction, sugestão):

        t: dict = translates(interaction.guild)
        channel: discord.TextChannel = self.bot.get_channel(int(1012123748637343756))
        emojiTicket: discord.Emoji = self.bot.get_emoji(1044752355163394119)

        embed: discord.Embed = discord.Embed(
            title = "Sugest",
            description = f"""
                **Enviado por:** \n {interaction.author}
                **Sugestão:** \n {sugestão}
                **No server:** \n {interaction.guild.name}
                **ID:** {interaction.author.id}
                """
            )

        await interaction.response.send_message(f'{emojiTicket} {t["args"]["feedback"]["sugest"]}', ephemeral = True)

        await channel.send(embed=embed)

    @slash_command(name = "report",
        description = "Send a report to my owner",
        guild_only = True,
        name_localizations = {
            "en-US": "report",
            "en-GB": "report",
            "es-ES": "reportar",
            "pt-BR": "reportar",
            "fr": "signaler"
        },
        description_localizations = {
            "en-US": "Send a report to my owner",
            "en-GB": "Send a report to my owner",
            "es-ES": "Enviar un informe a mi propietario",
            "pt-BR": "Envia um report para meu dono",
            "fr": "Envoyer un rapport à mon propriétaire"
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = "report", description = "Escreva o report")
    @commands.cooldown(1,5, commands.BucketType.user)
    async def report(self, interaction: discord.Interaction, report):

        t: dict = translates(interaction.guild)
        channel: discord.TextChannel = self.bot.get_channel(int(1012123813070262312))
        emojiTicket: discord.Emoji = self.bot.get_emoji(1044752355163394119)

        embed: discord.Embed = discord.Embed(
            title = "report",
            description = f"""
                    **Enviado por:** \n {interaction.author}
                    **Report:** \n {report}
                    **No server:** \n {interaction.guild.name}
                    **ID:** {interaction.author.id}
                    """
                )

        await interaction.response.send_message(f'{emojiTicket} {t["args"]["feedback"]["report"]}', ephemeral = True)

        await channel.send(embed=embed)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(feedback(bot))