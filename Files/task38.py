
def change(temp):
    print('Если вы хотите изменить свои данные на актуальные - введите 1')
    print('Если вы хотите удалить данные - введите 2')
    num = input('Ваш выбор')
    if num == 1:
        n = str(input('Введите ФИО и старый номер телефона которые хотите поменять: '))
        x = str(input('Введите полностью актуальные данные (ФИО и номер): '))
        new_list = ''
        for i in temp:
            if i == n:
                new_list = new_list + x
            else:
                new_list = new_list + i + ','
        new_list = list(new_list.split(','))
        print(new_list)
        return new_list
    elif num == 2:
        n = input('Введите ФИО и старый номер телефона которые хотите удалить: ')
        

        






def print_info(temp):
    print(temp)
    str1 = ''
    for i in temp:
            str1 = str1 +(i+ '\n')
    print(str1)
    


def read_file():
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        temp = file.readlines()
        str1 = ''
        for i in temp:
            str1 = str1 + i
        res_str = str1.replace(';', ' ')
        res_str = list(res_str.split('\n'))
        return res_str
        
    

def write_file():
    pass


def menu():
    data = read_file()
    print(data)
    while True:
        print('Выберите действие')
        print('2 - заменить номер телефона, фамилии, и тд')
        print('1 - ввыести инфо на экран')
        print('0 выход из программы')
        n = int(input('Введите ваш выбор: '))
        if n == 0:
            break
        elif n == 1:
            print_info(data)
        elif n == 2:
            data = change(data)
            


if __name__ == '__main__':
    menu()


# my_st = "Я\nучу; язык,программирования\nPython"
# print(re.split(";|,|\n", my_st))