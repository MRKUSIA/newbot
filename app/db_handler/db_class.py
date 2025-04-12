import sqlite3
import datetime

def create_connector():
    connection = None
    try:
        connection = sqlite3.connect('database.db')
        print("Подключение произошло успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")
    return connection


def create_user(user_id: int,
                 full_name:str = None):
    conn = create_connector()
    cursor = conn.cursor()

    find_user = """ SELECT * FROM users WHERE user_id = ?"""

    cursor.execute(find_user, (user_id,))
    user = cursor.fetchone()

    if user:
        print("Пользователь уже существует")
        return False
    
    create_at = datetime.datetime.now()
    update_at = datetime.datetime.now()
    balance = 0

    create_user = """INSERT INTO users (user_id, full_name, balanse, create_at, update_at)
    VALUES (?, ?, ?, ?, ?)"""
    cursor.execute(create_user, (user_id, full_name, balance, create_at, update_at))
    
    conn.commit()
    return True


create_user(2, "p1n0k10")