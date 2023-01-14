from pymongo import MongoClient
from utils.loader import configData
from pymongo.collection import Collection
from pymongo.database import Database

cluster: MongoClient = MongoClient(configData['mongokey'])
db: Database = cluster[configData['database']]
perf: Collection = db['PROFILE']

class dbmember:

    def upPerfil(member, oq, name, value):
        if member is not None:
            perf.update_one( { "_id": member.id}, {'$set':{oq:{'name': name,'value':value}}}, upsert = True )