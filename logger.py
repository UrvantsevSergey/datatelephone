#from data_create import name_data, phone_data, surname_data, address_data
from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каои формате записать данные \n\n"
    f"1 Вариант: \n" 
    f"{name}/n{surname}/n{phone}/n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")    
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_var.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
        
        
    elif var == 2:
        with open('data_sec_var.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")
    

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_var.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list)) 
        
    print('Вывожу данные из 2 файла: \n')
    with open('data_sec_var.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
        

# ДОМАШНЕЕ ЗАДАНИЕ 
def copy_data():
    # Выбираем с каким справочником работаем
    s = int(input("Выберите справочник: \n 1 - 1 справочник \n 2 - 2 справочник \n"))
    while s != 1 and s != 2:
        print("Неправильный ввод")
        s = int(input("Выберите справочник: \n 1 - 1 справочник \n 2 - 2 справочник \n"))
    if s == 1:
        # Выводим пронумерованные данные из 1 файла
        print('Вывожу данные из 1 файла: \n')
        with open('data_first_var.csv', 'r+', encoding='utf-8') as f:
            data_first = f.readlines()
            for i, line in enumerate((data_first)):
                print(f'{i+1} {line.strip()}')
        # Проверка на наличие данных по номеру строки
            n = int(input("Выберите номер строки для копирования: "))
            while n < 0 or n > len(data_first):
                print("Неправильный ввод")
                n = int(input("Выберите номер строки для копирования: "))
        # Записываем строку в переменную r
            for i, line in enumerate(data_first):
                if i+1 == n:
                    r = line.strip()
                    print(r)

        # Записываем новые данные в файл
        with open('data_sec_var.csv', 'r+', encoding='utf-8') as f:
            data_sec = f.readlines()
            n_sec = len(data_sec)
            for i, line in enumerate(data_sec):
                if i+1 == n_sec:
                    f.write(r)
                    f.write('\n\n')
                    print("Данные скопированы\n")
    if s == 2:
        # Выводим пронумерованные данные из 1 файла
        print('Вывожу данные из 2 файла: \n')
        with open('data_sec_var.csv', 'r+', encoding='utf-8') as f:
            data_first = f.readlines()
            for i, line in enumerate((data_first)):
                print(f'{i+1} {line.strip()}')
        # Проверка на наличие данных по номеру строки
            n = int(input("Выберите номер строки для копирования: "))
            while n < 0 or n > len(data_first):
                print("Неправильный ввод")
                n = int(input("Выберите номер строки для копирования: "))
        # Записываем строку в переменную r
            for i, line in enumerate(data_first):
                if i+1 == n:
                    r = line.strip()
                    print(r)

        # Записываем новые данные в файл
        with open('data_first_var.csv', 'r+', encoding='utf-8') as f:
            data_sec = f.readlines()
            n_sec = len(data_sec)
            for i, line in enumerate(data_sec):
                if i+1 == n_sec:
                    f.write(r)
                    f.write('\n\n')
                    print("Данные скопированы\n")



def delete_data():
    # Выбираем с каким справочников работаем
    s = int(input("Выберите справочник: \n 1 - 1 справочник \n 2 - 2 справочник \n"))
    while s != 1 and s != 2:
        print("Неправильный ввод")
        s = int(input("Выберите справочник: \n 1 - 1 справочник \n 2 - 2 справочник \n"))
    if s == 1:
    # Выводим пронумерованные данные из 1 файла
        print('Вывожу данные из 1 файла: \n')
        with open('data_first_var.csv', 'r+', encoding='utf-8') as f:
            data_first = f.readlines()
            for i, line in enumerate((data_first)):
                print(f'{i+1} {line.strip()}')
    # Проверка на наличие данных по номеру строки
            n = int(input("Выберите номер строки для удаления: "))
            while n < 0 or n > len(data_first):
                print("Неправильный ввод")
                n = int(input("Выберите номер строки для удаления: "))
    # Удаляем строку
        with open("data_first_var.csv", "w", encoding="utf-8") as f:
            for i, line in enumerate(data_first):
                if i+1 != n:
                    f.write(line)
        print("Строка удалена!\n")
    if s == 2:
    # Выводим пронумерованные данные из 2 файла
        print('Вывожу данные из 2 файла: \n')
        with open('data_sec_var.csv', 'r+', encoding='utf-8') as f:
            data_first = f.readlines()
            for i, line in enumerate((data_first)):
                print(f'{i+1} {line.strip()}')
    # Проверка на наличие данных по номеру строки
            n = int(input("Выберите номер строки для удаления: "))
            while n < 0 or n > len(data_first):
                print("Неправильный ввод")
                n = int(input("Выберите номер строки для удаления: "))
    # Удаляем строку
        with open("data_sec_var.csv", "w", encoding="utf-8") as f:
            for i, line in enumerate(data_first):
                if i+1 != n:
                    f.write(line)
        print("Строка удалена!\n")

def rename_data():
    # Выбираем с каким справочником работаем
    s = int(input("Выберите справочник: \n 1 - 1 справочник \n 2 - 2 справочник \n"))
    while s != 1 and s != 2:
        print("Неправильный ввод")
        s = int(input("Выберите справочник: \n 1 - 1 справочник \n 2 - 2 справочник \n"))

    if s == 1:
        # Выводим пронумерованные данные из файла
        print('Вывожу данные из 1 файла: \n')
        with open('data_first_var.csv', 'r+', encoding='utf-8') as f:
            data_first = f.readlines()
            for i, line in enumerate(data_first):
                print(f'{i+1} {line.strip()}')
        # Проверка на наличие данных по номеру строки
            n = int(input("Выберите номер строки для изменения: "))
            while n < 0 or n > len(data_first):
                print("Неправильный ввод")
                n = int(input("Выберите номер строки для изменения: "))
        # Вводим новые данные
            r = input("Введите новые данные: ")
        # Записываем новые данные в файл
        with open("data_first_var.csv", "w", encoding="utf-8") as f:
            for i, line in enumerate(data_first):
                if i+1 == n:
                    data_first[i] = r + '\n'
                    f.writelines(data_first)
        print("Данные изменены!\n")
    if s == 2:
        # Выводим пронумерованные данные из файла
        print('Вывожу данные из 2 файла: \n')
        with open('data_sec_var.csv', 'r+', encoding='utf-8') as f:
            data_first = f.readlines()
            for i, line in enumerate(data_first):
                print(f'{i+1} {line.strip()}')
        # Проверка на наличие данных по номеру строки
            n = int(input("Выберите номер строки для изменения: "))
            while n < 0 or n > len(data_first):
                print("Неправильный ввод")
                n = int(input("Выберите номер строки для изменения: "))
        # Вводим новые данные используя функции name_data, surname_data, phone_data, address_data
            print("Введите новые данные")
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            r = f"{name};{surname};{phone};{address}"
        # Записываем новые данные в файл
        with open("data_sec_var.csv", "w", encoding="utf-8") as f:
            for i, line in enumerate(data_first):
                if i+1 == n:
                    data_first[i] = r + '\n'
                    f.writelines(data_first)
        print("Данные изменены!\n")

                