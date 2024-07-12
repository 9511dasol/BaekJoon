import sys

def q1269():
    input = sys.stdin.readline

    A, B = map(int, input().strip().split())
    a = set(map(int, input().strip().split()))
    b = set(map(int, input().strip().split()))
    if len(a) != A and len(b) != B:
        return
    return a.symmetric_difference(b) # a ^ b => 대칭 차집합
print(len(q1269()))