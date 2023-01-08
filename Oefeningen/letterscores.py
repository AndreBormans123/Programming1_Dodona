# https://dodona.ugent.be/nl/courses/1286/series/14347/activities/774332532


punt = int(input("Enter: "))

if punt >= 90 and punt <= 100:
    print("A")
elif punt >= 80 and punt <= 90:
    print("B") 
elif punt >= 70 and punt <= 79:
    print("C")
elif punt >= 60 and punt <= 69:
    print("D")
else:
    print("F")
