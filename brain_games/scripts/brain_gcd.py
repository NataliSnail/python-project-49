import random
import prompt
import math


def welcome_user():
    name = prompt.string('May I have your name? \n')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    if play_even_game() == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
        

def play_even_game():
    i = 0
    while i != 3:
        first = random.randint(0, 100)
        second = random.randint(0, 100)
        print(f'Question: {first} {second}')
        answer = prompt.string('Your answer:\n')
        if int(answer) == nod(first,second):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{nod(first,second)}'.")
    return i


def nod(first,second):
    result = math.gcd(first,second)
    return result
