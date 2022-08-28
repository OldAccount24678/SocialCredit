from aiogram.types import Message

import db.db as db

async def info(message: Message):
	rows = db.AllUsers("credit", "credit", 99999)
	obsh = 0
	for i in rows:
		obsh += i[0]
	await message.reply(f"""
<code>Количество пользователей: {len(rows)}
Общий социальный рейтинг: {obsh}
Создатель:</code> @AmokDev
""")
