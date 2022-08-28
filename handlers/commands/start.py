from aiogram.types import Message

async def start(message: Message):
	await message.reply_sticker("CAACAgQAAxkBAAEJJ29jCqE4g1DUeruiWp5qsmGjKdhqkQACdggAAnAZ4FLMfDAQjIsPIx4E")
	await message.reply("🍚 Партия приветствовать тебя путник!")
