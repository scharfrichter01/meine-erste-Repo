
from module import *

global data, columns

"""

    Нужные нам формулы

    # columns, data = read_from_file('data.csv')
    # print(data)
    # insert(get_line())
    # print_data()
    # write_to_file('data.csv')
    # ChangeLine() 

"""

"""

    Это нам уже не нужно, выводить из под комментария только в случае обновления баззы данных

    # columns = ('id', 'name', 'lastname', 'age', 'height', 'weight')
    # data = [
    #     (1, 'Ivan', 'Ivanov', 14, 160, 50),
    #     (2, 'Sasha', 'Sidorov', 15, 210, 40),
    #     (3, 'Masha', 'Poradina', 30, 178, 70),
    #     (4, 'Timur', 'Korolev', 44, 160, 120)
    # ]

"""

print_data()

columns, data = read_from_file('data.csv')

# ChangeLine()

insert(get_line())

write_to_file('data.csv')

print_data()
