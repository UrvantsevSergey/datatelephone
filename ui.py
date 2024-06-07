from logger import input_data, print_data


def interface():
    print("Добрый день! Добро пожаловать в бот справочник! \n Выберите команду: \n 1 - Записать данные \n 2 - Вывести данные")
    command = int(input("введите команду: "))
    while command != 1 and command != 2:
        print("Неправильная команда")
        command = int(input("введите команду: "))
    if command == 1:   
        input_data()
    elif command == 2:
        print_data()