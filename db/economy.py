from pymongo import MongoClient
from utils.loader import configData

cluster = MongoClient(configData['mongokey'])
db = cluster[configData['database']]
bank = db['BANK']
inv = db['INV']

class dbeconomy:

    def update_bank(id, edinhos: int):

        if id is not None:
            if bank.count_documents({"_id":id.id}) == 0:
                bank.insert_one({"_id":id.id, "Nome":id.name, "Edinhos": edinhos})
            bank.update_one({"_id": id.id}, {"$inc": {"Edinhos": edinhos}}, upsert = True)