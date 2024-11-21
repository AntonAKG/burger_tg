from aiogram import Router, filters, types

router = Router()

@router.message(filters.CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Hello! I am a bot!")