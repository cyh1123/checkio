def checkio(opacity):
    temp = 10000
    y = 0
    a, b = 1, 1
    while opacity != temp:
        y += 1
        if y == b:
            temp -= b
            a, b = b, a + b
        else:
            temp += 1
        if y >= 5000:
            return
    return y

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
