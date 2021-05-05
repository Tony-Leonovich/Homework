#Задание №1

data = ['hello', 123, 65.34, ('first', '2nd', 3)]
for item in data:
   print(type(item))

#Задание №2

my_list = []
lenght = int(input('Введите длину списка: '))
while len(my_list) < lenght:
   my_list.append(input('Введите что-нибудь: '))

print(my_list)

for i in my_list:
   i = int(i)
   while i < len(my_list):
       new_one = my_list.pop(i)
       my_list.insert((i - 1), new_one)
       i += 2
   break

print(my_list)

#Задание №3

ask_month = int(input('Введите номер месяца: '))

number_of_month = []
month = 0
while len(number_of_month) < 12:
   number_of_month.append(month + 1)
   month += 1

name_of_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
if ask_month in number_of_month:
   print('This is', name_of_month[number_of_month.index(ask_month)])

year = {}
count = 0
while count < len(number_of_month):
   year[number_of_month[count]] = name_of_month[count]
   count += 1

print('This is', year[ask_month])

if ask_month < 6 and ask_month > 2:
   print("And it's all spring")
elif ask_month < 9 and ask_month > 5:
   print("And it's all summer")
elif ask_month < 12 and ask_month >10:
   print("And it's all autumn")
else:
   print("And it's all winter")

#Задание №4

sentence = input('Введите простое предложение: ').split()

for order, word in enumerate(sentence, 1):
   print(order, word[:10])

#Задание №5

my_list = [55, 31, 22, 22, 9, 5]
new_one = int(input('Введите целое положительное число: '))

if new_one in my_list:
    position_index = my_list.index(new_one)
    new_position = my_list.count(new_one)
    my_list.insert((position_index + new_position), new_one)
elif new_one < (min(my_list)):
    my_list.insert((my_list.index(min(my_list)) + 1), new_one)
else:
    my_list.insert((my_list.index(max(my_list))), new_one)

print(my_list)

# Задание №6

storage = [
   (1, {"название": "", "цена": "", "количество": "", "единица": ""}),
   (2, {"название": "", "цена": "", "количество": "", "единица": ""}),
   (3, {"название": "", "цена": "", "количество": "", "единица": ""}),
]
position = 0
for i in storage:
    storage[position][1]["название"] = input('Введите название товара: ')
    storage[position][1]["цена"] = input('Введите стоимость товара: ')
    storage[position][1]["количество"] = input('Введите количество товара: ')
    storage[position][1]["единица"] = input('Введите единицу измерения товара: ')
    position += 1

for i in storage:
    print(i)

print('.' * 40)

analitic_dict = {}

for name in ((storage[0][1]).keys()):
    analitic_dict[name] = (((storage[0][1][name])), ((storage[1][1][name])), ((storage[2][1][name])))

for i in analitic_dict.items():
    print(i)