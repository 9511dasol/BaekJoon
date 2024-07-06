import sys
import math
def isprime(x):
    if x == 0 or x==1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(x)) + 1, 1):
            if x % i == 0:
                return False
        return True
        
		
def q4134():
    input = sys.stdin.readline 
    for _ in range(int(input())):
        n = int(input())
        while True:
            if isprime(n):
                print(n)
                break
            else:
                n += 1
q4134()
         