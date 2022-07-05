class Five:
    value = 5

    def print_value(self):
        print(self.value)


class Person:

    def __init__(self, name, age, salary, friends):
        self.name = name
        self._age = age
        self.__salary = salary
        self.__friends__ = friends

    def print_info(self):
        print(self.name)
        print(self._age)
        print(self.__salary)
        print(self.__friends__)


alice = Person (
    'Alice Doe',
    age=42,
    salary=500,
    friends=None,
)


class Ancestor:
    def __init__(self):
        print("Ancestor.__init__")

    def fun(self):
        print("Ancestor.fun")

    def work(self):
        print("Ancestor.work")

print(type(type))

print(1.0 + True)
