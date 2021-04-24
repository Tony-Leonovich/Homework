# Задание №1

def calc (a, b):
    while True:
        if b == 0:
            print('На ноль делить нельзя!!!')
            b = int(input('Введите второе число, отличное от нуля: '))
        else:
            print(float(a / b))
            break

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
calc(num1, num2)

# Задание №2

user_info = lambda **kwargs: kwargs

info = user_info(
    name = input('Введите имя - '),
    surname = input('Введите фамилию - '),
    year_of_birth = input('Введите дату рождения - '),
    city = input('Введите место рождения - '),
    mail = input('Введите адрес электронной почты - '),
    phone = input('Введите телефон - ')
)

print(f"Имя - {info['name']} {info['surname']}, дата рождения {info['year_of_birth']}, место рождения - {info['city']}, почта - {info['mail']}, телефон - {info['phone']}")

# Задание № 3

def my_func(a, b, c):
    nums = []
    nums.append(a)
    nums.append(b)
    nums.append(c)
    nums.remove(min(nums))
    sum(nums)
    print(sum(nums))

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))

my_func(num1, num2, num3)

# Задание № 4

def my_func(x, y):
    print(x**y)

def my_func2(x, y):
    degree = 1
    result = x
    while degree < abs(y):
        result = result * x
        degree += 1
    print(1 / result)

num1 = int(input('Введите число: '))
num2 = int(input('Введите целое отрицательное число: '))

my_func(num1, num2)
my_func2(num1, num2)

# Задание № 5 - не знаю как сделать

nums = []
while True:
    input_str = input('Введите числа через пробел - ')
    input_str = input_str.split()
    for i in input_str:
        i = int(i)
        nums.append(i)
    print(sum(nums))

# Задание № 6

some_text = input('Введите какой-нибудь текст на латинице: ')

def int_func(*args):
    print(some_text.capitalize())
    print(some_text.title())

int_func(some_text)


