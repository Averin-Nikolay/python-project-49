#!/usr/bin/env python3
import prompt
from brain_games.scripts import main_script
from random import randint

game_name = 'brain-prime'
game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_script():
    main_script.main_intro(game_name, game_rule)
    name = main_script.name
    i = 0
    while i < 3 and i != 4:
        res = 'yes'
        divs = 0
        number = randint(1, 100)
        for n in range(1, number - 1):
            if number % n == 0 and divs > 2:
                res = 'no'
            else:
                divs += 1
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        i = main_script.checker(answer, res, i)
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    game_script()
