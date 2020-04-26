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
    cred = yaml.load(open(filepath), Loader=yaml.FullLoader)
    cred[session_name]["insert_time"] = int(time.time())
    cred[session_name]["timeout"] = wait_time
    with open(filepath, "w") as f:
        yaml.dump(cred, f)
    flag = True
    while(flag):
        time.sleep(10)
        cred = yaml.load(open(filepath), Loader=yaml.FullLoader)
        for key in cred:
            if int(time.time()) - cred[key]["insert_time"] > cred[key]["timeout"]:
                api_id =  cred[key]["api_id"]
                api_hash = cred[key]["api_hash"]
                session_name = key
                flag = False
                break
            
    client = TelegramClient(session_name, api_id, api_hash)

    # with client:
    #     pass  
    await client.connect()
    return (client,session_name)

