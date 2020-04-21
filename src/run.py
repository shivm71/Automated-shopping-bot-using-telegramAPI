import mongo_connect as mc
import telegram_connect as tc
from telegram_main import telegram
col = mc.db["groups"]
limit = 20
main = telegram(tc.client,col) # Telegram(client,column)
for k in col.find():
   tc.client.loop.run_until_complete(main.insert_user_from_group(k["group_id"],limit)) # insert_user_from_group(self,group_id,limit)



