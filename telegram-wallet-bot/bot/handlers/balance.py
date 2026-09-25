# bot/handlers/balance.py
from aiogram import Router, types
from aiogram.filters import Command

from services.wallet_service import WalletService

router = Router()


@router.message(Command("balance"))
async def cmd_balance(message: types.Message):
    service = WalletService()
    result = await service.get_balance(message.from_user.id)

    if "error" in result:
        await message.answer("❌ No wallet found. Use /wallet to create one.")
        return

    await message.answer(
        f"💰 Wallet Address:\n"
        f"<code>{result['address']}</code>\n\n"
        f"Use this address to receive crypto."
    )