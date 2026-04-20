def gcd(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Invalid"

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b
    return a