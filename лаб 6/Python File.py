import sqlite3

# Создаем базу данных
conn = sqlite3.connect('fashion.db')
cursor = conn.cursor()

# Создаем таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Designers (
    designer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT,
    birth_year INTEGER,
    specialty TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Collections (
    collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    designer_id INTEGER,
    season TEXT NOT NULL,
    year INTEGER NOT NULL,
    theme TEXT,
    FOREIGN KEY (designer_id) REFERENCES Designers(designer_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS FashionShows (
    show_id INTEGER PRIMARY KEY AUTOINCREMENT,
    collection_id INTEGER,
    location TEXT NOT NULL,
    date TEXT NOT NULL,
    attendees INTEGER,
    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id)
)
''')

