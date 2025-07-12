import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate the roots
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Roots are real and distinct: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"Roots are real and equal: {root}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return f"Roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"

# Get coefficients from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation
print(solve_quadratic(a, b, c))
