def recall_password(cipher_grille, ciphered_password):
    password, degrees = '', 0
    while degrees < 360:
        new_grille = ['.'*4 for i in range(4)]
        for line in range(4):
            for column in range(4):
                if cipher_grille[line][column] == 'X':
                    password += ciphered_password[line][column]
                    new_grille[column] = new_grille[column][:3-line] + 'X' + new_grille[column][4-line:]
        cipher_grille = new_grille
        degrees += 90
    return password


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'