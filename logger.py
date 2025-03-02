import datetime as d
import os

def create_note(author, redact=False, old_note=None, to_change=None):
    def init(num):
        nonlocal name, content, importance, type

        if num == 0:
            pass
        elif num == 1:
            name = input("заголовок заметки: ")
        elif num == 2:
            print("\nвведите содержимое заметки, чтобы прекратить ввод, напишите 'СТОП' или 'STOP'")
            content = ""

            while True:
                inp = input(">> ")

                if inp != "СТОП" and inp != "STOP":
                    content += inp + '\n'
                else:
                    content = content[:-1]
                    break
        elif num == 3:
            while True:
                importance = int(input("важность данной заметки (число от 1 до 10): "))
                if importance in range(1, 11):
                    break
                else:
                    print("важность не может быть меньше 1 или больше 10")
        
        elif num == 4:
            type = input("какой тип у этой заметки?: ")
        else:
            raise


    if not redact:
        date = str(d.datetime.now()).split(".")[0]
        init(1)
        init(2)
        init(3)
        init(4)

    else:
        name = old_note.split('\n')[1]
        content = old_note.split('\n\n')[1]
        date = old_note.split('\n')[-2][6:]
        importance = old_note.split('\n')[-5][18:]
        type = old_note.split('\n')[-4][13:]

        while True:
            inp = input("что хотите поменять в заметке?\n0. ничего (отмена)\n1. имя\n2. содержимое\n3. важность\n4. тип\n>> ")

            try:
                init(int(inp))
                break
            except RuntimeError:
                print("можно вводить только числа от 0 до 4")

#++++++++++++++++++++++++++
    note = f"""
--------------------------
{name}

{content}

важность заметки: {importance}
тип заметки: {type}
автор: {author}
дата: {date}
"""  #++++++++++++++++++++++++++

#>>>>>>>>>>>>>>>>>>>>>>>>>>>
    print('\n'*30 + f"""
ваша заметка:
{note}
""")  #>>>>>>>>>>>>>>>>>>>>>>>>>


    inp = input("сохранить?\n 1. да\n 2. нет\n>> ")

    while inp != "1" and inp != "2":

        print("некорректный ответ")
        inp = input(">> ")

    if not redact:
        if inp == "1":
            with open(f"notes\\{author}_notes.txt", "a", encoding="utf-8") as f:
                f.write(note[1:])
            print("заметка успешно сохранена")
    else:
        if inp == "1":
            with open(f"notes\\{author}_notes.txt", "r", encoding="utf-8") as f:
                text = f.read().replace(old_note, note[1:])

            with open(f"notes\\{author}_notes.txt", "w", encoding="utf-8") as f:
                f.write(text)

            print("заметка успешно изменена")
                





def find_user(user):
    bool = True

    with open('users.txt', 'r', encoding='utf-8') as f:
        for e in f.readlines():
            if e[:-1] == user:
                break
        else:
            bool = False

    return bool

def create_user():
    with open("users.txt", "a", encoding="utf-8") as f:
        name = input("введите имя пользователя: ")

        if not find_user(name) and name != '':
            f.write(name + '\n')
            print("успешно сохранено!")
        else:
            print("данное имя пользователя уже занято")

def list_of_users():
    with open("users.txt", "r", encoding="utf-8") as f:
        text = f.read()
        
        if text != '':
            print("список доступных пользоваелей:\n" + text[:-1])
        else:
            print('нет доступных пользователей')

def configure_user(user):
    cont = True
    old_name = user
    new_name = input("введите новое имя: ")

    with open("users.txt", "r", encoding="utf-8") as f:
        text = f.readlines()

        if "".join(text).find(new_name) == -1:
            for i in range(len(text)):

                if text[i] == old_name + "\n":
                    text[i] = new_name + "\n"
                    print("имя пользователя успешно изменено")
                    break
            else:
                print("старое имя пользователя не найдено")
                cont = False
        else:
            print("новое имя пользователя уже используется")
            cont = False
    
    with open("users.txt", "w", encoding="utf-8") as f:
        f.writelines(text)

    if cont:
        try:
            with open(f"notes\\{old_name}_notes.txt", "r", encoding="utf-8") as f:
                text = f.read()
            
            os.remove(f"notes\\{old_name}_notes.txt")

            with open(f"notes\\{new_name}_notes.txt", "w", encoding="utf-8") as f:
                f.write(text)
        except: pass

def delete_user(user):
    name = user

    while True:
        inp = input('все ваши заметки будут удалены, точно хотите удалить аккаунт?\n1. да\n2. нет\n>> ')
        
        if inp == '1' or inp == '2':
            break
        else:
            print('некорректный ответ')

    if inp == '1':
        print(1)
        with open("users.txt", "r", encoding="utf-8") as f:
            text = f.readlines()

            for i in range(len(text)):
                if text[i] == name + '\n':
                    text.pop(i)
                    break

            print("удалено успешно")

        with open("users.txt", "w", encoding="utf-8") as f:
            f.writelines(text)

        try:
            os.remove(f"notes\\{name}_notes.txt")
        except: pass

def get_notes(user):    
    with open(f"notes\\{user}_notes.txt", "r", encoding="utf-8") as f:
        text = f.read().split("--------------------------")
        notes = []

        if text != ['']:
            
            for e in text:
                notes.append('\n'.join(e.split('\n'))[1:])

        else:
            print("у вас еще нет заметок")

        return notes[1:]

def note_list(user):
    try:    
        notes = get_notes(user)

        for i in range(len(notes)):
            if i == 0:
                 print("список ваших заметок:")

            print(f"{i+1}. " + notes[i].split("\n")[0])

    except FileNotFoundError:
        print("у вас еще нет заметок")

def find_note(user):
    try:
        notes = get_notes(user)
        name = input("введите имя заметки: ")

        for e in notes:
            if e.split('\n')[0] == name:
                print('--------------------------\n' + e)
                break
        else:
            print("заметка не найдена")

    except FileNotFoundError:
        print("у вас еще нет заметок")

def redact_note(user):
    try:
        notes = ["--------------------------\n" + e for e in get_notes(user)]
        name = input("введите имя заметки: ")

        for e in notes:
            if e.split('\n')[1] == name:
                create_note(user, redact=True, old_note=e)
                break
        else:
            print("заметка не найдена")

    except FileNotFoundError:
        print("у вас еще нет заметок")

def delete_note(user):
    try:
        notes = ["--------------------------\n" + e for e in get_notes(user)]
        name = input("введите имя заметки: ")

        for e in notes:
            if e.split('\n')[1] == name:
                with open(f"notes\\{user}_notes.txt", "r", encoding="utf-8") as f:
                    text = f.read().replace(e, "")

                with open(f"notes\\{user}_notes.txt", "w", encoding="utf-8") as f:
                    f.write(text)

                print("заметка успешно удалена")
                break
        else:
            print("заметка не найдена")

    except FileNotFoundError:
        print("у вас еще нет заметок")

def change_user(old_user):
    user = input('введите имя пользователя: ')

    if find_user(user):
        print('успешно')
        return user

    else:
        print('имя пользователя не найдено')
        return old_user