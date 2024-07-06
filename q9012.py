import sys

input = sys.stdin.readline

def q9012():
    isVPS = list()
    T = int(input().strip())
    while T > 0:
        for i in input().strip():
            # print(i)
            if i == '(': # ( 가 오면 스택에 넣어준다
                isVPS.append(i)
            else:
                if isVPS: # ( 가 있을 경우
                    isVPS.pop()
                else: # ( 가 스택에 없을 때 ) 가 왔을 때
                    print("NO")   
        if isVPS: # 스택에 ( 가 있을 때 탈락
            print("NO") 
        else: # 아무것도 없으면 합격
            print("YES")
        T -= 1
q9012()