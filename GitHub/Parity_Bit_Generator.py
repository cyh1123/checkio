def checkio(message):
    """
        your code here
    """
    trans = []
    for msg in message:
        if bin(msg)[2:].count('1') % 2 == 0:
            trans.append(chr(int(bin(msg)[:-1], 2)))
    return ''.join(trans)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([135, 134, 124, 233,
                    209, 81, 42, 202,
                    198, 194, 229, 215,
                    230, 146, 28, 210,
                    145, 137, 222, 158,
                    49, 81, 214, 157]) == "Checkio"
    assert checkio([144, 100, 200, 202,
                    216, 152, 164, 88,
                    216, 222, 65, 218,
                    175, 217, 248, 222,
                    171, 228, 216, 205,
                    254, 201, 193, 220]) == "Hello World"