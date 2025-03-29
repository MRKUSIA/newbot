import sqlite3

def create_connector():
    conection = None
    try:
        connection = sqlite3.connect('database.db')
        print("Подключение произошло успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")
    return connection


def create_user(user_id: int,
                 username: int,
                 full_name:str = None):
    conn = create_connector()
    cursor = conn.cursor()

    find_user = """ SELET * FROM users WHERE users WHERE user_id = ?"""

    cursor.execute(find_user, (user_id))
    user = cursor.fetchone()

    if not user:
        req_date = str((datetime.datetime.now()))
        create_user = """INSERT INTO users (user_id,full_name, req_date)"
        VALUES (?, ?,   datetime('now))"""
        cursor.execute(create_user, (user_id, full_name,))
        conn.commit()
        return user
    
    crate_user(1, "p1n0f10")
