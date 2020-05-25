from telethon import TelegramClient, events, sync 
import asyncio
import telegram_connect as tc
import src.database_operations as database_operations

#@tc.client.on(events.NewMessage)
# @tc.client.on(events.NewMessage)
# async def main(event):
#     print(event.message.stringify())
#     obj = await tc.client.send_message(1139109151,event.message)    # to tele12 as backup
#     if database_operations.insert_message(obj,tc.session_name):
#         print('message arrived and inserted')
#     else:
#         print("error in inserting")

# #calling method/can use asyncio too

# tc.client.start()
# tc.client.run_until_disconnected()

##############
api_hash= '81c1daf35a14dcfe8b20dc8fca1b679a'
api_id= '1237102'
username= 'tele13'

client = TelegramClient(username, api_id, api_hash)
client.connect()

@client.on(events.NewMessage)
async def main(event):
    print(event.message.id,"recieved")                               #in tele13
    obj = await client.send_message(1139109151,event.message)
    obj.from_id = (await client.get_me()).id
    print(obj)
    # to tele12
    try:
        if database_operations.insert_message(obj,"tele12"):
            print('message arrived and inserted')
        else:
            print("error in inserting")
    except Exception as e:
        print(e)


#calling method/can use asyncio too
'''
client.start()
client.run_until_disconnected()
'''