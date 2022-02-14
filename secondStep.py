import random

print('1234 -> [1, 2, 3, 4]')
# a=list(map(int, input('\n')))
# print(a)
print("Iteration/Looping\n")
print("While Loop\n")
# count = 0
# print('Starting...')
# while count < 11:
#     print(count, ' ', end='')
#     count += 1
# print('\nDone')
print("For Loop\t(+increment by 2) (+anonymous loop)\n")
# print('Print out values in a range')
# for i in range(0, 11):
#     print(i, ' ', end='')
# print('\nDone')
#
# # Now use values in a range but increment by 2
# print('Print out values in a range with an increment of 2')
# for i in range(0, 11, 2):
#     print(i, ' ', end='')
# print('\nDone')

# anonymous' loop variable
# for _ in range(0,10):
#     print('.', end='')
# print()
print("Break Loop Statement\n")
# print('Only print code if all iterations completed')
# num = int(input('Enter a number to check for: '))
# for i in range(0, num+1):
#     if i == num+2:
#         break
#     print(i, ' ', end='')
# print('\nDone')
print('Continue Loop Statement\n')
# for i in range(0, 10):
#     print(i, ' ', end='')
#     if i % 2 == 1:
#         continue
#     print("hey it's an even number, \nwe love even numbers")
#
print("For Loop with Else\n")
# print('Only print code if all iterations completed')
# num = int(input('Enter a number to check for: '))
# for i in range(0, 10):
#     if i == num:
#         break
#     print(i, ' ', end='')
# else:
#     print('\nAll iterations successful')
print("False if any value of keys is nothing\n")
# List = {1: [], 2: [], 3: []}
# print(any(List.values()))
print("Dice Roll Game\n")
# MIN = 1
# MAX = 6
#
# roll_again = "y"
#
# while roll_again == "y":
#     print("Rolling the dices...")
#     print("The values are....")
#     dice1 = random.randint(MIN, MAX)
#     print(dice1)
#     dice2 = random.randint(MIN, MAX)
#     print(dice2)
#     roll_again = input('Roll the dices again? (y/n): ')
print("*" * 20 + " Ex: Calculate the Factorial of a Number: ")
#
# def factorial(n):
#     num = 1
#     while n >= 1:
#         num = num * n
#         n = n - 1
#     return num
# f = factorial(5)
# print(f)
#
# num = int(input('Enter a number to check for: '))
# fac = 1
# for i in range(1, num + 1):
#     fac = fac * i
# print("factorial of ", num, " is ", fac)
#
#
# num = int(input("enter a number: "))
#
# fac = 1
# i = 1
#
# while i <= num:
#     fac = fac * i
# i = i + 1
#
# print("factorial of ", num, " is ", fac)
a = [1, 2, 3] * 5
print(a)
while 3 in a:
    a.remove(3)
print(a)
s = 'privet'
while len(s) > 0:
    print(s[0], s[1:])
    s = s[1:]
s = 'dasda":XA*#@suh3wuhHDSAYDA32'
while len(s) > 0:
    bukva = s[0]
    if 'a' <= bukva <= 'z':
        print(bukva, 'small')
    elif 'A' <= bukva <= 'Z':
        print(bukva, 'big')
    elif bukva.isdigit():
        print(bukva, 'digit')
    else:
        print('characte')
    s = s[1:]
