# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/1515270930


def fib(n, depth=0):
    # Print the depth and value of n when the function is called
    print("  " * depth + "fib(" + str(n) + ")")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Increase the depth parameter by 1 when calling the function recursively
        result = fib(n-1, depth+1) + fib(n-2, depth+1)
        # Print the returned value, indented according to the depth
        print("  " * depth + "return " + str(result))
        return result

print(fib(5))