
def change(temp):
    n = str(input('Введите ФИО и старый номер телефона которые хотите поменять: '))
    x = str(input('Введите полностью актуальные данные (ФИО и номер): \n'))
    new_list = ''
    for i in temp:
        if i == n:
            new_list = new_list + x + ','
        else:
            new_list = new_list + i + ','
    new_list = list(new_list.split(','))
    new_list.pop(-1)
    print(new_list)
    return new_list


def delete(temp):
    n = str(input('Введите ФИО и старый номер телефона которые хотите удалить: '))
    for i in temp:
        if i == n:
            index = temp.index(n)
            temp.pop(index)
    return temp
    
    

def add(temp):

     print('Введите ФИО и номер который хотите добавить в справиочник')
     n = str(input('Ввод:\n'))
     temp.append(n)
     return temp
    



def print_info(temp):
    print(temp)
    str1 = ''
    for i in temp:
            str1 = str1 + (i+ '\n')
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
        
    
def write(data):
    with open('numbers.txt', 'w') as file:
        for i in data:
            print(i)
            file.write(i + '\n')
    


def menu():
    data = read_file()
    print(data)
    while True:
        print('Выберите действие')
        print('5 - Перезаписать справочник')
        print('4 - добавить данные')
        print('3 - удалить данные')
        print('2 - заменить номер телефона, фамилии, и тд')
        print('1 - ввыести инфо на экран')
        print('0 выход из программы')
        n = int(input('Введите ваш выбор: \n'))

        if n == 0:
            break
        elif n == 1:
            print_info(data)
        elif n == 2:
            data = change(data)
        elif n == 3:
            data = delete(data)
        elif n == 4:
            data = add(data)
        elif n == 5:
            write(data)


if __name__ == '__main__':
    menu()


# my_st = "Я\nучу; язык,программирования\nPython"
# print(re.split(";|,|\n", my_st))
# data = list(map(int, data.split ()))