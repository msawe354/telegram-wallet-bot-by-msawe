# bot/routers.py
from aiogram import Dispatcher

from bot.handlers import start, wallet, balance, send, import_wallet, settings as settings_handler


def register_all_routers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(wallet.router)
    dp.include_router(balance.router)
    dp.include_router(send.router)
    dp.include_router(import_wallet.router)
    dp.include_router(settings_handler.router)