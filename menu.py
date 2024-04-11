from os.path import exists
from file import create_file, check_file, read_file
from note import write_note, set_note, delete_note

def menu():
    while True:
        command = input('Введите команду (n - создать заметку, s - читать список заметок, '
                        'r - редактировать заметку, d - удалить заметку q - выйти): ')
        if command == 'q':
            break
        elif command == 'n':
            if not exists('notepad.csv'):
                create_file()
            write_note()
        elif command == 's':
            if check_file():
                for i in read_file():
                    print(i)
        elif command == 'r':
            if check_file():
                note_title = input('Заголовок заметки: ')
                set_note(note_title)
        elif command == 'd':
            if check_file():
                note_title = input('Заголовок заметки: ')
                delete_note(note_title)
        else: print('Команда введена не корректно')