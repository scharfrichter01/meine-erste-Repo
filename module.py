def get_line():
    s = list(input('Enter line: ').split())
    return (int(s[0]), s[1], s[2], int(s[3]), int(s[4]), int(s[5]))


def insert(line):
    if line not in data:
        data.append(line)


def print_data():
    m = max([len(i) for i in columns])
    for i in columns:
        print(str(i).ljust(m + 1, ' '), end='')
    print()
    for line in data:
        for i in line:
            print(str(i).ljust(m + 1, ' '), end='')
        print()


def ChangeLine():
    index = int(input('Enter number line: ')) - 1
    data[index] = tuple(input('Enter your changes: ').split())


def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write(','.join(columns) + '\n')
        for line in data:
            line = [str(i) for i in line]
            file.write(','.join(line) + '\n')


def read_from_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            if line != '\n':
                line = line.split(',')
                data.append((int(line[0]), line[1], line[2], int(line[3]), int(line[4]), int(line[5])))
    return columns, data


global data, columns

# columns = ('id', 'name', 'lastname', 'age', 'height', 'weight')
# data = [
#     (1, 'Ivan', 'Ivanov', 14, 160, 50),
#     (2, 'Sasha', 'Sidorov', 15, 210, 40),
#     (3, 'Masha', 'Poradina', 30, 178, 70),
#     (4, 'Timur', 'Korolev', 44, 160, 120)
# ]


columns, data = read_from_file('data.csv')

# Функции, использующиеся для программы RomeNumber

roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
romanBad = ['IV', 'IX', 'IL', 'IC', 'ID', 'IM']


# LLXIXV

# def IntFuerRoman(x):
#     ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
#     tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
#     hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
#     thous = ["", "M", "MM", "MMM", "MMMM"]
#
#     t = thous[x // 1000]
#     h = hunds[x // 100 % 10]
#     te = tens[x // 10 % 10]
#     o = ones[data % 10]
#
#     return t + h + te + o





def RomanFuerInt():
    x = input("Enter Roman Number: ")
    NormalNumber = 0
    RomanNumber = ''
    for i in x:
        RomanNumber += i
        for j in romanBad:
            if j in RomanNumber:
                NormalNumber -= 2
                break
        NormalNumber += int(roman[i])
    return NormalNumber



# z = input('enter number: ')
#
# print(RomanFuerInt(z))


# Ниже идут функции и переменные не имеющие отнощения к DataBase


def NumberCounter(x):
    count = 0
    for i in str(x):
        count += 1
    return count


def kleinerTaschenrechner():
    number1 = int(input('Enter number 1: '))
    number2 = int(input('Enter number 2: '))
    aktion = input('Aktion? \n"+ - * /"\n')
    if aktion == '+':
        print(number1 + number2)
        return number1 + number2
    elif aktion == '-':
        print(number1 + number2)
        return number1 - number2
    elif aktion == '*':
        print(number1 + number2)
        return number1 * number2
    elif aktion == '/':
        print(number1 + number2)
        return number1 / number2
    else:
        print('Only \n*\n/\n+\n-')
