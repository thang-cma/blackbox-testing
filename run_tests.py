import sys
import os
sys.path.append(os.path.abspath("src"))

from rectangle import perimeter, area
from quadratic import solve
from days_in_month import days
from prime import is_prime
from sum_alternating import calc as sum_alt
from gcd import gcd
from factorial import calc as fact_sum

def write(file, content):
    file.write(content + "\n")


def test_rectangle(file):
    write(file, "=== RECTANGLE ===")
    write(file, f"perimeter(2,3) = {perimeter(2,3)}")
    write(file, f"area(2,3) = {area(2,3)}")
    write(file, f"perimeter(-1,2) = {perimeter(-1,2)}")


def test_quadratic(file):
    write(file, "\n=== QUADRATIC ===")
    write(file, f"(1,-3,2) = {solve(1,-3,2)}")
    write(file, f"(1,2,1) = {solve(1,2,1)}")
    write(file, f"(1,0,1) = {solve(1,0,1)}")
    write(file, f"(0,2,-4) = {solve(0,2,-4)}")


def test_days(file):
    write(file, "\n=== DAYS IN MONTH ===")
    write(file, f"(2,2024) = {days(2,2024)}")
    write(file, f"(2,2023) = {days(2,2023)}")
    write(file, f"(13,2023) = {days(13,2023)}")


def test_prime(file):
    write(file, "\n=== PRIME ===")
    write(file, f"2 = {is_prime(2)}")
    write(file, f"4 = {is_prime(4)}")
    write(file, f"-5 = {is_prime(-5)}")


def test_sum(file):
    write(file, "\n=== SUM ALTERNATING ===")
    write(file, f"5 = {sum_alt(5)}")
    write(file, f"1 = {sum_alt(1)}")
    write(file, f"0 = {sum_alt(0)}")


def test_gcd(file):
    write(file, "\n=== GCD ===")
    write(file, f"(12,18) = {gcd(12,18)}")
    write(file, f"(0,5) = {gcd(0,5)}")
    write(file, f"(-4,6) = {gcd(-4,6)}")


def test_factorial(file):
    write(file, "\n=== FACTORIAL SUM ===")
    write(file, f"3 = {fact_sum(3)}")
    write(file, f"5 = {fact_sum(5)}")
    write(file, f"-1 = {fact_sum(-1)}")


if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)

    with open("results/output.txt", "w") as f:
        test_rectangle(f)
        test_quadratic(f)
        test_days(f)
        test_prime(f)
        test_sum(f)
        test_gcd(f)
        test_factorial(f)

    print("Done! Check results/output.txt")