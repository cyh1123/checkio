def checkio(text):
    text = text.lower()
    d = {}
    L = []
    for letter in text:
        if letter.isalpha():
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1
    for item in d.items():
        if item[1] == max(d.values()):
            L.append(item)
    if len(L) == 1:
        return L[0][0]
    return min(L)[0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

