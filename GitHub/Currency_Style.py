import re


def checkio(string):
    def repl(matchobj):
        part1, part2 = matchobj.group(1), matchobj.group(3)
        if part1:
            return part1.replace('.', ',') + part2.replace(',', '.')
        return part2.replace(',', '.')
    newstring = re.sub(r'(?<=\$)((\d+\.)*)(\d+,\d+)', repl, string)
    return newstring

# print(checkio('$111.222.333.444,555'))
if __name__ == '__main__':
    assert checkio("Lot 192.001 costs $1.000,94.") == "Lot 192.001 costs $1,000.94."
    assert checkio("$1,23 + $2,34 = $3,57.") == "$1.23 + $2.34 = $3.57."