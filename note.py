from datetime import datetime
from file import read_file, save_changes

def get_note():
    title = input('Введите заголовок: ')
    note = input('Введите текст заметки: ')
    return title, note, datetime.now()

def write_note():
    user_data = get_note()
    res = read_file()
    for el in res:
        if el['Заголовок'] == str(user_data[0]):
            print('Такой заголовок уже существует')
            return
    obj = {'Заголовок': user_data[0], 'Заметка': user_data[1], 'Изменено': user_data[2]}
    res.append(obj)
    save_changes(res)

def set_note(note_title):
    res = read_file()
    if check_note(note_title):
        for el in res:
            if el['Заголовок'] == str(note_title):
                print(el['Заметка'])
                el['Заметка'] = input('Введите новый текст заметки: ')
                el['Изменено'] = datetime.now()
                save_changes(res)

def delete_note(note_title):
    res = read_file()
    if check_note(note_title):
        for el in res:
            if el['Заголовок'] == str(note_title):
                res.remove(el)
                save_changes(res)

def check_note(note_title):
    res = read_file()
    for el in res:
        if el['Заголовок'] == str(note_title): return bool
    else: print('Заметки с таким заголовком не существует')