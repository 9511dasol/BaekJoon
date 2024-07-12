import sys

input = sys.stdin.readline

def q9012():
    stack = list()
    for _ in range(int(input().strip())):
        stack.clear()
        t = False
        line = input().strip()
        for s in line:
            if s == '(':
                stack.append(s)
            else:
                if stack: # STACK에 ( 가 있을시에 
                    stack.pop()
                else: # STACK에 아무것도 없을시 
                    print("NO")
                    t = True
                    break
        if t: 
            continue
        elif stack: # 스텍이 (가 남아있을시
            print("NO")
        else: # 스택이 깔끔할시ㅣㅣ
            print("YES")
q9012()