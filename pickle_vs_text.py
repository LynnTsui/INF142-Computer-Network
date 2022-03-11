from pickle import dumps
from sys import getsizeof

from rich import print
from rich.table import Table

from core import Champion, Match, Shape, Team

match = Match(
    Team([Champion(f'Champ{i}') for i in range(1, 4)]),
    Team([Champion(f'Champ{i}') for i in range(4, 7)])
)
match.play()

pickled_match = dumps(match)
print(f'Pickled match:\n{pickled_match}')
print(f'Size of pickled match: {getsizeof(pickled_match)}')

EMOJI = {
    Shape.ROCK: ':raised_fist-emoji:',
    Shape.PAPER: ':raised_hand-emoji:',
    Shape.SCISSORS: ':victory_hand-emoji:'
}

round_summary = Table(title='Round X')
round_summary.add_column("Red",
                         style="red",
                         no_wrap=True)
round_summary.add_column("Blue",
                         style="blue",
                         no_wrap=True)

round = match.rounds[0]
for key in round:
    red, blue = key.split(', ')
    round_summary.add_row(f'{red} {EMOJI[round[key].red]}',
                          f'{blue} {EMOJI[round[key].blue]}')

picled_table = dumps(round_summary)

print(f'Pickled table:\n{picled_table}')
print(f'Size of a pickled table: {getsizeof(picled_table)}')
print(f'Size of three pickled tables: {3*getsizeof(picled_table)}')

shape2letter = {
    Shape.ROCK: 'r',
    Shape.PAPER: 'p',
    Shape.SCISSORS: 's'
}

message = '\n\n'.join(
    '\n'.join(
        (f'{key};'
          f'{shape2letter[round[key].red]};'
          f'{shape2letter[round[key].blue]}') for key in round
    ) for round in match.rounds
)

print(f'Plain message:\n{message}')
print(f'Size of plain message: {getsizeof(message)}')

print('[red]Moral of the story: [/red]'
      'Avoid using pickle for objects that are easily parsed as text!')
