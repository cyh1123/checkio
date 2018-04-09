def check_connection(network, p1, p2):
    relations = list(network)
    part1 = {p1}
    part2 = {p2}
    while True:
        origin = relations[:]
        for r in relations:
            temp = r.split('-')
            if temp[0] in part1 or temp[1] in part1:
                part1 = part1 | set(temp)
                relations.remove(r)
            if temp[0] in part2 or temp[1] in part2:
                part2 = part2 | set(temp)
                if r in relations:
                    relations.remove(r)
            if part1 & part2:
                return True
        if len(origin) == len(relations):
            return False


if __name__ == '__main__':
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False

