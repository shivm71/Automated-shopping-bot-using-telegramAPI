import mongo_connect as mc
import telegram_connect as tc
import insert_user as iu
col = mc.db["groups"]
limit = 10
for k in col.find():
   tc.client.loop.run_until_complete(iu.main(k["group_id"],limit))
