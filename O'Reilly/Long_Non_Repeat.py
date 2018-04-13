def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    if not line:
        return ''
    parts = []
    while True:
        temp = ''
        for letter in line:
            if letter in temp:
                parts.append(temp)
                line = line[line.index(letter)+1:]
                break
            temp += letter
            if len(temp) == len(line):
                parts.append(temp)
                return max(parts, key=len)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')