def checkio(N):
    pigeons, munites = 0, 0
    while True:
        munites += 1
        if N < pigeons:
            return pigeons
        pigeons += munites
        if N < pigeons:
            return N
        N -= pigeons


if __name__ == '__main__':
    assert checkio(1) == 1
    assert checkio(2) == 1
    assert checkio(5) == 3
    assert checkio(10) == 6
