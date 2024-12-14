from telethon import TelegramClient, events
from utils import env
from services.services import getNotice
from asgiref.sync import sync_to_async
from main.models import Notice


client = TelegramClient(env.PHONE_NUMBER, env.API_ID, env.API_HASH)
last_notice_data = {}


    
chat_ids = [
    -1001661240991, -1002220553035, -1002406606261, -1002114024623, 
    -1002483533745, -1002169615850, -1001934813270, -1002237859063, 
    -1002225373901, -1001931951297, -1001276254263, -1001768202236,
    -1001869944953, -1002178966866, -1002202717276, -1002232778089,
    -1001932433103, -1002083400408, -1001950144985, 
]





message_counters = {chat_id: 0 for chat_id in chat_ids}
last_sents = {chat_id: False for chat_id in chat_ids}

async def is_chat_accessible(chat_id):
    try:
        await client.get_entity(chat_id)
        return True
    except Exception as e:
        print(f"Chat {chat_id} is not accessible: {e}")
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"Chat {chat_id} is not accessible. Error: {e}\n")
        return False



async def send_notice(notice, chat_id):
    try:
        formatted_description = f"**{notice.descriptions}**"
        await client.send_message(chat_id, formatted_description, parse_mode='Markdown')
        last_sents[chat_id] = True
    except Exception as e:
        print(f"Error sending message to {chat_id}: {e}")
        last_sents[chat_id] = False
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"Chat ID: {chat_id} - Error sending message: {e}\n")



@client.on(events.NewMessage())
async def handler(event):
    global message_counters, last_sents
    if event.chat_id in chat_ids:
        if not event.out:
            notices = await sync_to_async(getNotice)()
            if notices:
                message_counters[event.chat_id] += 1
                print(f"New message received in chat {event.chat_id}. Current count: {message_counters[event.chat_id]}")

                notice_list = await sync_to_async(list)(Notice.objects.all())
                if notice_list:
                    notice = notice_list[0]
                    if message_counters[event.chat_id] >= notice.interval and not last_sents[event.chat_id]:
                        if await is_chat_accessible(event.chat_id):
                            await send_notice(notice, event.chat_id)
                            message_counters[event.chat_id] = 0
                        else:
                            print(f"Cannot send message to chat {event.chat_id}, not accessible.")
                    elif message_counters[event.chat_id] < notice.interval:
                        last_sents[event.chat_id] = False

