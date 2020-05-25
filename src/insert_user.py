import asyncio
import threading
from src import database_operations
import telegram_connect


def intercall(client_name,client,group_id,group_tags,loc_tags):
    loop.run_until_complete(insert(client_name,client,group_id,group_tags,loc_tags))


async def insert(client_name,client,group_id,group_tags,loc_tags):
    count = 0
    entity = await client.get_entity(group_id)
    #print(entity)
    print(client_name)
    try:
        async for user in client.iter_participants(entity,limit=500):   #aggressive = True
            if database_operations.insert_user(client_name,user,group_tags,loc_tags):
                count+=1
            else:
                print("Failed to insert after level 2")
        print("inserted users for client=",client_name, " count=",count)
    except Exception as e:
        print("not working------",e)


loop = asyncio.get_event_loop()
client_dict,client_list = loop.run_until_complete(telegram_connect.get_all_client())

loc_tags = []
group_tags = []
for client_name in client_list:
    x = threading.Thread(target= intercall, args=(client_name,client_dict[client_name],'campusdriveupdates',group_tags,loc_tags))
    x.start()
    x.join()
