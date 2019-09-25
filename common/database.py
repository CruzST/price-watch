import pymongo
from typing import Dict



class Database:
    # URI = 'mongodb://127.0.0.1:27017/pricing'
    # DATABASE = pymongo.MongoClient(URI).get_database()

    DATABASE = pymongo.MongoClient("mongodb+srv://cruzst:pricingdb@pricing-rjzac.mongodb.net/test?retryWrites=true&w=majority").get_database()

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        # find returns a cursor
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        # find_one returns an object/dictionary
        # pymongo has the find_one method
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict):
        # upsert will add element instead of update if it is not found
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict):
        return Database.DATABASE[collection].remove(query)