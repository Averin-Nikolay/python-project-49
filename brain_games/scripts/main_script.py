import prompt
game_name = ''
game_rule = ''
name = ''


def main_intro(game_name, game_rule):
    global name
    print(f'{game_name}'
          f'\n\nWelcome to the Brain Games! ')
    name = prompt.string('May I have your names?')
    print(f'Hello, {name}')
    print(game_rule)
    return name











