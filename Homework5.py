# Задание №1

with open('new_file.txt', 'a') as file:
    while True:
        user_answ = input('Write smth: ')
        file.write(user_answ + '\n')
        if not user_answ:
            break

# Задание №2


def count_info():
    try:
        with open('new_file.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                print(f'Количество строк в файле {len(my_list)}. В {i + 1}-ой строке {len(new_l)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'


count_info()

# Задание №3


def workers_statistics():
    workers = [['Сидоров ', '12000 \n'], ['Кукушкин ', '19000 \n'], ['Иванов ', '145000 \n'], ['Смирнов ', '80000']]
    try:
        with open('new_file.txt', 'r+', encoding="utf-8") as file:
            for i in range(len(workers)):
                file.writelines(workers[i])
            l = file.readlines()
            poor = []
            sum = 0
            for i in range(len(l)):
                salary = int((l[i].split())[1])
                if salary < 20000:
                    poor.append((l[i].split())[0])
                sum += salary
            print(f'Средняя величина дохода сотрудников равна {sum / len(workers) / 12:.2f}')
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(poor)}')
    except FileNotFoundError:
        return 'Файл не найден.'


workers_statistics()

# Задание №4


def rewrite_file():
    num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []
    try:
        with open('file.txt', 'r+', encoding="utf-8") as file:
            with open('new_file.txt', 'r+', encoding="utf-8") as new_file:
                l = file.readlines()
                for i in l:
                    i = i.split(' ', 1)
                    new_text.append(num[i[0]] + ' ' + i[1])
                new_file.writelines(new_text)
    except FileNotFoundError:
        return 'Файл не найден.'


rewrite_file()

# Задание №5


def rewrite_file():
    try:
        with open('filsse.txt', 'r+') as file:
            file.write(input('Введите числа через пробел: '))
            l = map(int, file.read().split())
            print(sum(l))
    except FileNotFoundError:
        return 'Файл не найден.'


rewrite_file()

# Задание №6


def count_subjects():
    try:
        # Информатика: 100(л) 50(пр) 20(лаб).
        mydict = {}
        with open("file.txt", encoding='utf-8') as fobj:
            for line in fobj:
                name, stats = line.split(':')  # name = Информатика, stats = 100(л) 50(пр) 20(лаб).
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                """1. [i for i in stats if i == ' ' or ('0' <= i <= '9')] - Перебирает все элементы и берет только цифры
                        и пробелы(для разделения цифр: [' ', '1', '0', '0', ' ', '5', '0', ' ', '2', '0'])
                 2. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]) с помощью join объединяет
                        получившееся: _100_50_20  (где _ это пробел)
                 3. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()
                        - делит по пробелам методом .split(): ['100', '50', '20']
                 4. map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split())
                        - с помощью map(int, ['100', '50', '20']) приводит все элементы списка к типу int
                 5. с помощью sum(['100', '50', '20']) суммирует все элементы списка """
                mydict[name] = name_sum
            print(f"{mydict}")  # вывод:{'Информатика': 170}
    except FileNotFoundError:
        return 'Файл не найден.'


count_subjects()

# Задание №7

import json


def get_statistics():
    try:
        with open('file.txt', 'r+', encoding='utf-8') as file:
            statistics = []
            profit = {}
            average_profit = {}
            av = 0
            prof = 0
            i = 3
            for line in file:
                name, firm, earning, damage = line.split()
                total = int(earning) - int(damage)
                if total >= 0:
                    prof = prof + total
                else:
                    i -= 1
                profit[name] = total
            statistics.append(profit)
            if i != 0:
                (av) = prof / i
                average_profit['average_profit'] = round(av)
                statistics.append(average_profit)
            else:
                print('Все компании работают в убыток')
            print(statistics)
        with open('file.json', 'a+', encoding='utf-8') as json_file:
            json.dump(statistics, json_file)
    except FileNotFoundError:
        return 'Файл не найден.'


get_statistics()