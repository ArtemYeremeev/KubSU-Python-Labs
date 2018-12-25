"""KubSU Python Lab№4"""
print('Exercise 1.')
from random import randint
# Вставить random в первую строку программы
n = int(input('Введите количество элементов в списка -'))
a = int(input('Левая граница интервала -'))
b = int(input('Правая граница интервала -'))
list1 = []
for i in range(n):
    random = randint(a, b)
    list1.append(random)
print(list1)

print('Exercise 2.')
list1 = []
for x in range(1, 26):
    list1.append(x)
list1.append(100)
list1.append(200)
print(list1)

print('Exercise 3.')
from random import randint
# Вставить random в первую строку программы
list1 = []
list2 = []
for x in range(10):
    a = randint(-30, 30)
    list1.append(a)
print(list1)
for x in range(len(list1)):
    if list1[x] < 0:
        list2.append(list1[x])
print(list2)

print('Exercise 4.')
from random import randint
# Вставить random в первую строку программы
k = int(input('Введите нежелательный индекс -'))
list1 = []
list2 = []
for x in range(10):
    a = randint(-30, 30)
    list1.append(a)
print(list1)
for x in range(len(list1)):
    if not x == k:
        list2.append(list1[x])
print(list2)

print('Exercise 5.')
list1 = []


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


t = 1
for x in range(10):
    a = fib(t)
    list1.append(a)
    t += 1
print(list1)

from random import randint
print('Exercise 6.')
# Вставить random в первую строку программы
row = 1
places = []
for x in range(25):
    for i in range(36):
        place = int(randint(0, 1))
        places.append(place)
    print(places)
    if row == 12:
        print('Места в 12 ряду распределены следующим образом - ', places)
        print('Число занятых мест -', sum(places))
    row += 1
    places.clear()

print('Exercise 7.')
from random import randint
# Вставить random в первую строку программы
print('5 курсов, 8 групп, от 15 до 30 студентов в каждой группе')
courses = []
course_count = 1
course = int(input('Какой курс вас интересует? - '))
print('На курсах следующее количество студентов (по группам):')
for x in range(5):
    groups = []
    for i in range(8):
        group1_8 = []
        group1_8 = int(randint(15, 31))
        groups.append(group1_8)
    courses.append(sum(groups))
    if course_count == course:
        print('На', course_count, 'курсе следующее количество студентов - ')
    print(groups)
    course_count += 1
courses.insert(course, sum(groups))
courses.pop()
print('Общее число студентов университета (по курсам) -', courses)

print('Exercise 8.')
from random import randint
# Вставить random в первую строку программы
print('12 курсов, 20 человек, зарплата от 20 до 60 тысяч')
year = []
count_chosen = []
for x in range(12):
    months = []
    for i in range(19):
        user1_19 = []
        user1_19 = int(randint(20, 61))
        months.append(user1_19)
    chosen = []
    chosen = int(randint(20, 61))
    months.append(chosen)
    count_chosen.append(chosen)
    year.append(sum(months))
dave = (input('Кто вас интересует? - '))
print(dave, 'заработал за год следующие суммы (по месяцам) - ', count_chosen)
print('Фонд ЗП за год (по месяцам) - ', year)

print('Exercise 9.')
from random import randint
# Вставить random в первую строку программы
print('18 вагонов, 36 мест')
train = []
for x in range(18):
    carriages = []
    for i in range(36):
        place1_36 = []
        place1_36 = int(randint(0, 1))
        carriages.append(place1_36)
    print(carriages)
    train.append(sum(carriages))
carriage = int(input('Какой вагон вас интересует? - '))
train.insert(carriage - 1, sum(carriages))
train.pop()
print('В выбранном вами поезде имеется следующее число свободных мест (по вагонам) -', train)
print('В выбранном вами вагоне следующее число свободных мест -', sum(carriages))
print('Общее число свободных мест в поезде -', sum(train))

print('Exercise 10.')
from random import randint
# Вставить random в первую строку программы
print('10 магазинов, 12 месяцев, доход от 10 до 30 тысяч')
shop_net = []
for x in range(10):
    shops = []
    for i in range(12):
        month1_12 = []
        month1_12 = int(randint(10, 31))
        shops.append(month1_12)
    print(shops)
    shop_net.append(sum(shops))
print('Общий доход сети магазинов (по каждому магазину) -', shop_net)
shop_net_monthly = []
for i in range(len(shop_net)):
    a = shop_net[i]/12
    shop_net_monthly.append(a)
print('Среднемесячные доходы магазинов -', shop_net_monthly)

print('Exercise 11.')
from random import randint
# Вставить random в первую строку программы
print('18 сотрудников, 12 месяцев, доход от 20 до 60 тысяч')
year = []
for x in range(12):
    months = []
    for i in range(18):
        user1_18 = []
        user1_18 = int(randint(20, 61))
        months.append(user1_18)
    print(months)
    year.append(sum(months))
print('Фонд ЗП за год (по месяцам)', year)
print('Годовой размер фонда ЗП -', sum(year))

print('Exercise 12.')
from random import randint
# Вставить random в первую строку программы
print('3 экзамена, 3 группы, 20 человек в каждой')
exams = []
for x in range(3):
    exam1_3 = []
    print('Экзамен', x + 1)
    for i in range(3):
        group1_3 = []
        for n in range(20):
            student1_20 = []
            student1_20 = int(randint(2, 5))
            group1_3.append(student1_20)
        print(group1_3)
        average_groups = (sum(group1_3) / 20)
        group1_3 = average_groups
        exam1_3.append(group1_3)
    average_exams = (sum(exam1_3)/3)
    exam1_3 = average_groups
    exams.append(exam1_3)
print('Средняя оценка каждой группы -', exams)


