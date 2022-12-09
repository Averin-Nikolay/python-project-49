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
    while i < 3:
        res = 'yes'
        divs = 0
        number = randint(1, 100)
        for n in range(1, number - 1):
            if number % n == 0 and divs > 2:
                res = 'no'
            else:
                divs += 1
        print(res)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer != res:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer "
                f"was '{res}'.\nLet's try again, {name}! ")
            break
        else:
            print('Correct!')
            i += 1
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    game_script()
