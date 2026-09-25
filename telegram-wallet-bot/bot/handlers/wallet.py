# bot/handlers/wallet.py
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from services.wallet_service import WalletService

router = Router()


class WalletStates(StatesGroup):
    waiting_for_password = State()


@router.message(Command("wallet"))
async def cmd_wallet(message: types.Message, state: FSMContext):
    await message.answer(
        "🔐 Enter a password to encrypt your wallet.\n"
        "⚠️ This password will be used to decrypt your private key.\n"
        "Do not forget it."
    )
    await state.set_state(WalletStates.waiting_for_password)


@router.message(WalletStates.waiting_for_password)
async def process_password(message: types.Message, state: FSMContext):
    password = message.text
    if len(password) < 6:
        await message.answer("❌ Password must be at least 6 characters. Try again:")
        return

    service = WalletService()
    result = await service.create_wallet(message.from_user.id, password)

    await state.clear()

    await message.answer(
        f"✅ Wallet created!\n\n"
        f"Address: <code>{result['address']}</code>\n\n"
        f"⚠️ Save this address. Use /settings to export your private key."
    )