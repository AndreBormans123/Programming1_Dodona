# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/373633979
import copy


lijst = [1, 3, 7,  2, 5, 6, 3, 8, 5, 7, 6, 1]
lijst.sort()
lijst_copy = copy.deepcopy(lijst)
lijst_copy.sort()
nieuwe_lijst = []
counter = 0
counter1= 0 

for i in range(0, len(lijst)):
    nieuwe_lijst.append(lijst[i])
    lijst_copy.pop(0)
    if lijst_copy ==  []:
        break
    else:
        if lijst_copy[0] == nieuwe_lijst[counter]:
            nieuwe_lijst.pop(counter)
        else:
            counter += 1
print(nieuwe_lijst)