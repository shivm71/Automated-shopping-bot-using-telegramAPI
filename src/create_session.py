from telethon import TelegramClient,sync
import yaml

num = 12  #update this number and you can get any session from the created session

credentials = yaml.load(open('../config/application.yml'), Loader=yaml.FullLoader)
api_id = credentials['tele'+str(num)]['api_id']
api_hash = credentials['tele'+str(num)]['api_hash']
phone = credentials['tele'+str(num)]['phone']
username = credentials['tele'+str(num)]['username']

client = TelegramClient(username, api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except Exception:
        client.sign_in(password=input('Password: '))

me = client.get_me()
print(me)
