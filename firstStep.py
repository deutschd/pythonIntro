import string
print("Hello World!")
print("This code gives a number in square:")
# num = float(input('Enter another number: '))
# if num > 0:
#     print(num, 'is positive')
#     print(num, 'square is', num*num)
isPositive = 12
isNegative = -12

print("Python Strings\n")
# z = """
# Hello
#         World
# """
# print(z)
#
# a = True
# b = 43
# c = 'Hello'
# d = 32.2
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#
# string_1 = 'Good'
# string_2 = " day"
# string_3 = string_1 + string_2
# print(string_3)
# print('Hello' + ' World')
# print(len(string_3))
#
# my_string = "Hello World"
# print(my_string[:5])
# print(my_string*2)
print('Splitting Strings\n')
# title = 'The Good, The Bad, and the Ugly'
# print('Source string:', title)
# print('Split using a space')
# print(title.split(' '))
# print('Split using a comma')
# print(title.split(','))
print('Counting Strings\n')
# my_string = 'Count, the number of spaces'
# print("my_string.count(' '):", my_string.count(' '))
print('Finding Sub Strings\n')
# find_string = 'Edward Alun Rawlings'
# print(find_string.find('A'))
print("Operations with String\n")
# some_string = 'Hello World'
# print('Testing a String')
# print('-' * 20)
# print('some_string', some_string)
# print("some_string.startswith('H')",
#       some_string.startswith('H'))
# print("some_string.endswith('h')",
#       some_string.endswith('h'))
# print('some_string.istitle()', some_string.istitle())
# print('some_string.isupper()', some_string.isupper())
# print('some_string.islower()', some_string.islower())
# print('some_string.isalpha()', some_string.isalpha())
#
print('String conversions\n')
# print('-' * 20)
# print('some_string.upper()', some_string.upper())
# print('some_string.lower()', some_string.lower())
# print('some_string.swapcase()', some_string.swapcase())
# print('String leading, trailing spaces', "  xyz   ".strip())
print("String Formatting\n")
# format_string = 'Hello {}!'
# print(format_string.format('Phoebe'))
# # Allows multiple values to populate the string
# name = "Adam"
# age = 20
# print("{} is {} years old".format(name, age))
# # Can specify an index for the substitution
# format_string = "Hello {1} {0}, you fot {2}%"
# print(format_string.format('Smith', 'Carol', 75))
# # Can use named substitutions, order is not significant
# format_string = "{artist} sang {song} in {year}"
# print(format_string.format(artist='Paloma Faith',
#                            song='"Guilty"', year=2017))
#
# print('|{:25}|'.format('25 characters width'))
# print('|{:<25}|'.format('left aligned'))
# print('|{:>25}|'.format('right aligned'))
# print('|{:^25}|'.format('centered'))
# # Can format numbers with comma as thousands separator
# print('{:,}'.format(1234567890.0))
print("String Templates and a pinch of dict()\n")
# template = string.Template('$artist sang $song in $year')
# print(template.substitute(artist='Ed Sheeran', song='Galway Girl', year=2017))

# d = dict(artist='Billy Idol', song='Eyes Without a Face', year=1984)
# print(template.substitute(d))

print("-"*20 + " Ex:(character_replace) and check if there is a word 'Albus'")
# # EXERCISE 1
# character_replace = "Denyse,Marie,Smith,21,London,UK"
# print(character_replace.replace(',', ' '))
# print("We will concatenate your two words-sentences:")
# first_input = input("First word/sentence: ")
# second_input = input("Second word/sentence: ")
# new_string = first_input + ' ' + second_input
# print(new_string)
# print(str(len(new_string)) + ' symbols in give examples')
# print(new_string.upper())
# print(new_string.find('Albus'))
#
# character_replace = "Try, Your, <BEST>"
# print(character_replace.replace('<','').replace('>',''))
print("-"*20 + " Ex:(Kilometres to Miles)")
# #  Convert Kilometres to Miles
# kms_to_miles = int(input('Kilometre(s): '))
# converter = kms_to_miles*0.6214
# print("There are " + str(converter) +" miles in " + str(kms_to_miles) + " kilometre(s)")

print("Flow of Control Using If Statements\n")
# num = int(input("Enter a number:"))
# if num > 0:
#     print(num, "is positive")
#     print(num, 'square is', num*num)
# elif num == 0:
#     print(num, "is zero")
# else:
#     print(num, "is negative")
#
# savings = float(input("Enter how much you have in savings: "))
# if savings == 0:
#     print("Sorry no savings")
# elif savings < 0:
#     print("What the ...?")
# elif savings < 500:
#     print("Well done!")
# elif savings < 1000:
#     print("That's a tidy sum")
# elif savings < 10000:
#     print("Welcome sir!")
# else:
#     print("Thank you!")
print("Nesting If Statements:\n")
# snowing = True
# temp = -1
# if temp < 0:
#     print("It's freezing")
#     if snowing:
#         print("Put on Boots")
#         print("Time for hot chocolate")
# print('Bye')
print("If Expressions:\n")
# age = 15
# status = None
# if age > 12 and age <30:
#     status = "teenager"
# else:
#     status = "not teenager"
# print(status)
#
# status = ('teenager' if age > 12 and age < 30 else 'not teenager')
# print(status)

print("*"*20 + " Ex: Test if a Number Is Odd or Even")
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#     print(True)
# else:
#     print(False)
print("*"*20 + " Ex: (Modified) Kilometres to Miles Converter")
# kms_to_miles = input("Enter a number: ")
# if kms_to_miles.isnumeric():
#     print("It's a number")
# else:
#     print("Please write a number, not text.")
# if int(kms_to_miles) > 0:
#     converter = int(kms_to_miles) * 0.6214
#     print("There are " + str(converter) +" miles in " + str(kms_to_miles) + " kilometre(s)")
# else:
#     print("You cannot enter a negative number.")


