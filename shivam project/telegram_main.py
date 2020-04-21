from telethon import sync ,functions,types
import requests
from pymongo import MongoClient
from datetime import datetime
import mongo_connect as mc
import telegram_connect as tc
import csv
import random

class telegram:
    def __init__(self,client,col):
        self.client = client
        self.col = col
        pass
    def insert_user_to_db(self,user): 
        try:
            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            # gender = requests.get("https://api.genderize.io/?name={}".format(user.first_name)).json()
            # user.first_name
            x = self.col.insert_one(
            {   
                "telegram_id":user.id,
                "telegram_username":user.username,
                "userinfo":{
                            "firstname":user.first_name,
                            "lastname":user.last_name,
                            "gender":"gender['gender']",
                            "age":"",
                            "mobile_no":user.phone,
                            "pref_cat":[]
                            },
                "created":date,
                "updated":None,
                "access_hash":user.access_hash,
                "invite_status":False,
                "membership_status":False,
            })
            return True
        except:
            print("duplicate")
            return False
    async def insert_user_from_group(self,group_id,limit):
        count = 0
        try:  
            async for user in self.client.iter_participants(group_id,limit=limit,aggressive=True):
                if self.insert_user_to_db(user):
                    count+=1
                pass        
        except:
            print(group_id)
            errorgroup = await self.client.get_entity(group_id)  
            print(errorgroup.stringify()) 
        print(count,"- unique users are inserted from group")                        
    async def insert_user_from_csv(self,file_path,col_name):
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            inserted_user = 0
            for row in csv_reader:
                if row[col_name]:
                    result = await self.client(functions.contacts.ImportContactsRequest(
                            contacts=[types.InputPhoneContact(
                                    client_id=random.randrange(-2**63, 2**63),
                                    phone=row[col_name],
                                    first_name='',
                                    last_name=''
                            )]
                    ))

                    if (result.users):
                        # print(result.users[0].id)

                        if self.insert_user_to_db(result.users[0]):
                            print(row["firstname"])
                            inserted_user+=1
        print(inserted_user,"- unique users are inserted from csv file")             

                
