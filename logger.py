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

    note = f"""
--------------------------
{name}

{content}

важность заметки: {importance}
тип заметки: {type}
автор: {author}
дата: {date}
"""
    
    print('\n'*30 + f"""
ваша заметка:
{note}
""")

    inp = input("сохранить?\n 1. да\n 2. нет\n>> ")

    while inp != "1" and inp != "2":

        print("некорректный ответ")
        inp = input(">> ")

    if inp == "1":
        with open(f"notes\\{author}_notes.txt", "a") as f:
            f.write(note[1:])