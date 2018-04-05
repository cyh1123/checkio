from collections import Iterable


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    themin = []
    if not key:
        key = lambda x: x
    while True:
        try:
            if len(args) == 1 and args != args[0] and isinstance(args[0], Iterable):
                args = args[0]
                continue
        except:
            break
        break

    for i in args:
        if themin == []:
            themin = i
        if key(i) < key(themin):
            themin = i
    return themin


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    themax = []
    if not key:
        key = lambda x: x
    while True:
        try:
            if len(args) == 1 and args != args[0] and isinstance(args[0], Iterable):
                args = args[0]
                continue
        except:
            break
        break

    for i in args:
        if themax == []:
            themax = i
        if key(themax) < key(i):
            themax = i
    return themax



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

