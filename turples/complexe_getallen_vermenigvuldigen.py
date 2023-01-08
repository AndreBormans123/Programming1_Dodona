# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/1180618752

def product(a, b):
    real_part = a[0] * b[0] - a[1] * b[1]
    imag_part = a[0] * b[1] + a[1] * b[0]
    return (real_part, imag_part)

tuple_a = (3, 4)
tuple_b = (7, 2) 

print(product(tuple_a, tuple_b))
