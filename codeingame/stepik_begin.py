print(11111 * 1111111)
print(2014 ** 14)
print(1.2345e-3)
print(2014.0 ** 14)
print(-7 // 3)
number_1 = 2.9
print(int(number_1))
number_2 = -1.6
print(int(number_2))
number_3 = 9 ** 19 - int(float(9 ** 19))
print(number_3)


def foo():
    a = 1
    print(a)


x = foo()
print('x = foo() =>  ' + str(type(x)))

a = 3
a += 4
print(a)

print('Show your name:\n')
# name = input('Enter your name: ')
# print('Hello', name, '!')
print('Minutes to hours + minutes\n')
# minutes = int(input())
# print(int(minutes/60))
# print(minutes%60)
print('timer\n')
# X = int(input())  # minutes to sleep
# H = int(input())  # 0.00a.m + H(hours) exact time begins here
# M = int(input())  # 0.00a.m + M(minutes)
# hours_to_sleep = (X+M)//60 + H
# minutes_to_sleep = (X+M)%60
# print(hours_to_sleep)
# print(minutes_to_sleep)
print('Logical operations\n')
# a = int(input())
# print(a>0)
# print(10 <= a < 100)  # print(a == 10 and a < 100)
#
# x1, x2, x3 = False, True, False
# print((not x1 or x2) and x3)
# a, b = True, False
# print((a and b) or ((not a) and (not b)))
#
# x = 5
# y = 10
# print(y > x * x or y >= 2 * x and x < y)  # 10>25 or 10>=10 and 5<10
#
# a = True
# b = False
# print(a and b or not a and not b)
print('Python Conditions and If statements\n')
# x = int(input())
# if x % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# a = int(input())
# b = int(input())
# if b != 0:
#     print(a/b)
# else:
#     print('Division by zero == error')
#     b = int(input('Please type another number: '))
#     if b == 0:
#         print('Okay, It is wrong...')
#     else:
#         print(a/b)
print('timer upgrade - health identification-normal-oversleeping\n')
# A = int(input())  # healthy sleeping time (h)
# B = int(input())  # don't need to sleep over this time (h)
# H = int(input())  # now he/she is sleeping
#
# if A <= H <= B:
#     print('Это нормально')
# elif H < A:
#     print('Недосып')
# elif H > B:
#     print('Пересып')
print('leap year or not\n')
year = int(input())
if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print('Високосный')
else:
    print('Обычный')