

DATA = "YRIRY GJB CNFFJBEQ EBGGRA"

def rotate(c, distance=13):
    if c == ' ':
        return c
    return chr((((ord(c) - 65) + distance) % 26) + 65)

for i in range(26):
    print ''.join(map(lambda c: rotate(c, i), DATA))
