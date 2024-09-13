import aiogram.types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pprint import pprint
import json
import asyncio

TOKEN = 'place your token here'
BOT = Bot(token=TOKEN)
DISPATCHER = Dispatcher(bot=BOT, storage=MemoryStorage())


@DISPATCHER.message_handler(commands=['start'])
async def start_message(message: aiogram.types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')

@DISPATCHER.message_handler()
async def all_messages(message: aiogram.types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(DISPATCHER, skip_updates=True)
