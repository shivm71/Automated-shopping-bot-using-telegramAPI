from telethon import TelegramClient, events, sync 
import asyncio
import telegram_connect as tc 

@tc.client.on(events.NewMessage)
async def main(event):
    print(event.stringify()) #use event object to get data from various group 
    await event.reply('hi!') 

#calling method/can use asyncio too
'''
client.start()
client.run_until_disconnected()
'''