import datetime as d

def create_note(author):
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

    if inp == "1":
        with open(f"notes\\{author}_notes.txt", "a", encoding="utf-8") as f:
            f.write(note[1:])

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
list_of_users()