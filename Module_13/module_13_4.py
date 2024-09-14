from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pprint import pprint
import aiogram
import aiogram.types
import asyncio
import logging


TOKEN = 'place your token here'
BOT = Bot(token=TOKEN)
DISPATCHER = Dispatcher(bot=BOT, storage=MemoryStorage())
MAN_NAMINGS = ['мужчина', 'м', 'муж', 'мужской', 'мальчик', 'парень', 'man', 'm']
WOMAN_NAMINGS = ['женщина','ж', 'жен', 'женский', 'девочка', 'девушка', 'woman', 'w']


def get_data_from_state(data):
    result = {}
    for i in data:
        result[i] = data[i]
    return result

class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()

    def is_correct_sex(sex: str):
        if sex in MAN_NAMINGS + WOMAN_NAMINGS:
            return None
        raise ValueError

    def is_correct_age(age: str):
        result = float(age)
        if result <= 0:
            raise ValueError
        return result

    def is_correct_growth(growth: str):
        result = float(growth)
        if result <= 0:
            raise ValueError
        return result

    def is_correct_weight(weight: str):
        result = float(weight)
        if result <= 0:
            raise ValueError
        return result


@DISPATCHER.message_handler(commands=['start'], state=UserState)
async def start_message(message: aiogram.types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Напиши команду /calories, чтобы я вычислил '
                         'необходимую для тебя норму калорий.')

@DISPATCHER.message_handler(commands=['calories'])
async def set_sex(message: aiogram.types.Message):
    await message.answer('Введите ваш пол:')
    await UserState.sex.set()

@DISPATCHER.message_handler(state=UserState.sex)
async def set_age(message: aiogram.types.Message, state: FSMContext):
    try:
        UserState.is_correct_sex(message.text)
    except ValueError:
        await message.answer(f'Пол введён некорректно, попробуйте ещё раз. Вот список доступных комманд:')
        for naming in MAN_NAMINGS + WOMAN_NAMINGS:
            await message.answer(naming)
        await set_sex(message)
    else:
        await state.update_data(sex=message.text.lower())
        await message.answer('Введите ваш возраст:')
        await UserState.age.set()

@DISPATCHER.message_handler(state=UserState.age)
async def set_growth(message: aiogram.types.Message, state: FSMContext):
    try:
        UserState.is_correct_age(message.text)
    except ValueError:
        await message.answer(f'Возраст введён некорректно. Пожалуйста, введите число не меньшее 1.')
        await set_age(message)
    else:
        await state.update_data(age=float(message.text))
        await message.answer('Введите ваш рост:')
        await UserState.growth.set()

@DISPATCHER.message_handler(state=UserState.growth)
async def set_weight(message: aiogram.types.Message, state:FSMContext):
    try:
        UserState.is_correct_age(message.text)
    except ValueError:
        await message.answer(f'Рост введён некорректно. Пожалуйста, введите число не меньшее 1.')
        await set_growth(message)
    else:
        await state.update_data(growth=float(message.text))
        await message.answer('Введите ваш вес:')
        await UserState.weight.set()

@DISPATCHER.message_handler(state=UserState.weight)
async def send_calories(message: aiogram.types.Message, state: FSMContext):
    try:
        UserState.is_correct_weight(message.text)
    except ValueError:
        await message.answer(f'Вес введён некорректно. Пожалуйста, введите число не меньшее 1.')
        await set_growth(message)
    else:
        await state.update_data(weight=float(message.text))
        data = await state.get_data()
        if data['sex'] in MAN_NAMINGS:
            calories = 10*data['weight'] + 6.25*data['growth'] - 5*data['age'] + 5
        else:
            calories = 10*data['weight'] + 6.25*data['growth'] - 5*data['age'] - 161
        await message.answer(f'Ваша норма калорий: {calories} ккал')
        await state.reset_state()

@DISPATCHER.message_handler()
async def all_messages(message: aiogram.types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(DISPATCHER, skip_updates=True)
