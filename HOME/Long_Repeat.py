import itertools

import re


def long_repeat0(line):
    """
        length the longest substring that consists of the same char
    """
    if not line:
        return 0
    longest = max(len(list(g)) for k, g in itertools.groupby(line))
    return longest


def long_repeat(line):
    longest = 0
    for letter in set(line):
        temp = re.findall(letter + '+', line)
        longest = max(list(len(x) for x in temp) + [longest])
    return longest





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
