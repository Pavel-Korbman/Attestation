from csv import DictWriter, DictReader
from os.path import exists

def create_file():
    with open('notepad.csv', 'w', encoding='UTF-8') as data:
        f_writer = DictWriter(data, fieldnames=['Заголовок', 'Заметка', 'Изменено'])
        f_writer.writeheader()

def check_file():
    if exists('notepad.csv'): return bool
    else: print('Заметки не создавались')

def read_file():
    with open('notepad.csv', encoding='UTF-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def save_changes(res):
    with open('notepad.csv', 'w', encoding='UTF-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Заголовок', 'Заметка', 'Изменено'])
        f_writer.writeheader()
        f_writer.writerows(res)
    print('Изменения сохранены')