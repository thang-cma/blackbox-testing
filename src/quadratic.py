import math

def solve(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        return "Invalid"

    if a == 0:
        if b == 0:
            return "No solution"
        return -c / b

    delta = b*b - 4*a*c

    if delta < 0:
        return "No real root"
    elif delta == 0:
        return -b / (2*a)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)