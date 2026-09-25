# bot/handlers/start.py
from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Welcome to Crypto Wallet Bot\n\n"
        "Commands:\n"
        "/wallet - Create new wallet\n"
        "/import - Import existing wallet\n"
        "/balance - Show balance\n"
        "/send - Send crypto\n"
        "/settings - Wallet settings\n"
        "/help - Show help"
    )


@router.message(CommandStart())
async def cmd_help(message: types.Message):
    await message.answer(
        "Available commands:\n\n"
        "/wallet - Create a new crypto wallet\n"
        "/import - Import wallet from seed phrase\n"
        "/balance - Check your balance\n"
        "/send - Send crypto to another address\n"
        "/settings - Configure wallet settings"
    )