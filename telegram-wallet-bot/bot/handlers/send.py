# bot/handlers/send.py
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class SendStates(StatesGroup):
    waiting_for_address = State()
    waiting_for_amount = State()
    waiting_for_password = State()


@router.message(Command("send"))
async def cmd_send(message: types.Message, state: FSMContext):
    await message.answer("📤 Enter recipient address (0x...):")
    await state.set_state(SendStates.waiting_for_address)


@router.message(SendStates.waiting_for_address)
async def process_address(message: types.Message, state: FSMContext):
    address = message.text.strip()
    if not address.startswith("0x") or len(address) != 42:
        await message.answer("❌ Invalid address. Must start with 0x and be 42 characters. Try again:")
        return

    await state.update_data(to_address=address)
    await message.answer("💵 Enter amount to send (ETH):")
    await state.set_state(SendStates.waiting_for_amount)


@router.message(SendStates.waiting_for_amount)
async def process_amount(message: types.Message, state: FSMContext):
    try:
        amount = float(message.text.strip())
    except ValueError:
        await message.answer("❌ Invalid amount. Enter a number:")
        return

    if amount <= 0:
        await message.answer("❌ Amount must be greater than 0. Try again:")
        return

    await state.update_data(amount=amount)
    await message.answer("🔐 Enter your wallet password to confirm:")
    await state.set_state(SendStates.waiting_for_password)


@router.message(SendStates.waiting_for_password)
async def process_send_password(message: types.Message, state: FSMContext):
    password = message.text
    data = await state.get_data()

    await state.clear()

    await message.answer(
        f"📤 Transaction initiated\n\n"
        f"To: <code>{data['to_address']}</code>\n"
        f"Amount: {data['amount']} ETH\n\n"
        f"⚠️ Sending is not yet enabled in this version."
    )