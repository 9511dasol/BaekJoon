import sys

def isprime(x):
    for i in range(2, int(x**0.5)+1, 1): # 제곱근+1을 기억하자 <= 소수 문제 ㅇㅇ
        if x % i == 0:
            return False
    return True
    
input = sys.stdin.readline

def q1929():
    M,N = map(int, input().strip().split())
    
    for x in range(M, N+1, 1):
        if isprime(x):
            print(x)
def fix1929():
    M,N = map(int, input().strip().split())
    
    for x in range(M, N+1, 1):
        if x == 1: 
            continue
        elif x == 2:
            print(x)
            continue
        elif x ==3:
            print(x)
            continue
        elif x==4:
            continue
        elif isprime(x):
            print(x)
fix1929()