#!/usr/bin/env python3
import prompt
from random import randint


def main():
    name = ""
    print('brain-even \n\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = randint(1, 100)
        if num % 2 == 0:
            res = 'yes'
            # i += 1
        else:
            res = 'no'
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if answer != res:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer "
                f"was '{res}'.\nLet's try again, {name}! "
            )
        else:
            print('Correct!')
            i = i + 1
        if i == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
