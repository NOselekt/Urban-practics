from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message, InlineKeyboardButton, InlineKeyboardMarkup,\
    CallbackQuery
import aiogram
import asyncio
import logging

TOKEN = 'place your token here'
BOT = Bot(token=TOKEN)
DISPATCHER = Dispatcher(bot=BOT, storage=MemoryStorage())
MAN_NAMINGS = ['мужчина', 'м', 'муж', 'мужской', 'мальчик', 'парень', 'man', 'm', 'male']
WOMAN_NAMINGS = ['женщина','ж', 'жен', 'женский', 'девочка', 'девушка', 'woman', 'w', 'female']


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()

    def is_correct_sex(sex: str):
        if sex.lower() in MAN_NAMINGS + WOMAN_NAMINGS:
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


keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рассчитать")],
        [KeyboardButton(text="Информация")]
    ], resize_keyboard=True
)
inline_keyboard_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')],
        [InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')]
    ])
inline_keyboard_sex = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Мужской", callback_data='male')],
        [InlineKeyboardButton(text="Женский", callback_data='female')]
    ]
)


@DISPATCHER.message_handler(commands=['start'], state=UserState)
async def start_message(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Напиши "Рассчитать", чтобы я вычислил '
                         'необходимую для тебя норму калорий.', reply_markup=keyboard_start)

@DISPATCHER.message_handler(commands=['start'])
async def start_message(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Напиши "Рассчитать", чтобы я вычислил '
                         'необходимую для тебя норму калорий.', reply_markup=keyboard_start)

@DISPATCHER.message_handler(text=['Информация'])
async def start_message(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Напиши "Рассчитать", чтобы я вычислил '
                         'необходимую для тебя норму калорий.', reply_markup=keyboard_start)

@DISPATCHER.message_handler(text=["Рассчитать"])
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard_menu)

@DISPATCHER.callback_query_handler(text=['formulas'])
async def get_formulas(call: CallbackQuery):
    await call.message.answer("Упрощённая формула Миффлина-Сан Жеора:\n"
                              "10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()

@DISPATCHER.callback_query_handler(text=['calories'])
async def set_sex(call: CallbackQuery):
    await call.message.answer('Введите ваш пол:', reply_markup=inline_keyboard_sex)
    await call.answer()
    await UserState.sex.set()

@DISPATCHER.callback_query_handler(text=['male', 'female'], state=UserState.sex)
async def set_age(call: CallbackQuery, state: FSMContext):
    await call.answer()
    try:
        UserState.is_correct_sex(call.data)
    except ValueError:
        await call.message.answer(f'Пол введён некорректно, попробуйте ещё раз. Вот список доступных комманд:')
        for naming in MAN_NAMINGS + WOMAN_NAMINGS:
            await call.message.answer(naming)
        await set_sex(call)
    else:
        await state.update_data(sex=call.data.lower())
        await call.message.answer('Введите ваш возраст:')
        await UserState.age.set()

@DISPATCHER.message_handler(state=UserState.age)
async def set_growth(message: Message, state: FSMContext):
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
async def set_weight(message: Message, state:FSMContext):
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
async def send_calories(message: Message, state: FSMContext):
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
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(DISPATCHER, skip_updates=True)
