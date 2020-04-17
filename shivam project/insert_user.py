from telethon import sync
import requests
from pymongo import MongoClient
from datetime import datetime
import mongo_connect as mc
import telegram_connect as tc
client = tc.client
col = mc.db['users']  
async def main(group_id):
    count = 0
    try:  
        async for user in client.iter_participants(group_id,limit=10,aggressive=True):
            try:
                date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                # gender = requests.get("https://api.genderize.io/?name={}".format(user.first_name)).json()
                # user.first_name
                x = col.insert_one(
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
            except:
                print("duplicate")
            count+=1
            print(count)        
    except:
        print(group_id)
        errorgroup = await client.get_entity(group_id)  
        print(errorgroup.stringify())                     
    