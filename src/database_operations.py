from datetime import datetime
import mongo_connect  # fetch db

uname = mongo_connect.db["user_with_uname"]
nouname = mongo_connect.db["user_without_uname"]
msg_col = mongo_connect.db["fetched_messages"]


def insert_user(client_name,user,group_tag,loc_tags):
    collection_name = uname
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if not hasattr(user,'email'):
        user.email = None
    query = {
        "telegram_id":user.id,
        "telegram_username":user.username,
        "userinfo":{
            "firstname":user.first_name,
            "lastname":user.last_name,
            "email":user.email,
            "gender":None,
            "age":None,
            "mobile_no":user.phone,
            "pref_cat":[]
        },
        "group_tags" : group_tag,
        "loc_tags" : loc_tags,
        "created":date,
        "updated":None,
        "invite_status":False,
        "membership_status":False,
    }
    if not (user.username or user.phone):
        query["client_info"] = {client_name : user.access_hash}
        collection_name = nouname
    try:
        collection_name.insert_one(query)
        return True
    except Exception as e:
        update_tags(collection_name,user,group_tag,loc_tags)
        print("duplicate entry level 1",e)
        if collection_name == nouname:
            return update_user_and_client_hash(client_name,user)
        return True                                                                          # level 1


def update_tags(collection_name,user,group_tag,loc_tags):
    myquery = {"telegram_id":user.id}
    res = collection_name.find_one(myquery)
    loc = res["loc_tags"]
    group = res["group_tags"]
    loc+=loc_tags
    group+=group_tag
    loc = list(set(loc))
    group = list(set(group))
    newvalues = { "$set": { "group_tags":group,"loc_tags":loc} }
    if collection_name.update_one(myquery, newvalues):                                       #level 2
        return True
    else:
        print("not inserted at level 2")
        return False

    pass


def update_user_and_client_hash(client_name,user):
    myquery = {"telegram_id":user.id}
    pre = nouname.find_one(myquery)["client_info"]
    pre[client_name] = user.access_hash
    newvalues = { "$set": { "client_info":pre} }
    if nouname.update_one(myquery, newvalues):                                           #level 3
        return True
    else:
        print("not inserted at level 3")
        return False

def insert_group():
    pass


def update_invite_status(col,id):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    myquery = {'_id':id}
    newvalues = { "$set": { "invite_status": True,'updated':date } }
    col.update_one(myquery, newvalues)


def insert_message(obj,client_name):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    query = {
        'messsgae_id' :obj.id,
        'message_content' : obj.message,
        'client_used': client_name,
        'self_id':obj.from_id,
        'self_name':None,
        'to_id':obj.to_id.user_id,
        'to_name':None,
        'time': date,
        'reviewed': False,
        'tags':[]
    }
    try:
        msg_col.insert_one(query)
        return True
    except Exception as e:
        print("insert msg error",e )
        return False
