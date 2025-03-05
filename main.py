from logger import *

def indent(): print('\n' * 50)

end = False
while not end:
    while True: #register
        user = input('\nвведите имя пользователя чтобы войти в аккаунт\nесли вы забыли имя аккаунта или у вас его нет, нажмите enter\n>> ')
        indent()

        if user == '':
            inp = input('\n1. создать аккаунт\n2. показать список доступных пользователей\n3. удалить аккаунт\nдля отмены нажмите enter\n>> ')
            indent()

            if inp == '1':
                create_user()
            elif inp == '2':
                list_of_users()
            elif inp == '3':
                delete_user(user, glob=True)
                
        elif find_user(user) and input_password(user):
            indent()
            print('успешно')
            break
        else:
            print('не удалось совершить вход')

    active_user = True
    while active_user:
        inp = input(f'\n{user}\n1. заметки\n2. аккаунт\n3. закрыть приложение\n>> ')
        indent()

        if inp == '1':
            while True:
                inp = input('\n1. создать заметку\n2. показать список ваших заметок' + 
                '\n3. показать определенную заметку\n4. изменить заметку\n5. удалить заметку\n6. найти заметки по важности/дате\n'
                + '7. выйти из раздела "заметки"\n>> ')

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
                    sorted_note_list(user)
                elif inp == '7':
                    break

        elif inp == '2':
            while True:
                inp = input('\n1. создать новый аккаунт\n2. показать список доступных пользователей' + 
                '\n3. сменить аккаунт\n4. изменить имя текущего аккаунта\n5. удалить текущий аккаунт\n6. установить/сменить пароль\n' + 
                '7. удалить пароль\n8. выйти из раздела "аккаунт"\n>> ')

                indent()
                if inp == '1':
                    create_user()
                elif inp == '2':
                    list_of_users()
                elif inp == '3':
                    user = change_user(user)
                elif inp == '4':
                    user = configure_user(user)
                elif inp == '5':
                    delete_user(user)
                    active_user = False
                    break
                elif inp == '6':
                    create_password(user)
                elif inp == '7':
                    delete_password(user)
                elif inp == '8':
                    break

        elif inp == '3':
            end = True
            break