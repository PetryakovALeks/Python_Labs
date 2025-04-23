import sqlite3
import xml.etree.ElementTree as ET

# Подключение к БД
conn = sqlite3.connect('fashion.db')
cursor = conn.cursor()

# Создание XML-структуры
root = ET.Element("FashionDatabase")

# Экспорт дизайнеров
cursor.execute("SELECT * FROM designers")
designers = ET.SubElement(root, "Designers")
for row in cursor.fetchall():
    designer = ET.SubElement(designers, "Designer")
    ET.SubElement(designer, "ID").text = str(row[0])
    ET.SubElement(designer, "Name").text = row[1]
    ET.SubElement(designer, "Country").text = row[2]
    ET.SubElement(designer, "YearFounded").text = str(row[3])

# Сохранение в файл
tree = ET.ElementTree(root)
tree.write("fashion_export.xml", encoding="utf-8", xml_declaration=True)
print("Данные экспортированы в fashion_export.xml")

conn.close()