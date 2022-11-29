#!/usr/bin/env python3
from brain_games.scripts import main_script
import prompt
from random import randint


game_name = 'brain-calc'
game_rule = 'What is the result of the expression?'
name = ''

def game_script():
    i = 0
    while i < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        x = randint(0, 2)
        if x == 0:
            res = num1 + num2
            print(f'Question: {num1} + {num2}')
        elif x == 1:
            res = num1 - num2
            print(f'Question: {num1} - {num2}')
        else:
            res = num1 * num2
            print(f'Question: {num1} * {num2}')
        answer = prompt.string('Your answer: ')
        if int(answer) != res:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer "
                f"was '{res}'.\nLet's try again, {name}! "
            )
        else:
            print('Correct!')
            i = i + 1
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main_script.main_intro(game_name, game_rule)
    name = main_script.name
    game_script()
