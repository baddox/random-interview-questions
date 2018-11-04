def is_valid(string):
    level = 0
    for char in string:
        if char == "[":
            level += 1
        if char == "]":
            level -= 1
        if level < 0:
            return False
    if level != 0:
        return False
    return True


def main():
    valid = [
        # keep this formatting
        "",
        "[]",
        "[][][][][]",
        "[[[][][][[]]]]",
    ]
    invalid = [
        # keep this formatting
        "[",
        "]",
        "[[]][",
        "[[[][][]]][[][[]]]]",
    ]

    for string in valid:
        print("valid", is_valid(string))
    for string in invalid:
        print("invalid", not is_valid(string))


main()

