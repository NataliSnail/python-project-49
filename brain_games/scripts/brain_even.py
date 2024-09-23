#!/usr/bin/env python3


import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? \n')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if play_even_game() == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")

    if __name__ == '__main__':
        main() 


def play_even_game():
    i = 0
    while i != 3:
        random_num = random.randint(0, 100)
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer:\n')
        if answer == check(random_num):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was'{check(random_num)}'.")
            break
    return i


def is_even(random_num):
    if random_num % 2 == 0:
        return True
    else:
        return False


def check(random_num):
    result = 'yes' if is_even(random_num) else 'no'
    return result
