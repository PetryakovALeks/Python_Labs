import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('fashion.db')
cursor = conn.cursor()

# Запрос 1: Вывести все коллекции с указанием дизайнера
cursor.execute("""
SELECT c.name, d.name, c.season, c.year 
FROM collections c 
JOIN designers d ON c.designer_id = d.designer_id
""")
print("=== Все коллекции ===")
for row in cursor.fetchall():
    print(f"Коллекция: {row[0]}, Дизайнер: {row[1]}, Сезон: {row[2]}, Год: {row[3]}")

# Запрос 2: Средняя цена одежды по сезонам
cursor.execute("""
SELECT c.season, AVG(cl.price) 
FROM clothing cl 
JOIN collections c ON cl.collection_id = c.collection_id 
GROUP BY c.season
""")
print("\n=== Средняя цена одежды по сезонам ===")
for row in cursor.fetchall():
    print(f"Сезон: {row[0]}, Средняя цена: {row[1]:.2f} $")

# Запрос 3: Самый дорогой предмет одежды
cursor.execute("""
SELECT type, color, MAX(price) 
FROM clothing
""")
most_expensive = cursor.fetchone()
print(f"\nСамый дорогой предмет: {most_expensive[0]} ({most_expensive[1]}), Цена: {most_expensive[2]} $")

# Закрытие соединения
conn.close()