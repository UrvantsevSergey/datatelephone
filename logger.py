from data_create import name_data, phone_data, surname_data, address_data


def write_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате вы хотите записать данные? \n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address} \n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address} \n\n"
    f"Выберите вариант: "))




    while var != 1 and var != 2:
        print("Неправильная команда")
        var = int(input("введите команду: "))

    if var == 1:
        with open("data_first_var.csv" ,"a", encoding = 'utf-8') as f:
            f.write(f"{name} \n{surname}\n{phone}\n{address} \n\n")
            f.close()

    elif var == 2:
        with open("data_second_var.csv", "a", encoding = 'utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {address} \n\n")
            f.close()

def read_data():
    print("Вывожу данные из первого файла: \n\n")
    with open("data_first_var.csv" ,"r", encoding = 'utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
                data_first_list.append("".join(data_first_list[j:i+1]))
                j = i
        print("".join(data_first_list))

    print("Вывожу данные из второго файла: \n\n")
    with open("data_sec_var.csv" ,"r", encoding = 'utf-8') as f:
        data_sec = f.readlines()
        print(*data_sec)