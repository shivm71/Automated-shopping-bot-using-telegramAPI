from pymongo import MongoClient
mongoclient = MongoClient("mongodb+srv://test:test@cluster0-qgcs5.mongodb.net/test?retryWrites=true&w=majority")
db = mongoclient['telegram']
