# aiogram import
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# kode import
from utils.env import ADMIN, BOT_TOKEN
import logging

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()


bot = Bot(token=BOT_TOKEN, parse_mode='markdown')

dp = Dispatcher(bot, storage=storage)



