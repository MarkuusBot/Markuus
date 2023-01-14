import discord
from utils.loader import configData
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

cluster: MongoClient = MongoClient(configData['mongokey'])
db: Database = cluster[configData['database']]
mod: Collection = db['MOD']
advdb: Collection = db['ADV']

class dbmoderation:

    def lang(opt,oq,guild: discord.Guild):

        if opt is not None:
            if mod.count_documents({"_id":guild.id}) == 0:
                mod.insert_one({"_id":guild.id, "Nome":guild.name})
            mod.update_one({"_id": guild.id}, {"$set": {f"{opt}": oq}}, upsert = True)

    def autorole(opt,oq,guild,id):

        if opt is not None:
            if mod.count_documents({"_id":guild.id}) == 0:
                mod.insert_one({"_id":guild.id, "Nome":guild.name})
            mod.update_one({"_id": guild.id}, {'$set': {opt: {'True?':oq,'id':id}}}, upsert = True)

    async def logs(opt,oq,guild,id, webhook):

        if opt is not None:
            if mod.count_documents({"_id":guild.id}) == 0:
                mod.insert_one({"_id":guild.id, "Nome":guild.name})
            mod.update_one({"_id": guild.id}, {'$set': {opt: {'True?': oq,'id': id, 'webhook': webhook}}},upsert = True)

    def adcadvdb(guild, author, member, qnt, motivo):
        if guild is not None:
            advdb.update_one( { "_id":f'{guild.id}_{member.id}'}, {'$set':{qnt:[author.id,member.id,motivo]}}, upsert = True )

    def rmvadvdb(guild,author,member, qnt, motivo):
        if guild is not None:
            advdb.update_one( { "_id":f'{guild.id}_{member.id}'}, {'$unset':{qnt:[author,member.id,motivo]}})
    
    def modules(guild, module, value):

        if guild is not None:
            mod.update_one({"_id": guild.id}, {"$set":{f"modules.{module}": value}}, upsert=True)