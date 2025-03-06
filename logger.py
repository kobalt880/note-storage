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
                try:
                    importance = int(input("важность данной заметки (число от 1 до 10): "))
                    if importance in range(1, 11):
                        break
                    else:
                        print("важность не может быть меньше 1 или больше 10")
                except ValueError:
                    print('можно вводить только числа')

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

def delete_password(user, change=False):
    if find_password(user):
        with open('passwords.txt', 'r', encoding='utf-8') as f:
            text = f.readlines()

            for i in range(len(text)):
                if text[i][:len(user)+1] == f'{user}:':
                    text[i] = ''

        with open('passwords.txt', 'w', encoding='utf-8') as f:
            f.writelines(text)
    
            if not change:
                print('пароль успешно удален')
    else:
        print('у вас не установлен пароль')

def find_password(user):
        bool = False
        
        with open('passwords.txt', 'r', encoding='utf-8') as f:
            text = f.readlines()

            for e in text:
                if e[:len(user)+1] == f'{user}:':
                    bool = True

        return bool

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

        return new_name
    
        if find_password(old_name):
            create_password(new_name, change=True, old_user=old_name)

def delete_user(user, glob=False):
    name = user

    if glob:
        name = input('введите имя пользователя: ')

    while find_user(name):
        inp = input('все заметки будут удалены, точно хотите удалить аккаунт?\n1. да\n2. нет\n>> ')
        
        if inp == '1' or inp == '2':
            break
        else:
            print('некорректный ответ')
    else:
        inp = None
        print('имя пользователя не найдено')

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

        if find_password(user):
            delete_password(user, change=True)

def get_notes(user):
    with open(f"notes\\{user}_notes.txt", "r", encoding="utf-8") as f:
        text = f.read().split("--------------------------")
        notes = []

        if text != ['']:
            
            for e in text:
                notes.append('\n'.join(e.split('\n'))[1:])

        else:
            raise FileNotFoundError

        return notes[1:]

def note_list(user):
    try:    
        notes = get_notes(user)

        for i in range(len(notes)):
            if i == 0:
                 print("список ваших заметок:")

            print(f"{i+1}. " + notes[i].split("\n")[0] + f' ({'!' * int(notes[i].split('\n')[-5].split(': ')[-1])})')

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

def get_password(user):
    with open('passwords.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()

        for e in text:
            if e.split(':')[0] == user:
                return e.split(':')[1]

def create_password(user, change=False, old_user=None):
    while not find_password(user) and not change:
        inp = input('если вы забудете свой пароль, вы больше не сможете войти в свой аккаунт. установить пароль?\n1. да\n2. нет\n>> ')

        if inp == '1' or inp == '2':
            break
        else:
            print('некорректный ответ')
    else:
        inp = '1'

    if inp == '1':
        with open('passwords.txt', 'a', encoding='utf-8') as f:
            if not change:
                password = input('введите пароль: ')
            else:
                password = get_password(old_user)

            if not find_password(user):
                f.write(f'{user}:{password}\n')

            else:
                with open('passwords.txt', 'r', encoding='utf-8') as f:
                    text = f.readlines()

                    for i in range(len(text)):

                        if text[i][:len(user)+1] == f'{user}:':
                            text[i] = f'{user}:{password}\n'

                    with open('passwords.txt', 'w', encoding='utf-8') as f:
                        f.writelines(text)
            if change:
                delete_password(old_user, change=True)
            else:
                print('пароль успешно сохранен')

def input_password(user):
    bool = True
    
    if find_password(user):
        bool = False
        password = input('введите пароль: ')

        with open('passwords.txt', 'r', encoding='utf-8') as f:
            text = f.readlines()

            for e in text:
                if e[:len(user)+1] == f'{user}:' and e[len(user)+1:-1] == password:
                    bool = True
                    break
            else:
                print('неверный пароль')

    return bool

def change_user(old_user):
    user = input('введите имя пользователя: ')

    if find_user(user) and input_password(user):
        print('успешно')
        return user

    else:
        print('не удалось войти')
        return old_user

def filtered_note_list(user):
    def init(num):
        global val, str_index, str_index, split_str, split_index
        val = ''

        if num == 1:

            val = input('введите важность: ')
            
            str_index = -5
            split_str = ': '
            split_index = -1

            try:
                if int(val) < 1 or int(val) > 10:
                    print('важность не может быть меньше 1 или больше 10')
            except ValueError:
                print('можно вводить только числа') 

        elif num == 2:

            val += input('введите год: ') + '|'
            val += input('введите номер месяца: ') + '|'
            val += input('введите день: ')


            try:
                splited_val = val.split('|')
                for i in range(1, len(splited_val)):

                    if int(splited_val[i]) <= -1:
                        splited_val[i] = f'{int(splited_val[i]) * -1}'

                    if int(splited_val[i]) <= 10 and len(splited_val[i]) < 2:
                        splited_val[i] = '0' + splited_val[i]

                err = False
            except:
                err = True            
                

            val = '-'.join(splited_val)
            
            str_index = -2
            split_str = ' '
            split_index = 1

            if (len(splited_val[1]) != 2 or len(splited_val[2]) != 2 or int(splited_val[1]) == 0 or int(splited_val[2]) == 0
            or int(splited_val[1]) > 12 or int(splited_val[2]) > 31) or err:
                print('неверно введена дата')

        else:
            val = None

    try:
        notes = get_notes(user)

        inp = input('1. найти заметки по важности\n2. найти заметки по дате\n>> ')
        init(int(inp))

        result = False
        number = 1

        print()
        for e in notes:

            if e.split('\n')[str_index].split(split_str)[split_index] == val:
                print(f'{number}. {e.split('\n')[0]}' + (f' ({'!' * int(e.split('\n')[-5].split(': ')[-1])})' if len(val) > 2 else ''))

                number += 1
                result = True

        if not result:
            print('результаты не найдены')

    except FileNotFoundError:
        print('у вас еще нет заметок')

def sort_notes(user):
    def calculate_date(str):
        nonlocal att

        sum = 0
        string = str.split('-')
        prod = 365

        for i in range(len(string)):

            if i == 1:
                for i2 in range(1, int(string[i])):
                    month = 31 if i2 in [1, 3, 5, 7, 8, 10, 12] else 30 if i2 != 2 else 28
                    sum += month
                prod = 1
            
            sum += int(string[i]) * prod
        
        return sum

    def init(num):
        global val, str_index, split_str, split_index
        val = None

        if num == 1:
            str_index = -5
            split_str = ': '
            split_index = -1

        elif num == 2:
            str_index = -2
            split_str = ' '
            split_index = 1

        elif num == 3:
            str_index = 0
            split_str = None
            split_index = 0

        else:
            raise ValueError

        val = [e[str_index].split(split_str)[split_index] for e in [e.split('\n') for e in get_notes(user)]]

        if num == 2:
            val = [calculate_date(e) for e in val]
            val.sort()

        elif num == 3:
            val = [ord(e[0]) for e in val]
            val.sort()

        elif num == 1:
            val = [int(e) for e in val]
            val.sort()
            val.reverse()

    try:
        notes = get_notes(user)

        inp = int(input("1. отсортировать заметки по важности\n2. отсортировать заметки по дате\n" +
                        "3. отсортировать заметки по имени (по алфавиту)\n>> "))
        init(inp)
        
        exists_elem = []
        number = 1
        text = ''

        print('\n')
        for e in val:
            for e2 in notes:
                name = e2.split('\n')[0]

                if inp == 1:
                    att = int(e2.split('\n')[str_index].split(split_str)[split_index])

                elif inp == 2:
                    att = calculate_date(e2.split('\n')[str_index].split(split_str)[split_index])

                elif inp == 3:
                    att = ord(name[0])


                if name not in exists_elem and att == e:
                    exists_elem.append(name)

                    number += 1
                    text += '--------------------------\n' + e2

        with open(f'notes\\{user}_notes.txt', 'w', encoding='utf-8') as f:
            f.write(text)

        print('заметки успешно отсортированы')


    except FileNotFoundError:
        print('у вас еще нет заметок')
    except ValueError:
        print('неверно введены данные')
