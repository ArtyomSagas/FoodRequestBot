from aiogram import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tokens import *
from keyboards import *

bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())


# /start
@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.answer('Hello here you can order food.\nTo get started, you must register.',
                         reply_markup=keyboard_registration())


# /help
@dp.message_handler(commands='help')
async def command_help(message: types.Message):
    await message.answer('If you have any problems, you can contact +7-***-***-**-**.')


# Register
@dp.callback_query_handler(text='button_register')
async def button_register(callback: types.CallbackQuery):
    await callback.answer('Enter your full name')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
