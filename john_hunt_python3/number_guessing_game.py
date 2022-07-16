import random
import sys

print('Welcome to the Number Guessing Game')


def guess_number():
    number_to_guess = random.randint(1, 10)
    guess = int(input('Please guess a number between 1 and 10: '))
    count_number_of_tries = 1
    while number_to_guess != guess:
        print('Sorry wrong number')
        if count_number_of_tries == 4:
            break
        elif guess == -1:
            count_number_of_tries = count_number_of_tries - 1
            print('Your guess is', guess)
        elif guess == (number_to_guess - 1) or guess == (number_to_guess + 1):
            print('Your number is within 1')
        elif guess > number_to_guess:
            print('Your guess was higher than the number')
        else:
            print('Your guess was lower than the number')

        guess = int(input('Please guess again: '))
        count_number_of_tries += 1
    if number_to_guess == guess:
        print('Well done, you won!')
        print('You took', count_number_of_tries, 'goes to complete the game')
    else:
        print('Sorry you loose')
        print('The number you needed to guess was', guess)


guess_number()

play_again = input('Do you want to play again?(y/n): ')
if play_again == 'y':
    guess_number()

else:
    print('Game Over')
    sys.exit(0)
