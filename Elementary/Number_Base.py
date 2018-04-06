import string

chrmap = string.digits + string.ascii_lowercase


def checkio(str_number, radix):
    if not str_number:
        return 0
    if chrmap.index(max(str_number.lower())) >= radix:
        return -1
    return chrmap.index(str_number[0].lower()) * pow(radix, len(str_number) - 1) + checkio(str_number[1:], radix)


def checkio2(str_number, radix):
    str_number = str_number.lower()
    if chrmap.index(max(str_number)) >= radix:
        return -1
    val = 0
    for i in range(len(str_number)):
        val += chrmap.index(str_number[-i - 1]) * pow(radix, i)
    return val


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
