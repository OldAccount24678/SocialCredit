from aiogram.types import Message

async def donate(message: Message):
	await message.reply("""
Доступные кошельки:

Qiwi: <a href="https://qiwi.com/n/AmokDev">AmokDev</a>
ЮMoney: <code>4100117886581372</code>
""")
