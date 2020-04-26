import mongo_connect as mc
import telegram_connect as tc
from telegram_main import telegram
import sys
def main(limit,group_id):
   users_collection = mc.db["users"]
   main = telegram(tc.client,users_collection) # Telegram(client,column)
   tc.client.loop.run_until_complete(main.insert_user_from_group(group_id,limit)) # insert_user_from_group(self,group_id,limit)

if __name__ == "__main__":
   main(int(sys.argv[1]), sys.argv[2])  #put limit & group_id/group_name e.g https://web.telegram.org/#/im?p=@covid19indiaops



