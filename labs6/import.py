import sqlite3
import xml.etree.ElementTree as ET

def export_to_xml():
    conn = sqlite3.connect('dance_studio.db')
    cursor = conn.cursor()
    
    # Создаем корневой элемент XML
    root = ET.Element('DanceStudio')
    
    # Экспорт танцоров
    dancers = ET.SubElement(root, 'Dancers')
    for row in cursor.execute('SELECT * FROM Dancers'):
        dancer = ET.SubElement(dancers, 'Dancer')
        ET.SubElement(dancer, 'ID').text = str(row[0])
        ET.SubElement(dancer, 'Name').text = row[1]
        ET.SubElement(dancer, 'Age').text = str(row[2])
        ET.SubElement(dancer, 'Level').text = row[3]
        ET.SubElement(dancer, 'Phone').text = row[4]
    
    # Экспорт стилей танцев
    styles = ET.SubElement(root, 'DanceStyles')
    for row in cursor.execute('SELECT * FROM DanceStyles'):
        style = ET.SubElement(styles, 'Style')
        ET.SubElement(style, 'ID').text = str(row[0])
        ET.SubElement(style, 'Name').text = row[1]
        ET.SubElement(style, 'Origin').text = row[2]
        ET.SubElement(style, 'Difficulty').text = row[3]
    
    # Запись XML в файл
    tree = ET.ElementTree(root)
    tree.write('dance_studio.xml', encoding='utf-8', xml_declaration=True)
    print("Экспорт в XML завершен (dance_studio.xml)")
    
    conn.close()

def import_from_xml():
    conn = sqlite3.connect('dance_studio.db')
    cursor = conn.cursor()
    
    # Очистка таблиц перед импортом
    cursor.execute('DELETE FROM Dancers')
    cursor.execute('DELETE FROM DanceStyles')
    
    # Чтение XML файла
    tree = ET.parse('dance_studio.xml')
    root = tree.getroot()
    
    # Импорт танцоров
    for dancer in root.find('Dancers'):
        cursor.execute('''
        INSERT INTO Dancers (dancer_id, name, age, level, phone)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            int(dancer.find('ID').text),
            dancer.find('Name').text,
            int(dancer.find('Age').text),
            dancer.find('Level').text,
            dancer.find('Phone').text
        ))
    
    # Импорт стилей танцев
    for style in root.find('DanceStyles'):
        cursor.execute('''
        INSERT INTO DanceStyles (style_id, name, origin, difficulty)
        VALUES (?, ?, ?, ?)
        ''', (
            int(style.find('ID').text),
            style.find('Name').text,
            style.find('Origin').text,
            style.find('Difficulty').text
        ))
    
    conn.commit()
    print("Импорт из XML завершен")
    conn.close()

# Пример использования
export_to_xml()
# import_from_xml()  # Раскомментировать для импорта