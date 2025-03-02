from logger import *

def indent(): print('\n' * 50)

while True:
    while True: #register
        user = input('\nвведите свое имя пользователя чтобы войти в аккаунт\nесли вы забыли имя пользователя или у вас его нет, нажмите enter\n>> ')

        if user == '':
            inp = input('\n1. создать пользователя\n2. показать список доступных пользователей\nдля отмены нажмите enter\n>> ')

            if inp == '1':
                create_user()
            elif inp == '2':
                list_of_users()
                
        elif find_user(user):
            print('успешно')
            break
        else:
            print('такого имени пользователя не существует')

    con = True
    while con:
        inp = input('\n1. заметки\n2. пользователи\n>> ')

        if inp == '1':
            while True:
                inp = input('\n1. создать заметку\n2. показать список ваших заметок' + 
                '\n3. показать определенную заметку\n4. изменить заметку\n5. удалить заметку\n6. выйти\n>> ')

                indent()
                if inp == '1':
                    create_note(user)
                elif inp == '2':
                    note_list(user)
                elif inp == '3':
                    find_note(user)
                elif inp == '4':
                    redact_note(user)
                elif inp == '5':
                    delete_note(user)
                elif inp == '6':
                    break

        elif inp == '2':
            while True:
                inp = input('\n1. создать нового пользователя\n2. показать список доступных пользователей' + 
                '\n3. поменять пользователя\n4. изменить имя текущего аккаунта\n5. удалить текущего пользователя\n6. выйти\n>> ')

                indent()
                if inp == '1':
                    create_user()
                elif inp == '2':
                    list_of_users()
                elif inp == '3':
                    user = change_user(user)
                elif inp == '4':
                    configure_user(user)
                elif inp == '5':
                    delete_user(user)
                    con = False
                    break
                elif inp == '6':
                    break