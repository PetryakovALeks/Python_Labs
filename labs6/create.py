import sqlite3
import os
from pathlib import Path

def create_database():
    # Получаем абсолютный путь к файлу БД
    db_path = Path('dance_studio.db').absolute()
    
    # Удаляем старую БД, если она существует
    if db_path.exists():
        db_path.unlink()
    
    try:
        # Подключаемся к базе данных (файл создастся автоматически)
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        # Создаем таблицу танцоров
        cursor.execute('''
        CREATE TABLE Dancers (
            dancer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            level TEXT,
            phone TEXT
        )''')
        
        # Создаем таблицу стилей танцев
        cursor.execute('''
        CREATE TABLE DanceStyles (
            style_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            origin TEXT,
            difficulty TEXT
        )''')
        
        # Создаем таблицу занятий
        cursor.execute('''
        CREATE TABLE Classes (
            class_id INTEGER PRIMARY KEY AUTOINCREMENT,
            style_id INTEGER,
            dancer_id INTEGER,
            schedule TEXT,
            teacher TEXT,
            FOREIGN KEY (style_id) REFERENCES DanceStyles(style_id),
            FOREIGN KEY (dancer_id) REFERENCES Dancers(dancer_id)
        )''')
        
        # Добавляем тестовые данные
        cursor.executemany('''
        INSERT INTO Dancers (name, age, level, phone) VALUES (?, ?, ?, ?)
        ''', [
            ('Анна Смирнова', 25, 'Профессионал', '+79161234567'),
            ('Иван Петров', 18, 'Начинающий', '+79162345678'),
            ('Мария Иванова', 30, 'Средний', '+79163456789')
        ])
        
        cursor.executemany('''
        INSERT INTO DanceStyles (name, origin, difficulty) VALUES (?, ?, ?)
        ''', [
            ('Бальные танцы', 'Европа', 'Средний'),
            ('Хип-хоп', 'США', 'Высокий'),
            ('Сальса', 'Куба', 'Низкий')
        ])
        
        cursor.executemany('''
        INSERT INTO Classes (style_id, dancer_id, schedule, teacher) VALUES (?, ?, ?, ?)
        ''', [
            (1, 1, 'Пн, Ср 19:00', 'Ольга Козлова'),
            (2, 2, 'Вт, Чт 18:00', 'Дмитрий Соколов'),
            (3, 3, 'Пт 20:00', 'Алексей Иванов')
        ])
        
        # Сохраняем изменения
        conn.commit()
        
        # Проверяем, что файл создан
        if db_path.exists():
            print(f"База данных успешно создана: {db_path}")
            print(f"Размер файла: {db_path.stat().st_size} байт")
        else:
            print("Ошибка: файл базы данных не был создан")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    create_database()