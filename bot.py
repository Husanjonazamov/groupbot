from aiogram.types import Message
from aiogram import executor

# kode import
from loader import dp, bot
from utils.env import ADMIN
from handlers.notice.funk import client
from handlers.notice.handler import dynamic_notice_send_task
import handlers
import asyncio



async def on_startup(dispatcher):
    """
    botni ishga tushradigan funk
    """
    asyncio.create_task(run_client_with_task())
    await bot.send_message(ADMIN, 'bot ishga tushdi')
    
async def run_client_with_task():
    async with client:
        await client.start()

        await asyncio.gather(
            dynamic_notice_send_task(),
            client.run_until_disconnected()
        )
        

executor.start_polling(dp, on_startup=on_startup)



