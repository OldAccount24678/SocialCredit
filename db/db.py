import sqlite3
from config import path_user_db

def CreateDB():
	con = sqlite3.connect(path_user_db)
	cursor = con.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS users(
		bot_id INTEGER PRIMARY KEY AUTOINCREMENT,
		id INT,
		name TEXT,
		credit INT
	)""")
	cursor.close()
	con.close()

def InsertValues(name, id):
	con = sqlite3.connect(path_user_db)
	cursor = con.cursor()
	cursor.execute(f"""INSERT INTO users VALUES (
		NULL,
		{id},
		"{name}",
		0
	)""")
	con.commit()
	cursor.close()
	con.close()

def UpdateValue(znak, num, objj, id):
	con = sqlite3.connect(path_user_db)
	cursor = con.cursor()
	cursor.execute(f"SELECT {objj} FROM users WHERE id = {id}")
	try:
		var = cursor.fetchone()[0]
	except:
		var = 0
	if znak == "+":
		num2 = var + num
	elif znak == "-":
		num2 = var - num
	else:
		print("Ошибка! Только + или -!")
		cursor.close()
		con.close()
		return
	if num2 < 0:
		num2 = 0
	cursor.execute(f"UPDATE users SET {objj} = {num2} WHERE id = {id}")
	con.commit()
	cursor.close()
	con.close()

def Select(objj, fromm, id):
	con = sqlite3.connect(path_user_db)
	cursor = con.cursor()
	cursor.execute(f"SELECT {objj} FROM {fromm} WHERE id = {id}")
	try:
		jaj = cursor.fetchone()[0]
	except:
		jaj = "None"
	cursor.close()
	con.close()
	return jaj

def AllUsers(obj, order_by, limito):
	con = sqlite3.connect(path_user_db)
	cursor = con.cursor()
	cursor.execute(f"SELECT {objj} FROM users ORDER BY {order_by} DESC LIMIT {limito}")
	try:
		jaj = cursor.fetchall()
	except:
		jaj = "None"
	cursor.close()
	con.close()
	return jaj
