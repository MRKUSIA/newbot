from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.keywords.all_kb import main_kb, create_spec_kb
from app.utils.utils import ABOUT_ME, create_profile_message
from app.db_handler.db_class import create_user, get_user


start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user
    create_user(user.id, user.username)
    await message.answer('Запуск сообщения по' + \
        ' команде /start используя фильтр ' + \
            'CommandStart() upd test',
            reply_markup=main_kb(message.from_user.id))


@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по' + \
        ' команде /start_2 используя фильтр Command()',
        reply_markup=create_spec_kb())


@start_router.message(F.text == "О нас")
async def print_about_me_message(message: Message):
    await message.answer(ABOUT_ME)


@start_router.message(F.text == "Профиль")
async def print_user_info(message: Message):
    user = get_user(message.from_user.id)
    await message.answer(create_profile_message(user))
