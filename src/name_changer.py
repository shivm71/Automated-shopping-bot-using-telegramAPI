from telethon.sync import TelegramClient
from telethon import functions, types
import asyncio

def name_change(client,fname,lname=None,about=None):
    with client:
        try:
            result = client(functions.account.UpdateProfileRequest(
                first_name=fname,
                last_name=lname,
                about=about
            ))
        except: return False
    print("credectials after changing are  {} {} with about {}",format(result.first_name,result.last_name,about))
    return True


#name_change(client,"Shivam",'Shah',) # calling method