import discord, requests

from discord.ext import commands
from discord import slash_command
from utils.loader import configData
from db.economy import dbeconomy

class dono(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(name = 'giveedinhos',guild_ids = [929181582571503658])
    async def SetM(self,ctx, id,dindin: int):

        user = self.bot.get_user(id)

        dbeconomy.update_bank(user, + dindin)

        try:

            await user.send(f'Seus {dindin} edinhos foram setados <@{id}>')

            await ctx.send(f'Foram dados {dindin} edinhos para <@{id}>')

        except:

            await ctx.send(f'Foram dados {dindin} edinhos para <@{id}>')

    @slash_command(name = 'removeedinhos',guild_ids = [929181582571503658])
    async def RmvM(self,ctx, id: int, dindin: int):

        user = self.bot.get_user(id)
            
        await ctx.send(f'Foram removidos {dindin} edinhos para <@{id}>')

        dbeconomy.update_bank(user, - dindin)

    @slash_command(name = 'stats', guild_ids = [929181582571503658])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def stats(self, ctx: discord.Interaction, bot):
        
        if bot == 'MK':

            bot = 1010629199159107665
        
        elif bot == 'MKC':

            bot = 1012121641947517068

        res = requests.get(f'https://api.squarecloud.app/v1/public/status/{bot}', headers = {'Authorization': configData['squarekey']}).json()

        embed = discord.Embed()

        embed.add_field(name = 'HOST', value = f'<@{bot}>')
        embed.add_field(name = 'CPU', value = res['response']['cpu'])
        embed.add_field(name = 'RAM', value = res['response']['ram'])
        embed.add_field(name = 'SSD', value = res['response']['storage'])
        embed.add_field(name = 'NETWORK', value = res['response']['network'])
        embed.add_field(name = 'REQUESTS', value = res['response']['requests'])

        await ctx.respond(embed = embed)

    @slash_command(name = 'backup', guild_ids = [929181582571503658])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def backup(self, ctx: discord.Interaction):

        res = requests.get(f'https://api.squarecloud.app/v1/public/backup/{self.bot.user.id}', headers = {'Authorization': configData['squarekey']}).json()

        await ctx.user.send(res['response']['downloadURL'])

    @slash_command(name = 'init', guild_ids = [929181582571503658])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def init(self, ctx: discord.Interaction, bot):

        if bot == 'MK':

            bot = 1010629199159107665
        
        elif bot == 'MKC':

            bot = 1012121641947517068

        requests.post(f'https://api.squarecloud.app/v1/public/start/{bot}', headers = {'Authorization': configData['squarekey']}).json()

        await ctx.user.send(f'{bot} iniciado')

    @slash_command(name = 'stop', guild_ids = [929181582571503658])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def stop(self, ctx: discord.Interaction, bot):

        if bot == 'MKC':

            bot = 1010629199159107665
        
        elif bot == 'MK':

            bot = 1012121641947517068

        requests.post(f'https://api.squarecloud.app/v1/public/stop/{bot}', headers = {'Authorization': configData['squarekey']}).json()

        await ctx.user.send(f'{bot} iniciado')

def setup(bot:commands.Bot):
    bot.add_cog(dono(bot))