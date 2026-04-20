def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def calc(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid"

    return sum(factorial(i) for i in range(1, n+1))