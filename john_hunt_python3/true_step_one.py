print("Functions:")
#
#
# def print_my_msg(msg):
#     print(msg)
#
#
# print_my_msg('Hello World')
#
#
# def square(n):
#     n * n
#
#
# def swap(a, b):
#     return b, a
#
#
# print(swap(4, 3))
# a = 2
# b = 3
# x, y = swap(a, b)
# print(x, ',', y)
# z = swap(a, b)
# print(z)
print('\nMultiple Parameter Functions:')


def greeter(name, message):
    print('Welcome', name, message)


greeter('Eloise', 'Hope you like Rugby')
print('\nDefault Parameter Values:')


def greeter(name, message='Live Long and Prosper'):
    print('Welcome', name, '-', message)


greeter('Eloise')
greeter('Eloise', 'Hope you like Python')
print('\nNamed Arguments:')


def greeter(name,
            title='Dr',
            prompt='Welcome',
            message='Live Long and Prosper'):
    print(prompt, title, name, '-', message)


greeter(message='We like Python', name='Lloyd')
print("\nArbitrary Arguments:")


def greeter(*args):
    for name in args:
        print('Welcome', name)


greeter('John', 'Denise', 'Phoebe', 'Adam', 'Gryff')

print("\nPositional and Keyword Arguments:")


def my_function(*args, **kwargs):
    for arg in args:
        print('arg:', arg)
    for key in kwargs.keys():
        print('key:', key, 'has value: ', kwargs[key])


my_function('John', 'Denise', daughter='Phoebe', son='Adam')
print('-' * 50)
my_function('Paul', 'Fiona', son_number_one='Andrew',
            son_number_two='James', daughter='Joselyn')

print("\nDefine methods that only use of the *args && **kwargs")


def named(**kwargs):
    for key in kwargs.keys():
        print('arg:', key, 'has value:', kwargs[key])


named(a=1, b=2, c=3)

print("\nAnonymous Functions:")
number_doubled = lambda i: i * i
print(number_doubled(10))
func0 = lambda: print('no args')
func1 = lambda x: x * x
func2 = lambda x, y: x * y
func3 = lambda x, y, z: x + y + z

func0()
print(func1(4))
print(func2(3, 4))
print(func3(2, 3, 4))

print("\nScope and Lifetime of Variables")
max = 100


def print_max():
    global max
    max = max + 1
    print(max)


print_max()
print(max)

print("\nNonlocal Variables:")


def outer():
    title = 'original title'

    def inner():
        title = 'another title'
        print('inner:', title)

    inner()
    print('outer:', title)


outer()


def outer():
    title = 'original title'

    def inner():
        nonlocal title
        title = 'another title'
        print('inner:', title)

    inner()
    print('outer:', title)


outer()
