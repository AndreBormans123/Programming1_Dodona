# https://dodona.ugent.be/nl/courses/1286/series/14355/activities/200735652

deelbaar_door_3 = set(x for x in range(1, 1001) if x % 3 == 0)
deelbaar_door_7 = set(x for x in range(1, 1001) if x % 7 == 0)
deelbaar_door_11 = set(x for x in range(1, 1001) if x % 11 == 0)

A = set(x for x in range(1, 1001) if x % 3 == 0 and x % 7 == 0 and x % 11 == 0)
B = set(x for x in range(1, 1001) if x % 3 == 0 and x % 7 == 0 and not x % 11 == 0)
C = set(x for x in range(1, 1001) if not x % 3 == 0 and not x % 7 == 0 and not x % 11 == 0)

