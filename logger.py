import datetime as d
import os

def create_note(author, redact=False, old_note=None):
    date = str(d.datetime.now()).split(".")[0]
    name = input("заголовок заметки: ")
    
    print("\nвведите содержимое заметки, чтобы прекратить ввод, напишите 'СТОП' или 'STOP'")
    content = ""

    while True:
        inp = input(">> ")

        if inp != "СТОП" and inp != "STOP":
            content += inp + '\n'
        else:
            content = content[:-1]
            break
        
    importance = input("важность данной заметки: ")
    type = input("какой тип у этой заметки?: ")

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
                text = f.read().replace(old_note, note)

            with open(f"notes\\{author}_notes.txt", "w", encoding="utf-8") as f:
                f.write(text)

            print("заметка успешно изменена")
                
                
def create_user():
    with open("users.txt", "r+", encoding="utf-8") as f:
        name = input("введите имя пользователя: ")

        if f.read().find(name) == -1:
            f.write(name + '\n')
            print("успешно сохранено!")
        else:
            print("данное имя пользователя уже занято")

def list_of_users():
    with open("users.txt", "r", encoding="utf-8") as f:
        print("список доступных пользоваелей:\n" + f.read()[:-1])

def configure_user():
    cont = True
    old_name = input("введите имя пользователя которое хотите поменять: ")
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

def delete_user():
    name = input("введите имя пользователя которого вы хотите удалить\nесли не хотите никого удалять, просто нажмите enter\n>> ")

    if name != "":
        with open("users.txt", "r", encoding="utf-8") as f:
            text = f.read()

            if name not in text:
                print("имя пользователя не найдено")
            else:
                print("удалено успешно")

            text = text.replace(name + '\n', '')

        with open("users.txt", "w", encoding="utf-8") as f:
            f.write(text)

        try:
            os.remove(f"notes\\{name}_notes.txt")
        except: pass

def get_notes(user):    
    with open(f"notes\\{user}_notes.txt", "r", encoding="utf-8") as f:
        text = f.read().split("--------------------------")
        notes = []

        for e in text:
            notes.append('\n'.join(e.split('\n'))[1:])

        return notes

def note_list(user):
    try:    
        notes = get_notes(user)

        print("список ваших заметок:")

        for i in range(1, len(notes)):
            print(f"{i}. " + notes[i].split("\n")[0])

    except FileNotFoundError:
        print("у вас еще нет заметок")

def find_note(user):
    try:
        notes = get_notes(user)
        name = input("введите имя заметки: ")

        for e in notes:
            if e.split('\n')[0] == name:
                print('\n' + e)
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