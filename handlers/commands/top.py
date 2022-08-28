from aiogram.types import Message
from html import escape

import db.db as db

async def top(message: Message):
	msg = ""
	rows = db.AllUsers("credit, name", "credit", 10)
	for i in rows:
		msg += f"{rows.index(i)+1}. {escape(i[1])} - {i[0]}\n"
	await message.reply(str(msg))
