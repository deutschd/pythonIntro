import string

print('Hello World')

print('"Hello ", + user_name\n')
# user_name = input('Enter your name: ')
# print('Hello ', user_name)
# print(len(user_name))
# print(user_name[3])


print("Python Statements\n")
# city = "xyz"
# number_of_people_in_city = 123
# year = 1199
# print('The total population for',
#       city,
#       'was',
#       number_of_people_in_city,
#       'in',
#       year)
print("Splitting Strings - based on the character(method)\n")  # methods are applied with dot notation
# title = 'The Good, The Bad, and the Ugly'
# print('Source string', title)
# print(title.split())  # = print(title.split(' '))
# print(title.split('a'))
print("Counting Strings - how many times a string is repeated\n")
# my_string = 'Count, the number    of spaces'
# print("my_string.count(' '):", my_string.count(' '))
print("Replacing Strings - .replace(old, new)\n")
# welcome_message = 'Hello World!'
# print(welcome_message.replace("Hello", "Goodbye"))
print("Finding Sub Strings - string.find('A') -> where it starts\n")
# print('Edward Alun Rawlings'.find('2'))
# print('Hello this is a new way to start'.find('star'))
print("Other String Operations\n")
# text = 'hello World'
# print("Testing a string")
# print(text.startswith('H'))
# print(text.startswith('h'))
# print(text.endswith('d'))
# print(text.istitle())
# print(text.isupper())
# print(text.islower())
# print(text.isalpha())
#
# print("\nString conversions")
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.swapcase())
# print('String leading, trailing spaces', "       hel    ale   ".strip())

print("String Formatting\n")
# format_string = 'Hello {}!'
# print(format_string.format('Phoebe'))  # Hello Phoebe!
#
# name = "Adam"
# age = 20
# print("{} is {} years old".format(name, age))  # Adam is 20 y.o.
#
# format_string = "Hello {1} {0}, you got {2}%"
# print(format_string.format('Smith', 'Carol', 75))  # Hello Carol Smith, you got 75%
#
# format_string = "{artist} sang {song} in {year}"
# print(format_string.format(artist='Paloma Faith', song='Guilty', year=2022))
#
# print('|{:25}|'.format('left aligned'))  # :>right, :^centered :<ok
# print('|{:>25}|'.format('right aligned'))
# print('|{:^25}|'.format('centered'))
#
# print('{:,}'.format(12342132131321))
# print('{:,}'.format(1234567890.0))
print("String Templates\n")
# template = string.Template('$artist sang $song in $year')
# print(template.substitute(artist='Freddie Mercury',
#                           song='The Great Pretender', year=1987))
# print(template.substitute(artist='Ed Sheeran', song='Galway Girl', year=2017))
#
# d = dict(artist='Billy', song='Eyes Without a Face', year=1984)
# print(template.substitute(d))

print('Exercise 1\n')
# print('Denyse,Marie,Smith,21,London,UK'.replace(',', ' '))
# a = str(input('Write anything and it will be together, Let\'s the first one: '))
# b = str(input('Second one: '))
# new_string = a + ' ' + b
# print(new_string)
# print(len(new_string))
# print(new_string.upper())
# print(new_string.find('Albus'))


print("Numbers, Booleans and None\n")
# status = bool(input('well: '))  # check if there is something written or not True - False
# print(status)
# import decimal
# print(100/20)  # float 5.0
# print(3//2)  # int 1
print("Flow of Control Using If Statements\n")
# num = int(input('Enter a number: '))
# if num < 0:
#     print(num, 'is negative')
# elif num > 0:
#     print(num, 'is positive')
# elif num == 0:
#     print("ok, it's a zero")
# else:
#     print('pls, enter a number next time...')
print("The Use of elif\n")
# savings = float(input("Enter how much you have in savings: "))
# if savings == 0:
#     print("Sorry no savings")
# elif savings < 500:
#     print('Well done')
# elif savings < 1000:
#     print("That's a tidy sum")
# elif savings < 10000:
#     print('Welcome!')
# elif savings >= 10000:
#     print("That's a lot, good")
# else:
#     print('Thank you for response')
print("Nesting If Statements\n")
# snowing = True
# temp = -1
# if temp < 0:
#     print('It is freezing')
#     if snowing:
#         print('Put on boots')
#     print('Time for Hot Chocolat')
# print('Bye')
print("If Expressions\n")
# age = 15
# status = None
# if (age > 12) and age < 20:
#     status = 'teenager'
# else:
#     status = 'not teenager'
# print(status)
#
# status = ('teenager' if 12 < age < 20 else 'not teenager')
# print(status)

print("Exercise\n")
# num = int(input('Enter a number(integer): '))
# if num % 2 == 0:
#     print("It's the even number")
# else:
#     print("It's the odd number")


print("Iteration/Looping - while/for")
print("While Loop\n")
count = 0
print('Starting')
while count < 10:
    print(count, '- ', end='')
    count += 1
print('Done')
print("For Loop\n")
# for i in range(0, 10, 2):
#     print(i, '', end='')
# print('\nDone')
# for _ in range(0,10):
#     print('.', end='')
print("Break Loop Statement\n")
print('Only print code if all iterations completed')
# num = int(input('Enter a number to check for: '))
# for i in range(0, 6):
#     if i == num:
#         break
#     print(i, '', end='')
# print('Done')
print("Continue Loop Statement\n")
for i in range(0, 10):
    print(i, '', end='')
    if i % 2 == 1:
        continue
    print('hey its an even number')
    print('we love even numbers')
print('Done')
print("For Loop with Else\n")
# print('Only print code if all iterations completed')
# num = int(input('Enter a number to check for: '))
# for i in range(0, 6):
#     if i == num:
#         break
#     print(i, '', end='')
# else:
#     print('\nAll iterations successful')

print("Dice Roll Game\n")
# import random
# MIN = 1
# MAX = 6
#
# roll_again = 'y'
# while roll_again == 'y':
#     print('Rolling the dices...\nThe values are...')
#     dice1 = random.randint(MIN, MAX)
#     print(dice1)
#     dice2 = random.randint(MIN, MAX)
#     print(dice2)
#     roll_again = input('Roll the dices again? (y/n): ')

print("Exercise 1 - Calculate the Factorial of a Number\n")
# num = int(input('Enter a number: '))
# factorial = 1
# if num < 0:
#     print('Error, please enter positive integer...')
# if num == 0:
#     print(f'factorial of {num} is 1')
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)
#
#
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
#
# result = factorial(num)
# print("The factorial of", num, "is", result)

print("Exercise 2 - Print All the Prime Numbers in a Range\n")
start = int(input("Enter the lower bound: "))
stop = int(input("Enter the upper bound: "))

print("Prime numbers between", start, "and", stop, "are:")
for val in range(start, stop):
    if val < 1:
        print('more than 2 pls')
    if val > 1:
        for i in range(2, val):
            if (val % i) == 0:
                break
        else:
            print(val, end=' ')

