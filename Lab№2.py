"""KubSU Python Lab№2"""
print('Exercise 1.')
b = int(input('Введите число b (больше 10) - '))
t = 10
while t != b:
    print(t ** 3)
    t += 1
print(b ** 3)

print('Exercise 2.')
a = 1
b = 0.453
for t in range(10):
    print(a, 'фунт(а, ов) = ', b, 'кг')
    a += 1
    b += 0.453

print('Exercise 3.')
# Option 1
a = 10
for x in range(90):
    if a % 2 == 0:
        pass
    else:
        print(a)
    a += 1

# Option 2
a = 11
while a <= 100:
    print(a)
    a += 2

print('Exercise 4.')
x = int(input('Для какого числа нужна таблица умножения? - '))
a = 0
for n in range(10):
    print(x, ' * ', a, ' = ', x * a)
    a += 1

from random import randint
# Для отдельного документа вставить импорт random в первую строку
print('Exercise 5.')
numbers = []
for x in range(10):
    a = randint(0, 100)
    numbers.append(a)
print(numbers)
print('Сумма составляет - ', sum(numbers))

from random import randint
# Для отдельного документа вставить импорт random в первую строку
print('Exercise 6.')
n = int(input('Сколько учеников в каждом классе? - '))
a = []
b = []
for x1 in range(n):
    y1 = randint(2, 5)
    a.append(y1)
for x2 in range(n):
    y2 = randint(2, 5)
    b.append(y2)
print(a)
print(b)
r1 = sum(a) // n
r2 = sum(b) // n
print(r1)
print(r2)

print('Exercise 7.')
n = int(input('Срок вклада составляет - '))
P = 1000
summi = []
for x1 in range(n):
    P = P * 1.02
    summi.append(P)
print('Суммы вкладов по месяцам - ', summi)
prirosti = []
t1 = 0
t2 = 1
while t2 != n:
    prirost = summi[t2] - summi[t1]
    prirosti.append(prirost)
    t1 += 1
    t2 += 1
print('Приросты по месяцам - ', prirosti)

from random import randint
# Для отдельного документа вставить импорт random в первую строку
print('Exercise 8.')
april = []
nights = []
for t in range(30):
    night = randint(-30, 30)
    if night < 0:
        nights.append(night)
    april.append(night)
print('Температуры в апреле -', april)
print('Ночи с температурой ниже 0 -', nights)
print('Число ночей с температурой ниже 0 -', len(nights))

from random import randint
# Для отдельного документа вставить импорт random в первую строку
print('Exercise 9.')
count = 0
for n in range(20):
    a = randint(1, 9)
    b = randint(1, 9)
    question = a * b
    print('Сколько будет', a, '*', b, '?')
    answer = int(input())
    if answer == question:
        print('Верно!')
        count += 1
    else:
        print('Ошибка!')
print(count)

print('Exercise 10.')
chislo = int(input('Ваше число - '))
a = []
for x in range(10):
    if chislo > 0:
        cifra = chislo % 10
        a.append(cifra)
        chislo = chislo // 10
a.reverse()
maximum = max(a)
print('Ваше число состоит из цифр - ', a)
print('Наибольшая из этих цифр -', max(a))
print('Место этой цифры в вашем числе -', a.index(maximum) + 1)
