print('Simple calculator App')


def add(x, y):
    """ Add two numbers """
    return x + y


def subtract(x, y):
    """ Subtracts two numbers """
    return x - y


def multiply(x, y):
    """ Multiplies two numbers"""
    return x * y


def divide(x, y):
    """ Divides two numbers """
    return x / y


finished = False
while not finished:
    result = 0
    # Get the operation from the user
    # Get the numbers from the user
    # Select the operation
    print('Result:', result)
    print('==================')
    # Determine if the user has finished

print('Bye')

# def check_if_user_has_finished():
#     """
#     Checks that the user wants to finish or not.
#     Performs some verification of the input."""
#     ok_to_finish = True
#     user_input_accepted = False
#     while not user_input_accepted:
#         user_input = input('Do you want to finish (y/n): ')
#         if user_input == 'y':
#             user_input_accepted = True
#         elif user_input == 'n':
#             ok_to_finish = False
#             user_input_accepted = True
#         else:
#             print('Response must be (y/n), please try again')
#     return ok_to_finish
