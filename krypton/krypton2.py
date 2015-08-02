PASSWORD = "OMQEMDUEQMEK"

INPUT  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
OUTPUT = "MNOPQRSTUVWXYZABCDEFGHIJKL"


def rotate(c, distance=13):
    if c == ' ':
        return c
    return chr((((ord(c) - 65) + distance) % 26) + 65)

distance = ord(INPUT[0]) - ord(OUTPUT[0])
print ''.join(map(lambda c:rotate(c, distance), PASSWORD))
