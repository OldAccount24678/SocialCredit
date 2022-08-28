from aiogram.types import Message
import random as r
import asyncio

import db.db as db
from loader import bot, timer

async def minus(message: Message):
	id = db.Select("id", "users", message.from_user.id)
	if not id or id == "None":
		db.InsertValues(message.from_user.first_name, message.from_user.id)
	if message.reply_to_message:
		id_reply = db.Select("id", "users", message.reply_to_message.from_user.id)
		if not id_reply or id_reply == "None":
			db.InsertValues(message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id)
		if message.from_user.id == message.reply_to_message.from_user.id:
			await message.reply("Партия запрещать вредить себе Social Credits!\n\n+1 миска рис 😇🍚")
			return
		if message.from_user.id not in timer:
			rand = r.randint(1, 100)
			db.UpdateValue("-", rand, "credit", message.reply_to_message.from_user.id)
			await bot.send_message(chat_id = message.chat.id, text = f"Вы огорчили партия! Вам не достанется миска рис, мы изымаем ваш балы -{rand}!👎😡", reply_to_message_id = message.reply_to_message.message_id)
			timer.append(message.from_user.id)
			await asyncio.sleep(1800)
			timer.remove(message.from_user.id)
		else:
			await message.reply("🤬👎 Гордость и зло давать можно раз 30 минута")
