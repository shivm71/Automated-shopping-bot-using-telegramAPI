from pymongo import MongoClient
mongoclient = MongoClient("mongodb://jarvis:datamantra8890@127.0.0.1/crystal?retryWrites=true&w=majority")
db = mongoclient['crystal']
