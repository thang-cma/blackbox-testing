def perimeter(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid"
    if a <= 0 or b <= 0:
        return "Invalid"
    return 2 * (a + b)

def area(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid"
    if a <= 0 or b <= 0:
        return "Invalid"
    return a * b