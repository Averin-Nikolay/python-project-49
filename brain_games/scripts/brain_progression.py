#!/usr/bin/env python3
import prompt
from brain_games.scripts import main_script
from random import randint


game_name = 'brain-progression'
game_rule = 'What number is missing in the progression?'


def game_script():
    main_script.main_intro(game_name, game_rule)
    name = main_script.name
    i = 0
    while i < 3:
        progression = ''
        res = ''
        lenght = randint(6, 10)
        start = randint(1, 50)
        offset = randint(1, 10)
        hiden_number = randint(1, lenght - 1)
        progression = str(start)
        for n in range(1, lenght):
            cur_value = start + n * offset
            if n != hiden_number:
                progression += ' ' + str(cur_value)
            else:
                progression += ' ..'
                res = str(cur_value)
        print(f'Question: {progression}')
        answer = prompt.string('Your answer: ')
        if answer == res:
            print('Correct!')
            i += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer "
                f"was '{res}'.\nLet's try again, {name}! ")
            break
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    game_script()
