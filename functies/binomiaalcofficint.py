# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/33489040

#Faculteit berekenen
def faculteit(getal):
    factorial = 1
    for i in range(1, getal + 1):
        factorial = factorial * i
    return factorial


#binomiaal berekenen
def binomiaal(n,k):
    factorial_n = 1
    factorial_k = 1
    factorial_verschil = 1
    verschil = n - k
    for x in range(1, n + 1):
        factorial_n = factorial_n * x
    for y in range(1, k + 1):
        factorial_k = factorial_k * y
    for a in range(1, verschil + 1):
        factorial_verschil = factorial_verschil * a
    oplossing = (factorial_n) / (factorial_k *  (factorial_verschil))
    return int(oplossing)



if __name__ == '__main__':
    print(faculteit(5))
    print(binomiaal(7,3))



