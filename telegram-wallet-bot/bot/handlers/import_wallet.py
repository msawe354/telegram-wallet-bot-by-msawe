# bot/handlers/import_wallet.py
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from services.wallet_service import WalletService

router = Router()


class ImportStates(StatesGroup):
    waiting_for_key = State()
    waiting_for_password = State()


@router.message(Command("import"))
async def cmd_import(message: types.Message, state: FSMContext):
    await message.answer(
        "🔑 Enter your private key (hex format, with or without 0x prefix):"
    )
    await state.set_state(ImportStates.waiting_for_key)


@router.message(ImportStates.waiting_for_key)
async def process_key(message: types.Message, state: FSMContext):
    private_key = message.text.strip()
    if private_key.startswith("0x"):
        private_key = private_key[2:]

    if len(private_key) != 64:
        await message.answer("❌ Invalid private key length. Must be 64 hex characters. Try again:")
        return

    await state.update_data(private_key=private_key)
    await message.answer("🔐 Now enter a password to encrypt your wallet:")
    await state.set_state(ImportStates.waiting_for_password)


@router.message(ImportStates.waiting_for_password)
async def process_import_password(message: types.Message, state: FSMContext):
    password = message.text
    if len(password) < 6:
        await message.answer("❌ Password must be at least 6 characters. Try again:")
        return

    data = await state.get_data()
    private_key = data["private_key"]

    try:
        service = WalletService()
        result = await service.import_wallet(message.from_user.id, private_key, password)

        await state.clear()

        await message.answer(
            f"✅ Wallet imported!\n\n"
            f"Address: <code>{result['address']}</code>\n\n"
            f"⚠️ Delete this message with your private key for security."
        )
    except Exception as e:
        await state.clear()
        await message.answer(f"❌ Import failed: {str(e)}")