import asyncio
import csv
import random
import mongo_connect as mc
import telegram_connect as tc
from telegram_main import telegram
from telethon import sync ,functions,types,errors
from datetime import date, timedelta
import sys
collection = mc.db["users"]

telegram_obj = telegram(tc.client,collection)
async def insert_user_from_csv(file_path, rows_to_skip,col_name = "phone",):
    client = tc.client 
    session_name = tc.session_name 
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in range(int(rows_to_skip)):
            next(csv_reader)
        inserted_user = 0
        count = rows_to_skip
        print("Starting pushing data from csv to mongo-")
        for row in csv_reader:
            if row[col_name]:
                count+=1
                while(True):
                    try: 
                        result = await client(functions.contacts.ImportContactsRequest(
                            contacts=[types.InputPhoneContact(
                                client_id=random.randrange(-2**63, 2**63),
                                phone='+91'+row[col_name][-10:],
                                first_name='',
                                last_name=''
                            )]
                        ))
                        break
                    except errors.FloodWaitError as e:
                        print('FloodWaitError for session:', session_name, ' time:', e.seconds)
                        client,session_name = await tc.get_next_client(client,session_name,e.seconds)
                try:
                    if (result.users):
                        user = result.users[0]
                        if (hasattr(user.status,'was_online') and user.status.was_online.date() > (date.today() - timedelta(days=60))):
                            print("found user at:", count, "user_id:", row['user_id'])
                            user.email = row['email']
                            if (user.first_name is None):
                                user.first_name = row['firstname']
                            if telegram.insert_user_to_db(telegram_obj,user):
                                inserted_user+=1
                except Exception as e:
                    print("Exception after fetching user",e)
    print(inserted_user,"- unique users are inserted from csv file")

def main(rows_to_skip):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(insert_user_from_csv("../resource/user.csv",rows_to_skip, "phone"))  # insert_user_from_csv(self,file_path,col_name)

if __name__ == "__main__":
    main(int(sys.argv[1]))