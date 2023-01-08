# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/1180320113

def tafel_van_vermenigvuldiging(getal):
    for i in range(1, 11):
        oplossing = i * getal
        print(f"{i} * {getal} = {oplossing}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    tafel_van_vermenigvuldiging(10)




