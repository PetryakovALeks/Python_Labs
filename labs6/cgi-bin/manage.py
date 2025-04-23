#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import cgitb
import sys
import io
import os

cgitb.enable()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, 'dance_studio.db')

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=utf-8\n")

def init_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Dancers (
                dancer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                level TEXT,
                phone TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS DanceStyles (
                style_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                origin TEXT,
                difficulty TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Classes (
                class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                style_id INTEGER,
                dancer_id INTEGER,
                schedule TEXT,
                teacher TEXT,
                FOREIGN KEY (style_id) REFERENCES DanceStyles(style_id),
                FOREIGN KEY (dancer_id) REFERENCES Dancers(dancer_id)
            )
        ''')

        conn.commit()
        conn.close()

    except Exception as e:
        print(f"<div style='color:red;'>Ошибка инициализации базы данных: {str(e)}</div>")

# Создаём таблицы, если их ещё нет
init_db()

# HTML-страница
print("""<!DOCTYPE html>
<html>
<head>
    <title>Танцевальная студия - Главное меню</title>
    <meta charset="utf-8">
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 40px auto; 
            max-width: 800px;
        }
        h1 {
            color: #333;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 10px;
        }
        .nav-section {
            margin: 30px 0;
        }
        .nav-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 10px;
        }
        .btn {
            display: inline-block;
            padding: 12px 20px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            transition: background-color 0.3s;
        }
        .btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Главное меню - Танцевальная студия</h1>

    <div class="nav-section">
        <h2>Управление</h2>
        <div class="nav-buttons">
            <a href="dancers.py" class="btn"> Танцоры</a>
            <a href="styles.py" class="btn"> Стили танцев</a>
        </div>
    </div>

    <div class="nav-section">
        <h2>Добавление данных</h2>
        <div class="nav-buttons">
            <a href="add_dancer.py" class="btn"> Добавить танцора</a>
            <a href="add_style.py" class="btn"> Добавить стиль</a>
        </div>
    </div>
</body>
</html>
""")
