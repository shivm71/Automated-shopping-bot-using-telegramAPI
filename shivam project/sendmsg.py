from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import asyncio 
api_id = '1201180'
api_hash = '1b3d4bdf22f0b52af3f1df6db89b62b7'
phone = '+917828871116'
username = 'Shivam Shah'
client = TelegramClient(username, api_id, api_hash)
client.connect()
user = [1057346232,689402190,-477045489,185209613,-481982874,902231413]
async def main():
    for i in [902231413,-477045489]:
        # await client.send_file(i,"download.jpg")
        await client.send_message(i,
         'Some <b>bold</b> and <i>italic</i> text \n'
         'An <a href="https://example.com">URL</a>'
         '<code>code</code> and <pre>pre\nblocks</pre>'
         '<a href="tg://user?id=me">message with html format</a>', parse_mode='html')
        # q = await client.send_message(i,"message with image test2",file="download.jpg")
        # print(q.stringify())
        # await client.send_message(i,"hello user with telegram logo",caption="content with image")
        
with client:
    client.loop.run_until_complete(main())   