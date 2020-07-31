# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('my.sqlite')
c = conn.cursor()

#Функция занесения пользователя в базу
def add_user(username,userpass):
    c.execute("INSERT INTO users (name,password) VALUES ('%s','%s')"%(username,userpass))
    conn.commit()

#Вводим данные
name = raw_input("Введите Логин\n")
passwd = raw_input("Введите Пароль\n")
add_user(name, passwd) 
print('\n')

#Делаем запрос в базу
print("Список пользователей:\n")
c.execute('SELECT * FROM users ORDER BY password')
row = c.fetchone()
#выводим список пользователей в цикле

while row is not None:
   print("name: " + row[0] + " | password: " + row[1])
   row = c.fetchone()


# закрываем соединение с базой
c.close()
conn.close()

#Удаление пользователя из базы
# c.execute("DELETE FROM users WHERE password LIKE '%8%'")
# conn.commit()
