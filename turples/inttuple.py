# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/1567511933

def flatten(t):
    flattened = []
    for x in t:
        if isinstance(x, int):
            flattened.append(x)
        else:
            flattened.extend(flatten(x))
    return tuple(flattened)

inttuple = (1, 2, (3, 4), 5, ((6, 7, 8, (9, 10), 11), 12, 13), ((14, 15, 16), (17, 18, 19, 20)))
print(flatten(inttuple))
