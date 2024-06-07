from data_create import name_data, phone_data, surname_data, address_data


def write_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"%s" %name + " " + surname + " в каком формате вы хотите записать данные? \n\n 1 Вариант:" f"\n{name} \n{surname}\n{phone}\n{address} \n\n 2 Вариант: {name}; {surname}; {phone}; {address} \n\n Выберите вариант: "))
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
    pass

write_data()