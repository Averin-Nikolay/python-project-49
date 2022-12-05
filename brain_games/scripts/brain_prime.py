#!/usr/bin/env python3
import prompt
import math
from brain_games.scripts import main_script
from random import randint

game_name = 'brain-prime'
game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_script():
    i = 0
    while i < 3:
        divs = []
        number = randint(1, 100)
        for n in range(1, number - 1):
            if number % n == 0:
                divs.append(n)
        if len(divs) > 2:
            print(len(divs))
            print(divs)
            res = "no"
        else:
            res = "yes"
        print(number)
        answer = prompt.string('Your answer: ')
        if answer != res:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer "
                f"was '{res}'.\nLet's try again, {name}! ")
        else:
            print('Correct!')
            i += 1

    if i == 3:
        print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main_script.main_intro(game_name, game_rule)
    name = main_script.name
    game_script()




