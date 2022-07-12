def main():
    print("main function executed")


if __name__ == "__main__":
    main()


def calculate(a, b):
    return a + b


result1 = calculate(1, -10)
result2 = calculate('Hello, ', 'Bob!')
print(result1)
print(result2)


# None result
def send_data():
    print('Data was sent!')
    return None


result = send_data()
print(result)


# empty return
def empty_func(a, b): return a + b


print(empty_func(1, 2))


# 4 returns + rec
def fibb(arg):
    if arg < 0:
        print('arg < 0')
        return

    elif arg == 0:
        return 0

    elif arg == 1:
        return 1

    else:
        return fibb(arg - 1) + fibb(arg - 2)

    print('Hello')


print(fibb(-1))
print(fibb(0))
print(fibb(1))
print(fibb(10))


def say_hello(name):
    print(f'Hello {name}')


# function as an arg
def say_hey(func):
    name = calculate('Jo', 'Jo')
    func(name)


say_hey(say_hello)

# function is also an object
methods_for_function = dir(say_hello)
print(methods_for_function)
var = say_hello.__name__
print(var)

# variable for function
get_hello_str = say_hello
get_hello_str('Dante')


def external_func(arg1):
    data = arg1 + 101

    def internal_func(arg2):
        return arg2 * data

    return internal_func


result1_func = external_func(2)
print(result1_func)
print(result1_func(3))
