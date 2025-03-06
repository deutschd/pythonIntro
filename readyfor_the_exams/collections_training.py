a = {}
print(type(a))
a = []
print(type(a))

b = {1, 2, 3}
print(type(b))
b = [1, 2, 3]
print(type(b))

c = {'a': 1, "b": 2}
print(type(c))

my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(my_list)
print(my_dict)
print(len(my_list))
print(len(my_dict))
print(len('a b c'))

print('a' in my_list)
print('a' not in my_list)

print('a' in my_dict)
print('a' in my_dict.keys())
print('a' in my_dict.values())  # a is key not value
print(1 in my_dict.values())

print(('a', 1) in my_dict.items())
print('ab' in 'daskdahehwqewqehqwjg   ab dsa')

for elm in my_dict:
    print(elm)
for elm in my_dict.values():
    print(elm)

# key - value
for key, value in my_dict.items():
    print(key, value)

for elm in list(my_list):
    print(my_list)
print(max(my_list))
print(sum(my_dict.values()))

print("\nMethods. Examples:\n")
print(".count()")  # count elements for ordinary collections([]-list(), tuple(), string)
my_list = [1, 2, 3, 2, 3, 2, 3]
print(my_list.count(2))
print(".index()")
print(my_list.index(2))
print(".copy()")
my_set = {1, 2, 3}
my_set_2 = my_set.copy()
print(my_set_2 == my_set)
print(my_set_2)
print(my_set_2 is my_set)  # they have similar elements but they're not identical, different id's
print('.clear()')  # works on list, dict, set
my_set = {1, 2, 3}
print(my_set)  # {1, 2, 3, 4}
my_set.clear()
print(my_set)  # set()

# set_a.isdisjoint(set_b) - true if they don't have similar elements
# set_b.issubset(set_a) && set_a.issuperset(set_b)

my_keys = ('a', 'b', 'c')
my_values = [1, 2]
my_dict = dict(zip(my_keys, my_values))
print(my_dict)

my_tuple = ('a', 'b', 'a')
my_list = list(my_tuple)
my_set = set(my_tuple)
my_frozenset = frozenset(my_tuple)
print(my_list, my_set, my_frozenset)





