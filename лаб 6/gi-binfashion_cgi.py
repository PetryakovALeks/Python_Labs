#!/usr/bin/env python3
import sqlite3
import cgi

# Подключение к БД
conn = sqlite3.connect('fashion.db')
cursor = conn.cursor()

# Заголовок HTML
print("Content-type: text/html\n")
print("<html><head><title>Модная база данных</title></head><body>")

# Обработка формы
form = cgi.FieldStorage()
if "action" in form:
    action = form.getvalue("action")
    if action == "show_designers":
        cursor.execute("SELECT * FROM designers")
        print("<h2>Дизайнеры</h2><ul>")
        for row in cursor.fetchall():
            print(f"<li>{row[1]} ({row[2]}, основан в {row[3]})</li>")
        print("</ul>")
    elif action == "show_collections":
        cursor.execute("SELECT * FROM collections")
        print("<h2>Коллекции</h2><ul>")
        for row in cursor.fetchall():
            print(f"<li>{row[1]} (Сезон: {row[2]}, Год: {row[3]})</li>")
        print("</ul>")

# Форма для выбора действия
print("""
<h1>Модная база данных</h1>
<form method="post">
    <select name="action">
        <option value="show_designers">Показать дизайнеров</option>
        <option value="show_collections">Показать коллекции</option>
    </select>
    <input type="submit" value="Отправить">
</form>
""")

print("</body></html>")
conn.close()