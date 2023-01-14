import discord

from discord.ext import commands
from discord import slash_command
from db.economy import dbeconomy

class dono(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot: commands.Bot = bot

    @slash_command(name = 'giveedinhos',guild_ids = [929181582571503658])
    async def SetM(self, ctx: discord.Interaction, id: int, dindin: int) -> None:

        user: discord.User = self.bot.get_user(id)

        dbeconomy.update_bank(user, + dindin)

        try:

            await user.send(f'Seus {dindin} edinhos foram setados <@{id}>')

            await ctx.send(f'Foram dados {dindin} edinhos para <@{id}>')

        except:

            await ctx.send(f'Foram dados {dindin} edinhos para <@{id}>')

    @slash_command(name = 'removeedinhos',guild_ids = [929181582571503658])
    async def RmvM(self,ctx: discord.Interaction, id: int, dindin: int) -> None:

        user: discord.User = self.bot.get_user(id)
            
        await ctx.send(f'Foram removidos {dindin} edinhos para <@{id}>')

        dbeconomy.update_bank(user, - dindin)

def setup(bot:commands.Bot):
    bot.add_cog(dono(bot))