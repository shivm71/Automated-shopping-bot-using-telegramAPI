from pymongo import MongoClient
host = str(input("enter host defualt = cluster0-qgcs5.mongodb.net/test?retryWrites=true&w=majority   - "))
port = str(input("enter port default = 27017    -"))
username = str(input("enter username default = test   -"))
password = str(input("enter password default = test   -"))
db_name = str(input("enter db_name default = telegram   -"))
uri = "mongodb://%s:%s@%s" % (username, password, host)
mongoclient = MongoClient(uri,port)
db = mongoclient[db_name]
col = db["users"]
col.create_index('telegram_id',unique=True,name = "index1")
col.create_index([('telegram_id',1),('invite_status',1),("membership_status",1)],name = "index2")
col.create_index('created',name = "index3")

col = db['groups']
col.create_index("group_id",unique = True,name = "index1")