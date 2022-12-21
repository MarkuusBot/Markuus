import discord, random

from discord.ext import commands
from discord import slash_command, option
from funcs.defs import *
from classes.buttons import *
from db.economy import *

class economia(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @discord.slash_command(
        name = 'roll', 
        description = 'You can win from 0 to 2000 edinhos',
        guild_only = True,
        name_localizations = {
            'en-US': 'roll',
            'en-GB': 'roll',
            'es-ES': 'rodar',
            'pt-BR': 'rolar',
            'fr': 'rouler'
        },
        description_localizations = {
            'en-US': 'You can win from 0 to 2000 edinhos',
            'en-GB': 'You can win from 0 to 2000 edinhos',
            'es-ES': 'Puedes ganar de 0 a 2000 edinhos',
            'pt-BR': 'Voce pode ganhar de 0 a 2000 edinhos',
            'fr': 'Vous pouvez gagner de 0 à 2000 edinhos'
        })
    @commands.cooldown(5, 7200, commands.BucketType.user)
    async def rolar(self, ctx: discord.Interaction):

        t = translates(ctx.guild)

        rand = random.randint(0,10)

        if rand == 10:

            dbeconomy.update_bank(ctx.user, + 2000)

            await ctx.respond(f'Parabens {ctx.user.name}, {t["args"]["gan"]} 2000 edinhos')

        elif rand == 8 or 9:

            r = random.randint(100,900)

            dbeconomy.update_bank(ctx.user,r)

            await ctx.respond(f'{ctx.user.name}, {t["args"]["gan"]} {r} edinhos')

        elif rand == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7:

            r = random.randint(0,100)         

            dbeconomy.update_bank(ctx.user, + r)

            await ctx.respond(f'{ctx.user.name}, {t["args"]["gan"]} {r} edinhos')

    @slash_command(
        name = 'edinhos',
        description = 'Mostra quantas edinhos uma pessoa tem',
        guild_only = True,
        name_localizations = {
            'en-US': 'wallet',
            'en-GB': 'wallet',
            'es-ES': 'cartera',
            'pt-BR': 'carteira',
            'fr': 'portefeuille'
        },
        description_localizations = {
            'en-US': 'Shows how many edinhos you have or from the mentioned member',
            'en-GB': 'Shows how many edinhos you have or from the mentioned member',
            'es-ES': 'Muestra cuántos edinhos tienes o del miembro mencionado',
            'pt-BR': 'Mostra quantos edinhos você tem ou do membro mencionado',
            'fr': 'Montre combien de edinhos vous avez ou du membre mentionné'
        })
    @option(name = 'member', description = 'Escolha um membro')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def edinhos(self, ctx: discord.Interaction, member: discord.Member = None):

        t = translates(ctx.guild)
            
        if member == None:

            member = ctx.user

        if member.bot:

            ctx.respond(t['args']['economy']['botacount'], ephemeral = True)

            return

        if bank.count_documents({"_id": member.id}) == 0:

            dbeconomy.update_bank(member,0)

        bal = bank.find_one({"_id": member.id})
        
        em = discord.Embed(title = f"{member.name} edinhos", color = discord.Color.red())

        em.add_field(name ='LothCoin', value = bal["edinhos"])

        await ctx.respond(embed = em)

    @slash_command(
        name = 'transfer',
        description = 'Transfer edinhos for outher member',
        guild_only = True,
        name_localizations = {
            'en-US': 'transfer',
            'en-GB': 'transfer',
            'es-ES': 'transferir',
            'pt-BR': 'transferir',
            'fr': 'trasférer'
        },
        description_localizations = {
            'en-US': 'You can transfer edinhos to other people',
            'en-GB': 'You can transfer edinhos to other people',
            'es-ES': 'Puedes transferir edinhos a otras personas',
            'pt-BR': 'Trafere edinhos para um membro',
            'fr': "Vous pouvez transférer des edinhos à d'autres personnes"
        })
    @option(name = 'member', description = 'Ecolha o membro a transferir')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Transferir(self, ctx: discord.Interaction, member: discord.Member, edinhos: int):

        t = translates(ctx.guild)

        if member.bot:

            await ctx.respond(t['args']['economy']['bottransfer'], ephemeral = True)

            return
        
        if member == ctx.user:

            await ctx.respond(t['args']['economy']['notself'], ephemeral = True)

            return

        if bank.count_documents({"_id": member.id}) == 0:

            dbeconomy.update_bank(member,0)

        if bank.count_documents({"_id": ctx.user.id}) == 0:

            dbeconomy.update_bank(ctx.user,0)

        bal = bank.find_one({"_id": ctx.user.id})

        b1 = bal["edinhos"]

        if edinhos > b1:

            await ctx.respond(t['args']['economy']['notmoney'], ephemeral = True)

            return

        elif edinhos == 0:

            await ctx.respond(t['args']['economy']['>0'], ephemeral = True)

            return

        elif edinhos < 0:

            await ctx.respond(t['args']['economy']['<0'], ephemeral = True)

            return

        dbeconomy.update_bank(ctx.user,- edinhos)

        dbeconomy.update_bank(member,+ edinhos)

        await ctx.respond(t['args']['economy']['vct'].format(edinhos,member.mention))

    @slash_command(
        name = 'slot_machine',
        description = 'Slot machine bet',
        guild_only = True,
        name_localizations = {
            'en-US': 'slot_machine',
            'en-GB': 'slot_machine',
            'es-ES': 'tragamonedas',
            'pt-BR': 'caça-niquel',
            'fr': 'machine_à_sous'
        },
        description_localizations = {
            'en-US': 'Slot machine bet',
            'en-GB': 'Slot machine bet',
            'es-ES': 'Apuesta de tragamonedas',
            'pt-BR': 'Aposta no caça-niquel',
            'fr': "Pari de machine à sous"
        })
    @option(name = 'edinhos', description = 'Escolha a quantidade a jogar')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def loteria(self, ctx: discord.Interaction, edinhos:int):

        t = translates(ctx.guild)
            
        if bank.count_documents({"_id": ctx.user.id}) == 0:

            dbeconomy.update_bank(ctx.user,0)

        bal = bank.find_one({"_id": ctx.user.id})

        if edinhos > bal["edinhos"]:

            await ctx.respond(t['args']['economy']['notmoney'], ephemeral = True)

            return

        elif edinhos == 0:

            await ctx.respond(t['args']['economy']['>0'], ephemeral = True)
        
            return

        elif edinhos < 0:

            await ctx.respond(t['args']['economy']['<0'], ephemeral = True)

            return

        final = []

        for i in range(3):

            a = random.choice([':pineapple:',':grapes:',':kiwi:',])

            final.append(a)

        await ctx.respond(str(final))

        if final[0] == final[1] == final[2]:

            dbeconomy.update_bank(ctx.user,4*edinhos)

            await ctx.respond(f'{t["args"]["gan"]} {4*edinhos} edinhos!!')

        else:

            dbeconomy.update_bank(ctx.user,-1*edinhos)

            await ctx.respond( t['args']['economy']['lost'] + f' {edinhos} edinhos', ephemeral = True)

    @slash_command(
        name = 'edinhos_top', 
        description = 'Shows the rank of richest people', 
        guild_only = True,
        description_localizations = {
            'en-US': 'Shows the rank of richest people',
            'en-GB': 'Shows the rank of richest people',
            'es-ES': 'Muestra el rango de las personas más ricas',
            'pt-BR': 'Mostra o rank de pessoas mais ricas',
            'fr': "Affiche le rang des personnes les plus riches"
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    async def edinhosTOP(self, ctx: discord.Interaction):

        t = translates(ctx.guild)

        rankings = bank.find().sort("edinhos",-1)

        i=1

        embed = discord.Embed(title = f"***{t['args']['economy']['top']}***")

        for x in rankings:

            loth = x["edinhos"]

            embed.add_field(name=f"{i}: {x['Nome']}", value=f"{loth}", inline=False)

            if i == 10:

                break

            else:

                i += 1

        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon}")

        await ctx.respond(embed=embed)

    @rolar.error
    async def error(self, ctx: discord.Interaction, error):

        t = translates(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(economia(bot))