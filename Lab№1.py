"""KubSU Python Lab№1"""
import math
print('Exercise 1.')
print('Hello, World!')

print('Exercise 2.')
a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))
c = a + b
print("Сумма чисел равна ", c)

print('Exercise 3.')
print('4 5 7')
print(4+5+7)
print(4*5*7)
print((4*5*7)/3)

print('Exercise 4.')
a = math.pi
print(round(a, 2))

print('Exercise 5.')
a = math.e
print(round(a, 1))

print('Exercise 6.')
a = int(input("Введите первый катет\n"))
b = int(input("Введите второй катет\n"))
c = ((a ** 2 + b ** 2) ** 0.5)
print(c)

print('Exercise 7.')
P = int(input("Введите сумму вклада\n"))
I = int(input("Введите процентную ставку\n"))
t = int(input("Число дней начисления\n"))
print(((P * I * t) / (365 * 100)) + P)

print('Exercise 8.')
a = int(input("Введите число\n"))
n = float(input("Введите степень\n"))
print(a ** n)

print('Exercise 9.')
age = int(input("Введите возраст"))
if age >= 25 and age <= 40:
    print("Подходит!")
else:
    print("Не подходит!")

print('Exercise 11.')
age = int(input("Введите возраст"))
a = [11, 12, 13, 14]
b = [2, 3, 4]
с = [0, 5, 6, 7, 8, 9]
if age in a:
    print(age, 'лет')
else:
    if age % 10 == 1 and age != 11:
        print(age, 'год')
    else:
        if age % 10 in b:
            print(age, 'года')
        else:
            if age % 10 in с:
                print(age, 'лет')

print('Exercise 12.')
v = float(input("Введите вещественное число"))
if v >= 0:
    print(v)
else:
    print(-v)

print('Exercise 13.')
a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))
c = int(input("Число третье число\n"))
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

print('Exercise 14.')
rainy = input("Что по погоде? Дождит? (да/нет)")
cold = input("Мерзнешь? (да/нет)")
if rainy == 'да' and cold == 'да':
    print("Надень ка лучше пальто, холодно и мокро")
elif rainy == 'да' and cold != 'да':
    print("Захвати с собой зонтик, а то промокнешь")
elif rainy != 'да' and cold == 'да':
    print("Надень пиждак, а то замерзнешь")
elif rainy != 'да' and cold != 'да':
    print("Можешь надеть что угодно, погода отличная")

print('Exercise 15.')
x = int(input("Введите значение х"))
if x < -1:
    print('y = ', -1)
if x == -1:
    print('y = ', x)
if x > -1:
    print('y = ', 1)

print('Exercise 16.')
x = float(input("Введите значение х"))
if x <= 0:
    print('y =', 0)
elif 0 < x <= 1:
    print('y =', x)
else:
    print('y =', x ** 2)

print('Exercise 17.')
x = float(input("Введите первое вещественное значение\n"))
y = float(input("Введите второе вещественное значение\n"))
print(max(x, y))

print('Exercise 18.')
x = float(input("Введите первое вещественное значение\n"))
y = float(input("Введите второе вещественное значение\n"))
z = float(input("Введите третье вещественное значение\n"))
print(max(x, y, z))

print('Exercise 19.')
t = int(input("Сколько минут прошло с начала часа?"))
a = [1, 2, 3, 6, 7, 8]
if t % 10 in a:
    print('Зеленый')
else:
    print('Красный')

print('Exercise 20.')
x = int(input("Введите шестизначное число"))
a1 = x % 10
x = x // 10
a2 = x % 10

x = x // 10
a3 = x % 10

x = x // 10
a4 = x % 10

x = x // 10
a5 = x % 10

x = x // 10
a6 = x % 10

if a1+a2+a3 == a4+a5+a6:
    print('Число счастливое')
else:
    print('Не повезло')

print('Exercise 21.')
t = int(input('Введите год'))
if t % 4 != 0 or (t % 100 == 0 and t % 400 != 0):
    print("Обычный год")
else:
    print("Високосный год")

print('Exercise 22.')
day = int(input('Введите день года'))
k = 365
year = list(range(1, k))
if day in year[::6] or day in year[::7]:
    print("Выходной!")
else:
    print("На работу!")