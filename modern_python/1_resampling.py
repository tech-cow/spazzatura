'''
Resampling
===========

Big Idea: Statistics modeled in a program are easier to
get right and understand than using a formulaic
approach, It is also extends to more complicated
situations that classic formulasself.

Topics to Prepare for Resampling
=================================


* F-strings
    Example Usage: https://gist.github.com/yuzhoujr/140227b402598556e8cb91695e9490ad
* Counter(), most_common, elements
* Statistics
* Random: seed gauss triangular expovariate
*         choice choices sample shuffle
* Review list concatenation, slicing, count/index, sorted()
* Review lambda expressions and chained comparisons.


'''
import pprint
from collections import Counter

newline = '\n'
doubleline = '\n\n'
space = '\n\n\n'


def f_strings():
    ''' Modern way of calling f-strings'''
    old = 'The answer is %d today' % 10
    new = 'The answer is {0} today'.format(10)
    new2 = 'The answer is {x} today and {y} tomorrow'.format(x=10, y=11)
    new3 = f'The answer is {10} today'
    return[old, new, new2, new3]


def py_counter():
    '''Counter(), most_common, elements'''
    # Old
    d = {}                  # d['dragons'] -> KeyError

    # New
    c = Counter("red green red blue red blue green".split())
    most_common = f'@ Most Common{newline}' +\
        f'>>> c = Counter("red green red blue red blue green".split()){newline}' +\
        f'{Counter("red green red blue red blue green".split())}{newline}' +\
        f'>>> c.most_common(1){newline}' +\
        f'{c.most_common(1)}{newline}' +\
        f'>>> c.most_common(2){newline}' +\
        f'{c.most_common(2)}{newline}'

    elements = f'@ Elements' +\
        f'>>> list(c.elements()){newline}' +\
        f'{list(c.elements())}{newline}' +\
        f'>>> list(c){newline}' +\
        f'{list(c)}{newline}' +\
        f'>>> list(c.values()){newline}' +\
        f'{list(c.values())}{newline}' +\
        f'>>> list(c.items()){newline}' +\
        f'{list(c.items())}{newline}'

    return [most_common, elements]


def main():
    print(space)
    pprint.pprint(f_strings())
    print(space)
    [print(item) for item in py_counter()]


if __name__ == '__main__':
    main()
