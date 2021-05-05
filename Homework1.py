# задание № 1

#name = input('Введите имя: ')
#age = input('Введите возраст: ')
#city = input('Введите город в котором вы живете: ')
#print('Здравствуйте,', name, '!', 'Вам', age, 'лет.', 'Вы из города', city, '.' )

# задание № 2

#ask_time = int(input('Введи время в секундах: '))
#hour = ask_time // 3600
#minute = ask_time % 3600 // 60
#second = ask_time % 3600 % 60

#print(f"{ask_time} секунд в формате ЧЧ:ММ:СС это {hour}:{minute}:{second}")

# задание № 3

#count = input('Введите число: ')
#result = int(count) + int(count + count) + int(count + count + count)
#print(result)

# задание № 4

print('{}'.format(['el_1', 'el_2', 'el_3', 'el_4']))

figure = int(input('Введите целое положительное число: '))



   # print(int(input('Введите число с большим количеством знаков: ')))

# задание № 5

#revenue = int(input('Введите сумму выручки: '))
#cost = int(input('Введите сумму издержек: '))
#profitability = revenue / cost

#while True:
#    if revenue > cost:
#        print('Поздравляем, у Вас прибыль в размере', revenue - cost)
#        print('Рентабельность -', "%.2f" % (profitability))
#        employee = int(input('Введите количество сотрудников: '))
#        profit = profitability / employee
#        print('Прибыль на душу -', "%.2f" % (profit))
#        break
#    elif revenue < cost:
#        print('К сожалению Вы в убытке на', cost - revenue)
#        break
#    else:
#        print('Вы вышли в 0')
#        break

# задание № 6

#start_distance = int(input('Введите стартовый километраж: '))
#purpose_distance = int(input('Введите цель в километрах: '))
#day = 1

#while start_distance <= purpose_distance:
#    start_distance += start_distance * 0.1
#    day += 1

#print(f'на {day}-й день Вы достигнете результата — не менее {purpose_distance} км.')
