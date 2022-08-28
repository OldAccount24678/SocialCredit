from loader import dp
import db.db as db

from aiogram.types import BotCommand
import os

async def reg_handlers(dp):
#~~~~~~~~~~~~~~~~~~~~~~~~~#

	from handlers.commands.start import start
	dp.register_message_handler(start, commands=["start"])

	from handlers.commands.stats import stats
	dp.register_message_handler(stats, commands=["stats"])

	from handlers.commands.top import top
	dp.register_message_handler(top, commands=["top"])

	from handlers.commands.info import info
	dp.register_message_handler(info, commands=["info"])

	from handlers.commands.donate import donate
	dp.register_message_handler(donate, commands=["donate"])

	from handlers.commands.plus import plus
	dp.register_message_handler(plus, text=["+"])

	from handlers.commands.minus import minus
	dp.register_message_handler(minus, text=["-"])

#~~~~~~~~~~~~~~~~~~~~~~~~~#





# other
	db.CreateDB()
	await dp.bot.set_my_commands(
		[
			BotCommand("stats", "узнать свой социальный рейтинг"),
			BotCommand("top", "топ социальный рейтинг"),
			BotCommand("info", "о боте"),
			BotCommand("donate", "поддержать создателя")
		]
	)
	try:
		os.system("clear")
		logger = f"""
Version: 0.1 | Author: @AmokDev
Bot: @SocialCreditsBot | Channel: @end_soft
"""
		print(logger)
	except:
		pass
