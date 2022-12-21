import discord,os, json
from discord import Bot as BotBase

with open("utils/config.json", 'r') as f:
    configData = json.load(f)

__title__ = "MarkuusBot"
__author__ = "Marciel404"
__license__ = "MIT"
__copyright__ = "Copyright 2022-present Marciel404"
__version__ = "3.5.0"

class client(BotBase):
    
    def __init__(self):
        
        super().__init__(
            command_prefix = "!",
            intents = discord.Intents(
                bans = True,
                emojis = True,
                guild_messages = True,
                guilds = True,
                members = True,
                message_content = True,
                voice_states = True
            ),
            case_insensitive = True,
            help_command = None
        )   
        
    def loadcogs(self):
        pastaname = 'cogs'
        for filename in os.listdir(f'./{pastaname}'):
            for commands in os.listdir(f'./{pastaname}/{filename}'):
                if commands.endswith('.py') and not commands.startswith('__'):
                    self.load_extensions(f'{pastaname}.{filename}.{commands[:-3]}')

    def __run__(self):
        
        self.loadcogs()

        self.run(configData['token'])