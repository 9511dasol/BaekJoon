import sys
import math

input = sys.stdin.readline
def q1934():
    for _ in range(int(input().strip())):
        a, b = map(int, input().strip().split())
        print(abs(a * b) // math.gcd(a, b))
q1934()

        