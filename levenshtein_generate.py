CHARS = [chr(x) for x in range(ord("a"), ord("z") + 1)]


def within_levenshtein(string, distance):
    if distance == 0:
        yield string
        return
    for s in insertions(string):
        yield from within_levenshtein(s, distance - 1)
    for s in deletions(string):
        yield from within_levenshtein(s, distance - 1)
    for s in substitutions(string):
        yield from within_levenshtein(s, distance - 1)


def insertions(string):
    for char in CHARS:
        for i in range(len(string)):
            yield string[:i] + char + string[i:]


def deletions(string):
    for i in range(len(string)):
        yield string[:i] + string[i + 1 :]


def substitutions(string):
    for char in CHARS:
        for i in range(len(string)):
            yield string[:i] + char + string[i + 1 :]


def main():
    string = "hi"
    distance = 3
    print(string)
    print("---")
    strings = list(within_levenshtein(string, distance))
    print(len(strings))
    print(len(set(strings)))


main()

