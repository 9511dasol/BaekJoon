import sys
import math

input = sys.stdin.readline
def q13241():
    a, b = map(int, input().strip().split())
    print(abs(a * b) // math.gcd(a,b))
    # math 모듈에서 gcd 함수를 사용하여 최대공약수를 구한 후, 
    # 이를 이용하여 최소공배수를 계산합니다.
q13241()