def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    ans = []
    if data:
        start, end = min(data), max(data)
        for i in range(start, end+1):
            if i in data and i+1 not in data:
                ans.append((start, i))
            if i not in data and i+1 in data:
                start = i+1
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')