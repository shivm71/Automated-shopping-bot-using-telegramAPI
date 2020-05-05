from telethon import TelegramClient,sync
import yaml
import time

api_id = '1339832'
api_hash = '2e8f2ed964cc27010fb5f9fe38ef9077'
phone = '+18727042784'
session_name = 'tele_groups'
filepath = '../config/application.yml'
client = TelegramClient(session_name, api_id, api_hash)

with client:
  pass  
client.connect()

async def get_next_client(client,session_name,wait_time):
    if client is not None:
        cred = yaml.load(open(filepath), Loader=yaml.FullLoader)
        cred[session_name]["insert_time"] = int(time.time())
        cred[session_name]["timeout"] = wait_time
        with open(filepath, "w") as f:
            yaml.dump(cred, f)
    flag = True
    to_wait = False
    wait_time = 100000
    while(flag):
        cred = yaml.load(open(filepath), Loader=yaml.FullLoader)
        for key in cred:
            wait_time = min(wait_time,int(time.time()) - cred[key]["insert_time"])
            if int(time.time()) - cred[key]["insert_time"] > cred[key]["timeout"]:
                api_id =  cred[key]["api_id"]
                api_hash = cred[key]["api_hash"]
                session_name = key
                flag = False
                to_wait = False
                break
            else:
                to_wait = True
        if to_wait:
            print("All clients are in Flood wait error")
            print("Reinitializing in {}sec ",format(wait_time))
            time.sleep(wait_time)  
        cred = []    
    client = TelegramClient(session_name, api_id, api_hash)

    # with client:
    #     pass  
    await client.connect()
    return (client,session_name)

