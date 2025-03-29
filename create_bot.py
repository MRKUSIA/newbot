import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import load_dotenv # модуль для импорта переменных
from app.db_handler.db_class import create_connector

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMINS = os.getenv('ADMINS')

admins = [int(admin_id) for admin_id in ADMINS.split(',')]
bot = Bot(token=BOT_TOKEN, 
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
    

def create_tables():
    conn = create_connector()
    cursor = conn.cursor()

    cursor.execute('''
CREATE TABLE IF NOT EXISTS users
(
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    full_name TEXT,
    req_date TEXT
)
    ''')

    conn.commit()
    conn.close()
        
create_tables()
