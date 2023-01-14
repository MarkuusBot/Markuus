import discord
import os
import json

from discord import Bot as BotBase
from discord.ext import commands

with open("utils/config.json", 'r') as f:
    configData = json.load(f)

__title__: str = "MarkuusBot"
__author__: str = "Marciel404"
__license__: str = "MIT"
__copyright__: str = "Copyright 2022-present Marciel404"
__version__: str = "3.6.0"

class client(BotBase):
    
    def __init__(self):
        
        super().__init__(
            command_prefix = commands.when_mentioned_or(configData["prefix"]),
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

        for commands in os.listdir('./commands'):
            if commands.endswith(".py") and not commands.startswith("__"):
                self.load_extensions('commands.{}'.format(commands[:-3]))
        
        for events in os.listdir('./plugins'):
            if events.endswith(".py") and not events.startswith("__"):
                self.load_extensions('plugins.{}'.format(events[:-3]))

    def __run__(self):
        
        self.loadcogs()

        self.run(configData['token'])