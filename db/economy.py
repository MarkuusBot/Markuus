from pymongo import MongoClient
from utils.loader import configData
from pymongo.collection import Collection
from pymongo.database import Database

cluster: MongoClient = MongoClient(configData['mongokey'])
db: Database = cluster[configData['database']]
bank: Collection = db['BANK']
inv: Collection = db['INV']

class dbeconomy:
    
    def update_bank(id, edinhos: int):

        if id is not None:
            if bank.count_documents({"_id":id.id}) == 0:
                bank.insert_one({"_id":id.id, "Nome":id.name, "edinhos": edinhos})
            bank.update_one({"_id": id.id}, {"$inc": {"Edinhos": edinhos}}, upsert = True)