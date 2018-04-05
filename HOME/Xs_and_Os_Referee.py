def checkio(game_result):
    s1, s2 = '', ''
    for i in range(len(game_result)):
        s3 = ''
        for j in game_result:
            if len(set(j)) == 1 and j[0] != '.':
                return j[0]
            s3 += j[i]
        if len(set(s3)) == 1 and s3[0] != '.':
            return s3[0]
        s1 += game_result[i][i]
        s2 += game_result[i][-i-1]
    for k in [s1, s2]:
        if len(set(k)) == 1 and k[0] != '.':
            return k[0]
    return 'D'

# numpy ?

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

