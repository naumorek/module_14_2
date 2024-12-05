'''Задача "Средний баланс пользователя":
Для решения этой задачи вам понадобится решение предыдущей.
Для решения необходимо дополнить существующий код:
Удалите из базы данных not_telegram.db запись с id = 6.
Подсчитать общее количество записей.
Посчитать сумму всех балансов.
Вывести в консоль средний баланс всех пользователей.



Пример результата выполнения программы:
Выполняемый код:
# Код из предыдущего задания
# Удаление пользователя с id=6
# Подсчёт кол-ва всех пользователей
# Подсчёт суммы всех балансов
print(all_balances / total_users)
connection.close()

Вывод на консоль:
700.0'''

import sqlite3
import random

connection=sqlite3.connect('not_telegram.db')
cursor=connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)    
''')

#cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email) ")
#for i in range(1,11):
#    cursor.execute("INSERT INTO Users (username,email,age, balance) VALUES (?,?,?,?)",(f'new_users_{i}',f'ex{i}@gmail.com',f"{random.randint(18,96)}","1000"))
#for i in range (1,11,2):
#    cursor.execute(f'UPDATE Users SET balance = ? WHERE id= ? ',(500,i))
#for i in range (1,11,3):
#    cursor.execute(f'DELETE FROM Users WHERE id= ? ',(i,))
#cursor.execute('SELECT username, email, age, balance FROM Users WHERE age < ?', (60,))
#users=cursor.fetchall()
#for user in users:
#    print(f'Имя: {user[0]} | Э-майл: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
#cursor.execute(f'DELETE FROM Users WHERE id= ? ',(6,))
cursor.execute("SELECT COUNT(*) FROM Users")
total1=cursor.fetchone()[0]
print('всего пользователей:', total1)
cursor.execute("SELECT SUM(balance) FROM Users")
total2=cursor.fetchone()[0]
cursor.execute("SELECT AVG(balance) FROM Users")
total3=cursor.fetchone()[0]
print('Средний баланс:', total3)

connection.commit()
connection.close()