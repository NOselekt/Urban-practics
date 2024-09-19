from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message, InlineKeyboardButton, InlineKeyboardMarkup,\
    CallbackQuery
import aiogram
import asyncio
import logging
import crud_functions
import os.path


TOKEN = '7316117657:AAEcOvVzsyarwbnDhdh42uIXSpXw8M1Rofw'
BOT = Bot(token=TOKEN)
DISPATCHER = Dispatcher(bot=BOT, storage=MemoryStorage())
crud_functions.initiate_db()
PRODUCTS_DATA = crud_functions.get_all_products()


class UserState(StatesGroup):
    sex = State()
    growth = State()
    weight = State()
    age = State()


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

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


    def is_correct_username(username: str):
        for char in username:
            if char.lower() not in "qwertyuiopasdfghjklzxcvbnm":
                raise ValueError
        return None

    def is_correct_email(email: str):
        if email[0] == "@":
            raise ValueError
        for char in email:
            if char == "@":
                break
            if char.lower() not in "qwertyuiopasdfghjklzxcvbnm":
                raise ValueError
        else:
            raise ValueError
        return None

    def is_correct_age(age: str):
        result = float(age)
        if result <= 0:
            raise ValueError
        return result


keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рассчитать"), KeyboardButton(text="Информация")],
        [KeyboardButton(text="Купить"), KeyboardButton(text="Регистрация")]
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
inline_keyboard_buying_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Продукт1", callback_data="product_buying"), InlineKeyboardButton(text="Продукт2", callback_data="product_buying")],
        [InlineKeyboardButton(text="Продукт3", callback_data="product_buying"), InlineKeyboardButton(text="Продукт4", callback_data="product_buying")],
        [InlineKeyboardButton(text="Продукт5", callback_data="product_buying"), InlineKeyboardButton(text="Продукт6", callback_data="product_buying")],
        [InlineKeyboardButton(text="Продукт7", callback_data="product_buying"), InlineKeyboardButton(text="Продукт8", callback_data="product_buying")],
        [InlineKeyboardButton(text="Продукт9", callback_data="product_buying"), InlineKeyboardButton(text="Продукт10", callback_data="product_buying")]
    ]
)


#resetting messages
@DISPATCHER.message_handler(commands=['start'])
async def start_message(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Напиши "Рассчитать", чтобы я вычислил '
                         'необходимую для тебя норму калорий.', reply_markup=keyboard_start)

@DISPATCHER.message_handler(commands=['start'], state=UserState)
async def start_message(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Напиши "Рассчитать", чтобы я вычислил '
                         'необходимую для тебя норму калорий.', reply_markup=keyboard_start)

@DISPATCHER.message_handler(commands=['start'], state=RegistrationState)
async def start_message(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Напиши "Рассчитать", чтобы я вычислил '
                         'необходимую для тебя норму калорий.', reply_markup=keyboard_start)

@DISPATCHER.message_handler(text=["Информация"])
async def start_message(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Напиши "Рассчитать", чтобы я вычислил '
                         'необходимую для тебя норму калорий.', reply_markup=keyboard_start)

@DISPATCHER.message_handler(text=["Информация"], state=UserState)
async def start_message(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Напиши "Рассчитать", чтобы я вычислил '
                         'необходимую для тебя норму калорий.', reply_markup=keyboard_start)

@DISPATCHER.message_handler(text=["Информация"], state=RegistrationState)
async def start_message(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Напиши "Рассчитать", чтобы я вычислил '
                         'необходимую для тебя норму калорий.', reply_markup=keyboard_start)


#handlers for keyboard_start
@DISPATCHER.message_handler(text=["Рассчитать"])
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard_menu)

@DISPATCHER.message_handler(text=["Купить"])
async def get_buying_list(message: Message):
    for i in range(1, 11):
        product = PRODUCTS_DATA[i - 1]
        with open(product[-1], "rb") as image:
            await message.answer_photo(photo=image, caption=f"{product[1]} | {product[2]} | Цена: {product[3]}₽")
    await message.answer("Выберите товар:", reply_markup=inline_keyboard_buying_list)

@DISPATCHER.message_handler(text="Регистрация")
async def sign_up(message: Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


#formulas button handler
@DISPATCHER.callback_query_handler(text=['formulas'])
async def get_formulas(call: CallbackQuery):
    await call.message.answer("Упрощённая формула Миффлина-Сан Жеора:\n"
                              "10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


#buying buttons handler
@DISPATCHER.callback_query_handler(text=["product_buying"])
async def send_confirm_massage(call: CallbackQuery):
    await call.message.answer(f"Вы успешно приобрели продукт!")
    await call.answer()


#registration state chain
@DISPATCHER.message_handler(state=RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    try:
        RegistrationState.is_correct_username(message.text)
    except ValueError:
        await message.answer("Имя пользователя введено некорректно, попробуйте ещё раз.")
    else:
        if crud_functions.is_included(message.text):
            await message.answer("Данное имя занято, введите другое")
        else:
            await state.update_data(username=message.text)
            await message.answer("Введите ваш email:")
            await RegistrationState.email.set()

@DISPATCHER.message_handler(state=RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    try:
        RegistrationState.is_correct_email(message.text)
    except ValueError:
        await message.answer("email введён некорректно, попробуйте ещё раз.")
    else:
        await state.update_data(email=message.text)
        await message.answer("Введите ваш возраст:")
        await RegistrationState.age.set()

@DISPATCHER.message_handler(state=RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    try:
        RegistrationState.is_correct_age(message.text)
    except ValueError:
        await message.answer("Возраст введён некорректно, попробуйте ещё раз.")
    else:
        await state.update_data(age=message.text)
        user = await state.get_data()
        crud_functions.add_user(user["username"], user["email"], user["age"])
        print(user["username"], user["email"], user["age"])
        await state.reset_state()


#calories count state chain
@DISPATCHER.callback_query_handler(text=['calories'])
async def set_sex(call: CallbackQuery):
    await call.message.answer('Введите ваш пол:', reply_markup=inline_keyboard_sex)
    await call.answer()
    await UserState.sex.set()

@DISPATCHER.callback_query_handler(text=['male', 'female'], state=UserState.sex)
async def set_age(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(sex=call.data.lower())
    await call.message.answer('Введите ваш возраст:')
    await UserState.age.set()

@DISPATCHER.message_handler(state=UserState.age)
async def set_growth(message: Message, state: FSMContext):
    try:
        UserState.is_correct_age(message.text)
    except ValueError:
        await message.answer(f'Возраст введён некорректно. Пожалуйста, введите число не меньшее 1.')
    else:
        await state.update_data(age=float(message.text))
        await message.answer('Введите ваш рост:')
        await UserState.growth.set()

@DISPATCHER.message_handler(state=UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    try:
        UserState.is_correct_age(message.text)
    except ValueError:
        await message.answer(f'Рост введён некорректно. Пожалуйста, введите число не меньшее 1.')
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
    else:
        await state.update_data(weight=float(message.text))
        data = await state.get_data()
        if data['sex'] == "male":
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