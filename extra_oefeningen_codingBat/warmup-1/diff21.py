def diff21(n):
    getal = 21
    if n > getal:
        tussenstap = getal - n
        uitkomst = tussenstap * 2
        return abs(uitkomst)
    else:
        uitkomst = getal - n
        return abs(uitkomst)

print(diff21(22))