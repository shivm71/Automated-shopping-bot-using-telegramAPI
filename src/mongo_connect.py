from pymongo import MongoClient
mongoclient = MongoClient("mongodb://jarvis:datamantra890@127.0.0.1/crystal?retryWrites=true&w=majority")
#mongoclient = MongoClient("mongodb+srv://test:test@cluster0-qgcs5.mongodb.net/test?retryWrites=true&w=majority")
db = mongoclient['crystal']