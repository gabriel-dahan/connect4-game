from typing import List
from libgravatar import Gravatar
import random as r

def rand_uid(length: int = 7) -> str:
    """ Generates a unique id with given length. """
    alph = ''.join(chr(ordinal) for ordinal in range(97, 123))
    num = '0123456789'
    return ''.join(r.choice(list(alph) + list(num) + list(alph.upper())) for _ in range(length))

def linear_as_int_grid(linear_grid: str) -> List[List[int]]:
    return [[int(elem) for elem in line] for line in linear_grid.split('-')]
    
def int_grid_as_linear(int_grid: List[List[int]]) -> str:
    res = ''
    for line in int_grid:
        res += ''.join(str(elem) for elem in line)
        res += '-'
    return res[:-1]

def anonymize_email(email: str) -> str:
    after_at = email.split('@')[1]
    return f'{email[0]}***@{after_at}'

def generate_avatar_url(_str: str):
    g = Gravatar(email = _str)
    return g.get_image(default = 'identicon')