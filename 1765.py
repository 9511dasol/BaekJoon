def q10816_fix():
    input = sys.stdin.readline
    int(input())
    cards = list(map(int, input().strip().split()))
    int(input())
    cardss = list(map(int, input().strip().split()))
    confirm = dict()
    for i in cards:
        if i in confirm: # key가 있는지 여부 판단
            confirm[i] +=1
        else:
            confirm[i] = 1 
    for x in cardss:
        print(confirm.get(x, 0), end=' ') # x가 있으면 그 개수 반환, 아니면 0출력
# q10816_fix()
import sys
input = sys.stdin.readline
N,M, = map(int, input().strip().split())
set1, set2= set(), set()

for _ in range(N):
    set1.add(input().strip())
for _ in range(M):
    set2.add(input().strip())
intersection = set1.intersection(set2)

print(len(intersection))
for x in sorted(intersection):
    print(x)

