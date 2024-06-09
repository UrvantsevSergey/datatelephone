from logger import input_data, print_data, rename_data, delete_data


def interface():
    print("Добрый день! Добро пожаловать в бот справочник! \n Выберите команду: \n 1 - Записать данные \n 2 - Вывести данные \n 3 - Изменить данные \n 4 - Удалить данные \n")
    command = int(input("введите команду: "))
    while command != 1 and command != 2 and command != 3 and command != 4:
        print("Неправильная команда")
        command = int(input("введите команду: "))
    if command == 1:   
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        rename_data()
    elif command == 4:
        delete_data()