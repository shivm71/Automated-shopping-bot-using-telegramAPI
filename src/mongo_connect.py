from pymongo import MongoClient
mongoclient = MongoClient("")
db = mongoclient['crystal']
