# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/446763531

import math

# FUNCTION IN ANOTHER FUNCTION
def discriminant(a, b, c):
    """
    Calculates the discriminant of a quadratic equation and the number of real solutions and the actual solutions of the equation.
    
    Parameters:
    a (int or float): The coefficient of the x^2 term.
    b (int or float): The coefficient of the x term.
    c (int or float): The constant term.
    
    Returns:
    tuple: A tuple containing the discriminant (float), the number of real solutions (int), the first solution (float), and the second solution (float).
    """
    
#     def solutions(discriminant):
#         """
#         Calculates the number of real solutions and the actual solutions of a quadratic equation.
        
#         Parameters:
#         discriminant (float): The discriminant of the quadratic equation.
        
#         Returns:
#         tuple: A tuple containing the number of real solutions (int), the first solution (float), and the second solution (float).
#         """
#         if discriminant < 0:  # If the discriminant is negative, there are no real solutions
#             return 0, None, None  # Return 0 solutions and None for the solutions
#         elif discriminant == 0:  # If the discriminant is zero, there is one real solution
#             x = -b / (2*a)  # Calculate the one solution using the formula -b / (2a)
#             return 1, x, None  # Return 1 solution and the value of x as the solution
#         else:  # If the discriminant is positive, there are two real solutions
#             x1 = (-b + math.sqrt(discriminant)) / (2*a)  # Calculate the first solution using the formula (-b + sqrt(discriminant)) / (2a)
#             x2 = (-b - math.sqrt(discriminant)) / (2*a)  # Calculate the second solution using the formula (-b - sqrt(discriminant)) / (2a)
#             return 2, x1, x2  # Return 2 solutions and the values of x1 and x2 as the solutions
    
#     discriminant_value = b**2 - 4*a*c  # Calculate the discriminant using the formula b^2 - 4ac
#     return discriminant_value, solutions(discriminant_value)  # Return the discriminant and the result of calling the oplossingen function with the discriminant as the argument

# print(discriminant(1, 0, -1))  # Expected output: (4.0, 1, -1.0, 1.0)
# print(discriminant(1, 4, -5))  # Expected output: (36.0, 1, -5.0, 1.0)


#TWO DIFFERENT FUCNTIONS OUTSIDE OF EACH OTHER
def discriminant(a, b, c):
    """
    Calculates the discriminant of a quadratic equation.
    
    Parameters:
    a (int or float): The coefficient of the x^2 term.
    b (int or float): The coefficient of the x term.
    c (int or float): The constant term.
    
    Returns:
    float: The discriminant of the quadratic equation.
    """
    return float(b**2 - 4*a*c)  # Calculate the discriminant using the formula b^2 - 4ac

def solutions(a, b, c):
    """
    Calculates the number of real solutions and the actual solutions of a quadratic equation.
    
    Parameters:
    a (int or float): The coefficient of the x^2 term.
    b (int or float): The coefficient of the x term.
    c (int or float): The constant term.
    
    Returns:
    tuple: A tuple containing the number of real solutions (int), the first solution (float), and the second solution (float).
    """
    discriminant = b**2 - 4*a*c  # Calculate the discriminant using the formula b^2 - 4ac
    if discriminant < 0:  # If the discriminant is negative, there are no real solutions
        return 0, 0, 0  # Return 0 solutions and None for the solutions
    elif discriminant == 0:  # If the discriminant is zero, there is one real solution
        x = -b / (2*a)  # Calculate the one solution using the formula -b / (2a)
        return 1, x, 0.0  # Return 1 solution and the value of x as the solution
    else:  # If the discriminant is positive, there are two real solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)  # Calculate the first solution using the formula (-b + sqrt(discriminant)) / (2a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)  # Calculate the second solution using the formula (-b - sqrt(discriminant)) / (2a)
        return 2, x2, x1  # Return 2 solutions and the values of x1 and x2 as the solutions
