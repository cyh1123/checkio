def power_supply(connections, power_plants):
    items, circle = set(), set()
    for c in connections:
        items |= set(c)
    while any(power_plants.values()):
        for k in power_plants.keys():
            temp = set([k])
            while power_plants[k] > 0:
                for i in connections:
                    if temp & set(i):
                        temp |= set(i)
                        connections.remove(i)
                power_plants[k] -= 1
            circle |= temp
    return items - circle


if __name__ == '__main__':
    assert power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['с2'])
    assert power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3'])
    assert power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([])