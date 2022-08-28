from aiogram.types import Message

import db.db as db

async def stats(message: Message):
	soc = db.Select("credit", "users", message.from_user.id)
	await message.reply(f"Ваш социальный рейтинг: {soc}")
