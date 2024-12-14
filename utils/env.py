from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
ADMIN= env('ADMIN')
BASE_URL = env('BASE_URL')

PHONE_NUMBER = env('PHONE_NUMBER')
API_ID = env('API_ID')
API_HASH = env('API_HASH')
GROUP_ID = -1002264446732