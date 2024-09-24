import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? \n')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    if play_even_game() == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
        

def play_even_game():
    i = 0
    while i != 3:
        first = random.randint(0, 10)
        second = random.randint(0, 10)
        operation = random.choice(['+','-','*'])
        print(f'Question: {first} {operation} {second}')
        answer = prompt.string('Your answer:\n')
        if int(answer) == calc(first,second,operation):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{calc(first,second,operation)}'.")
    return i


def calc(first,second,operation):
    if operation == '+':
        return first + second
    if operation == '-':
        return first - second
    if operation == '*':
        return first * second

