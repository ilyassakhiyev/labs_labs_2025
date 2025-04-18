import psycopg2
import csv
from psycopg2 import sql
# -*- coding: utf-8 -*-

conn = psycopg2.connect(
    dbname="data_base",  
    user="postgres",   
    password="jas0mykr555",  
    host="localhost",          
)

cursor = conn.cursor()

def from_csv_to_db(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)  # Пропускаем заголовок
        for line in file:
            user_name, numb = line.strip().split(',')
            insert_query = """
            INSERT INTO basetry (user_name, numb) 
            VALUES (%s, %s);
            """
            cursor.execute(insert_query, (user_name, int(numb)))
    conn.commit()
    print("Данные из CSV файла успешно импортированы в базу данных.")

def insert_user(user_name, numb):
    insert_query = """
    INSERT INTO basetry (user_name, numb) 
    VALUES (%s, %s) RETURNING user_id, user_name, numb;
    """
    cursor.execute(insert_query, (user_name, numb))
    conn.commit()
    user_data = cursor.fetchone()
    print(f"Пользователь добавлен: ID = {user_data[0]}, Имя = {user_data[1]}, Number = {user_data[2]}")
    return user_data[0]  # Возвращаем ID нового пользователя

def update_username(old_name, new_name, conn):
    update_query = """
        UPDATE basetry
        SET user_name = %s
        WHERE user_name = %s
        RETURNING user_id, user_name, numb;
    """
    
    with conn.cursor() as cur:
        cur.execute(update_query, (new_name, old_name))
        user_data = cur.fetchone()
        conn.commit()
        
        if user_data:
            print(f"Данные обновлены: ID = {user_data[0]}, Имя = {user_data[1]}, Новые номеры = {user_data[2]}")
        else:
            print("Пользователь с таким именем не найден.")

def update_numb(old_numb, new_numb, conn):
    update_query = """
        UPDATE basetry
        SET numb = %s
        WHERE numb = %s
        RETURNING user_id, user_name, numb;
    """
    
    with conn.cursor() as cur:
        cur.execute(update_query, (new_numb, old_numb))
        user_data = cur.fetchone()
        conn.commit()
        
        if user_data:
            print(f"Данные обновлены: ID = {user_data[0]}, Имя = {user_data[1]}, Новый номер = {user_data[2]}")
        else:
            print("Пользователь с таким номером не найден.")


def export_to_csv(file_name='exported_data.csv'):
    if not file_name.endswith('.csv'):
        file_name += '.csv'

    select_query = "SELECT user_id, user_name, numb FROM basetry ORDER BY user_id;"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['user_id', 'user_name', 'numb'])  # Header
        for row in rows:
            writer.writerow(row)

    print(f"✅ Данные экспортированы в файл: {file_name}")


def delete_user(user_name):   
    delete_query = """
    DELETE FROM basetry
    WHERE user_name = %s
    RETURNING user_id, user_name;
    """
    cursor.execute(delete_query, (user_name,))
    conn.commit()

    user_data = cursor.fetchone()

    if user_data:
        print(f"Пользователь удален: ID = {user_data[0]}, Имя = {user_data[1]}")
    else:
        print("Пользователь не найден.")

def get_users_sorted_by_number():
    select_query = "SELECT user_id, user_name, numb FROM basetry ORDER BY numb DESC;"
    cursor.execute(select_query)

    rows = cursor.fetchall()

    print("Пользователи, отсортированные по номерам (от максимального):")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Номер: {row[2]}")

if __name__ == '__main__':
    oper = input("Введите операцию (1 - добавить, 2 - удалить, 3 - обновить, 4 - получить всех, 5 - конвертировать в CSV-файл): ")
    if oper == '1':
        b = input("Введите 1 - добавить из CSV, 2 - добавить вручную: ")
        if b == '1':
            file_path = input("Введите путь к CSV файлу: ")
            from_csv_to_db(file_path)
        elif b == '2':
            user_name = input("Введите имя: ")
            numb = int(input("Введите номер телефона: "))
            insert_user(user_name, numb)
    elif oper == '2':
        user_name = input("Введите имя для удаления: ")
        delete_user(user_name)
    elif oper == '3':
        num = int(input("Введите 1 - обновить номер, 2 - обновить имя: "))
        if num == 1:
            old_numb = int(input("Введите старый номер телефона: "))
            new_numb = int(input("Введите новый номер телефона: "))
            update_numb(old_numb, new_numb, conn)
        elif num == 2:
            old_name = input("Введите старое имя: ")
            new_name = input("Введите новое имя: ")
            update_username(old_name, new_name, conn)
    elif oper == '4':
        get_users_sorted_by_number()
    elif oper == '5':
        file_name = input("Введите имя CSV файла (по умолчанию 'exported_data.csv'): ")
        if not file_name:
            file_name = 'exported_data.csv'
        export_to_csv(file_name)
    else:
        print("Неверная операция.")
