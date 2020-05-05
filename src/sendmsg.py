from telethon import TelegramClient, events, sync
import asyncio 
import telegram_connect as tc
client = tc.client
user = [1057346232,689402190,-477045489,185209613,-481982874,902231413]
async def main(id,message):
        # await client.send_file(i,"../resource/download.jpg")
        await client.send_message(id,
         'Some <b>bold</b> and <i>italic</i> text \n'
         'An <a href="https://example.com">URL</a>'
         '<code>code</code> and <pre>pre\nblocks</pre>'
         '<a href="tg://user?id=me">message with html format</a>', parse_mode='html')
        # q = await client.send_message(i,"message with image test2",file="download.jpg")
        # print(q.stringify())
        # await client.send_message(i,"hello user with telegram logo",caption="content with image")
        
        
# call using some asycn loop from anywhere with id and message content with below method 
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(args))
        