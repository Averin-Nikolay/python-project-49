#!/usr/bin/env python3
import prompt
import math
from brain_games.scripts import main_script
from random import randint


game_name = 'brain-gcd'
game_rule = 'Find the greatest common divisor of given numbers.'


# An additional script (out of rules)
def cheat_gcd():
    i = 0
    while i < 3:
        num_1 = randint(0, 100)
        num_2 = randint(0, 100)
        cheat_result = math.gcd(num_1, num_2)
        print(f'Question: {num_1} {num_2}')
        answer = prompt.string('Your answer: ')
        if int(answer) != cheat_result:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer "
                f"was '{cheat_result}'.\nLet's try again, {name}! ")
            break
        else:
            print('Correct!')
            i = i + 1
    if i == 3:
        print(f'Congratulations, {name}!')
# if __name__ = '__main__':
# main_script.main_intro(game_name, game_rule)
# name = main_script.name
# cheat_gcd()


def game_script():
    main_script.main_intro(game_name, game_rule)
    name = main_script.name
    i = 0
    while i < 3:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        print(f'Question: {num_1} {num_2}')
        while num_1 != num_2:
            if num_1 >= num_2:
                num_1 -= num_2
            else:
                num_2 -= num_1
        res = num_1
        answer = prompt.string('Your answer: ')
        if int(answer) != res:
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
