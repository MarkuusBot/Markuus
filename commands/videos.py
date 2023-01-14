import discord as discord

from discord.ext import commands
from discord import slash_command
from funcs.checks import NoVote, moduleCheck, vote
from funcs.defs import translates
from funcs.videos import *

class videos(commands.Cog):

    def __init__(self, bot:commands.Bot):
        
        self.bot = bot

    @slash_command(name = 'lula_maromba', description = 'Um meme do lula maromba')
    @moduleCheck('diverção')
    @vote()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def lulamaromba(self, interaction:discord.Interaction, member: discord.Member = None):

        t: dict = translates(interaction.guild)

        if member == None: member = interaction.user
            
        await member.display_avatar.replace(size = 128).save('./videos/img/membro.png')
        await interaction.response.send_message(t['args']['lulamaromba']['preparevideo'])
        await lulamarombafuncvideo('./videos/img/membro.png')
        await interaction.channel.send(content = t['args']['lulamaromba']['herevideo'].format(interaction.user.mention),
        file = discord.File('./videos/videosave/lulamaromba.mp4'))

def setup(bot:commands.Bot):
    bot.add_cog(videos(bot))