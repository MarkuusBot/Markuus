import discord as discord

from discord.ext import commands
from discord import slash_command, option
from db.moderation import advdb
from funcs.checks import moduleCheck, vote
from funcs.defs import translates
from pymongo.collection import Collection

class membersreport(commands.Cog):

    def __init__(self, bot:commands.Bot):
        
        self.bot = bot

    @slash_command(
        guild_only = True,
        name = 'warns',
        description = 'Mostra as advs de um membro',
        )
    @moduleCheck('moderação')
    @commands.cooldown(1,5, commands.BucketType.user)
    @vote()
    @option(name = 'membro', description = 'Escolha o membro a ver a advertencia')
    async def veradv(self, ctx: discord.Interaction, member: discord.Member):

        t:dict = translates(ctx.guild)
        if advdb.count_documents({ "_id":f'{ctx.guild.id}_{member.id}'}) == 1:
            rankings: Collection = advdb.find_one({'_id': f'{ctx.guild.id}_{member.id}'})
            embed: discord.Embed = discord.Embed(title = f"***{member.name}***")
            i = 1
            while True:
                hgc: Collection = rankings[f'{t["args"]["adv"]}{i}']
                embed.add_field(name=f"{t['args']['adv']}{i}", value=t["args"]["mod"]["logadv"].format(hgc[0],hgc[1],hgc[2]), inline=False)
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon}")
                if i == advdb.find_one({'_id': f'{ctx.guild.id}_{member.id}'})['qnt']:
                    break
                else:
                    i += 1
            await ctx.response.send_message()(embed=embed)
        else: 
            await ctx.response.send_message()(t['args']['notadv'], ephemeral = True)
            
def setup(bot:commands.Bot):
    bot.add_cog(membersreport(bot))