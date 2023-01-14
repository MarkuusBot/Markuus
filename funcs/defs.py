from functools import cache, lru_cache
import discord
from db.moderation import mod, dbmoderation
from json import load

with open('translate/enUS.json', encoding = 'utf-8') as f:
    enUS = load(f)
with open('translate/ptBR.json', encoding = 'utf-8') as f:
    ptBR = load(f)
with open('translate/esES.json', encoding = 'utf-8') as f:
    esES = load(f)
with open('translate/frFR.json', encoding = 'utf-8') as f:
    frFR = load(f)

def better_time(cd: int) -> str:

    time: str = f"{cd} s"
    if cd > 60:
        minutes: int = cd - (cd % 60)
        seconds: int = cd - minutes
        minutes: int = int(minutes / 60)
        time: str = f"{minutes}min {seconds}s"
        if minutes > 60:
            hoursglad: int = minutes - (minutes % 60)
            hours = int(hoursglad / 60)
            minutes: int = minutes - (hours*60)
            time: str = f"{hours}h {minutes}min {seconds}s"

    return time

def translates(guild: discord.Guild) -> dict:

    try:

        match mod.find_one({'_id': guild.id})['lang']:
            case 'pt-br':lang: dict = ptBR
            case 'en-us':lang: dict = enUS
            case 'fr-fr':lang: dict = frFR
            case 'es-es':lang: dict = esES
        return lang

    except:
        dbmoderation.lang('lang', 'en-us', guild)
        
        translates(guild)

@lru_cache
def upModules(guild: discord.Guild) -> None:

    modulesName = ['economia', 'moderação', 'diverção', 'gerais']
    vali=1
    while True:

        dbmoderation.modules(guild,modulesName[vali-1], True)

        if vali != modulesName.__len__(): vali += 1
        else: break