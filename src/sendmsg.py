import asyncio
from telethon.tl.types import InputPeerUser
import database_operations
import mongo_connect as mc
import telegram_connect as tc

loop = asyncio.get_event_loop()
offset = 100

async def send_msg_with_username():
    global offset
    client_dict,client_list = await tc.get_all_client()
    collection = mc.db["user_with_uname"]   ## change according to db collection name
    curr_index = 0

    while collection.find({"invite_status": False}).count() > 0:
        offset = min(collection.find({"invite_status": False}).count(),offset)
        for user in collection.find({"invite_status": False}).limit(offset):  ##todo: need to implement limit offset logic, & get object in sorted order of the created time
            key = client_list[curr_index]
            temp_client = client_dict[key]
            username = user["telegram_username"]
            contact_no = user["userinfo"]["mobile_no"]
            if username:
                entity = await temp_client.get_input_entity(username)
            elif contact_no:

                entity = await temp_client.get_input_entity('+91'+str(contact_no)[-10:])
            else:
                print("Wrong USER with no username and mobile number with col_id :",user["_id"])
            try:
                await temp_client.send_message(entity,"MESSAGE")    # enter message or pass as argument
                database_operations.update_invite_status(collection,user["_id"])

            except:
                print("message not sent to user with col_id {} from client : {}".format(user["_id"],key))
            curr_index+=1
            curr_index%=len(client_list)



async def send_msg_without_username():
    global offset
    client_dict,client_list = await tc.get_all_client()
    collection = mc.db["user_without_uname"]   ## change according to db collection name
    curr_index = 0
    while collection.find({"invite_status": False}).count() > 0:
        offset = min(collection.find({"invite_status": False}).count(),offset)
        for user in collection.find({"invite_status": False}):   ##todo: need to implement limit offset logic, & get object in sorted order of the created time
            start_index,local_index = curr_index,curr_index
            client_dict = user["client_info"]
            user_id = user["telegram_id"]
            sent = False
            while client_dict:
                key = client_list[local_index]
                temp_client = client_dict[key]
                if key in client_dict:
                    access_hash = client_dict[key]
                    entity = InputPeerUser(user_id=user_id,access_hash=access_hash)
                    try:
                        await temp_client.send_message(entity,"MESSAGE")    # enter message or pass as argument
                        database_operations.update_invite_status(collection,user["_id"])
                        sent = True
                        break

                    except:
                        local_index+=1
                        local_index%=len(client_list)
                        del client_dict[key]
                else:
                    local_index+=1
                    local_index%=len(client_list)
                if local_index == start_index:
                    break
            if not sent:
                print("message not sent to user with col_id {}(nousername) with no client present".format(user["_id"]))


            curr_index+=1
            curr_index%=len(client_list)


loop.run_until_complete(send_msg_with_username())



# client = tc.client
# user = [1057346232,689402190,-477045489,185209613,-481982874,902231413]
# async def main(id,message):
#         # await client.send_file(i,"../resource/download.jpg")
#         await client.send_message(-477045489,
#          'Some <b>bold</b> and <i>italic</i> text \n'
#          'An <a href="https://example.com">URL</a>'
#          '<code>code</code> and <pre>pre\nblocks</pre>'
#          '<a href="tg://user?id=me">message with html format</a>', parse_mode='html')
#         # q = await client.send_message(i,"message with image test2",file="download.jpg")
#         # print(q.stringify())
#         # await client.send_message(i,"hello user with telegram logo",caption="content with image")


# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(main(args))

