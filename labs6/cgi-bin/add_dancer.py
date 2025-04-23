#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import cgi
import cgitb
import sys
import io
import html
import os

cgitb.enable()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, 'dance_studio.db')

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if form.getvalue('name'):
        name = form.getvalue('name')
        age = int(form.getvalue('age'))
        level = form.getvalue('level')
        phone = form.getvalue('phone')

        cursor.execute(
            "INSERT INTO Dancers (name, age, level, phone) VALUES (?, ?, ?, ?)",
            (name, age, level, phone)
        )
        conn.commit()

        print("Status: 303 See Other")
        print("Location: dancers.py")
        print()
        sys.exit()

except Exception as e:
    print(f"<div style='color:red;'>Ошибка: {str(e)}</div>")

finally:
    if 'conn' in locals():
        conn.close()

print("""<!DOCTYPE html>
<html>
<head>
    <title>Добавить танцора</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial; max-width: 600px; margin: 20px auto; }
        form { background: #f5f5f5; padding: 20px; border-radius: 5px; }
        input, select { width: 100%; padding: 8px; margin: 5px 0 15px; }
        .btn { 
            background: #4CAF50; 
            color: white; 
            padding: 10px; 
            border: none;
            text-decoration: none;
            display: inline-block;
            margin-top: 10px;
        }
        .nav-buttons { margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>Добавить нового танцора</h1>

    <div class="nav-buttons">
        <a href="manage.py" class="btn">Главное меню</a>
        <a href="dancers.py" class="btn">Список танцоров</a>
    </div>

    <form method="post">
        Имя: <input type="text" name="name" required><br>
        Возраст: <input type="number" name="age" required><br>
        Уровень:
        <select name="level" required>
            <option value="Начинающий">Начинающий</option>
            <option value="Средний">Средний</option>
            <option value="Продвинутый">Продвинутый</option>
        </select><br>
        Телефон: <input type="text" name="phone" required><br>
        <input type="submit" value="Добавить" class="btn">
    </form>
</body>
</html>""")
