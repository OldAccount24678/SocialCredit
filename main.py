from aiogram import executor
from loader import dp
from utils.app import reg_handlers

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=reg_handlers)
