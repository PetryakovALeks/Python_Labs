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

    if 'delete_style' in form:
        style_id = form.getvalue('style_id')
        cursor.execute('DELETE FROM DanceStyles WHERE style_id = ?', (style_id,))
        conn.commit()

except Exception as e:
    print(f"<div style='color:red;'>Ошибка: {str(e)}</div>")

print("""<!DOCTYPE html>
<html>
<head>
    <title>Управление стилями танцев</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial; margin: 20px; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .btn { 
            display: inline-block;
            padding: 6px 12px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 2px;
        }
        .delete-btn { background-color: #f44336; }
        .nav-buttons { margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>Управление стилями танцев</h1>

    <div class="nav-buttons">
        <a href="manage.py" class="btn">Главное меню</a>
        <a href="add_style.py" class="btn">Добавить стиль</a>
        <a href="dancers.py" class="btn">Танцоры</a>
    </div>

    <table>
        <tr>
            <th>ID</th>
            <th>Название</th>
            <th>Происхождение</th>
            <th>Сложность</th>
            <th>Действия</th>
        </tr>
""")

try:
    cursor.execute('SELECT * FROM DanceStyles ORDER BY style_id')
    styles = cursor.fetchall()

    for style in styles:
        print(f"""
        <tr>
            <td>{style[0]}</td>
            <td>{html.escape(style[1])}</td>
            <td>{html.escape(style[2])}</td>
            <td>{html.escape(style[3])}</td>
            <td>
                <form style="display:inline;" method="post" action="">
                    <input type="hidden" name="style_id" value="{style[0]}">
                    <input type="submit" name="delete_style" value="Удалить" class="btn delete-btn">
                </form>
            </td>
        </tr>
        """)

except Exception as e:
    print(f"<tr><td colspan='5' style='color:red;'>Ошибка: {str(e)}</td></tr>")

print("""
    </table>
</body>
</html>
""")

if 'conn' in locals():
    conn.close()
