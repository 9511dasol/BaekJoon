import sys
import math

input = sys.stdin.readline
def q1735():
    a, b = map(int, input().strip().split())
    c, d = map(int, input().strip().split())
    
    A = a * d + b * c
    B = d * b
    gcd = math.gcd(A,B)
    
    print(A//gcd, B//gcd)
q1735()