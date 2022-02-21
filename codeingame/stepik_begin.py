print(11111*1111111)
print(2014**14)
print(1.2345e-3)
print(2014.0**14)
print(-7//3)
number_1 = 2.9
print(int(number_1))
number_2 = -1.6
print(int(number_2))
number_3 = 9**19 - int(float(9**19))
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

X = int(input())  # minutes to sleep
H = int(input())  # 0.00a.m + H(hours) exact time begins here
M = int(input())  # 0.00a.m + M(minutes)
hours_to_sleep = (X+M)//60 + H
minutes_to_sleep = (X+M)%60
print(hours_to_sleep)
print(minutes_to_sleep)
