import prompt
from brain_games.scripts import main_script
from random import randint
game_name = ''
game_rule = ''


def main_intro(game_name, game_rule):
    global name
    print(f'{game_name}'
          f'\n\nWelcome to the Brain Games! ')
    name = prompt.string('May I have your names? ')
    print(f'Hello, {name}!')
    print(game_rule)
    return name


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


def checker(answer, res, i):
    if answer != res:
        print(
            f"'{answer}' is wrong answer ;(. Correct answer "
            f"was '{res}'.\nLet's try again, {name}! ")
        i = 4
    else:
        print('Correct!')
        i += 1
    return i


if __name__ == '__main__':
    game_script()
