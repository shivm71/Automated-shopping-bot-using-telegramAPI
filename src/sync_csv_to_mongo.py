import csv
import random
import mongo_connect as mc
import telegram_connect as tc
from telegram_main import telegram
from telethon import sync ,functions,types
collection = mc.db["users"]
telegram_obj = telegram(tc.client,collection)

async def insert_user_from_csv(file_path,col_name):
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        inserted_user = 0
        for row in csv_reader:
            if row[col_name]:
                result = await tc.client(functions.contacts.ImportContactsRequest(
                    contacts=[types.InputPhoneContact(
                        client_id=random.randrange(-2**63, 2**63),
                        phone=row[col_name],
                        first_name='',
                        last_name=''
                    )]
                ))

                if (result.users):
                    # print(result.users[0].id)
                    if telegram.insert_user_to_db(telegram_obj,result.users[0]):
                        print(row["firstname"])
                        inserted_user+=1
    print(inserted_user,"- unique users are inserted from csv file")


tc.client.loop.run_until_complete(insert_user_from_csv("../resource/user.csv","phone"))  # insert_user_from_csv(self,file_path,col_name)