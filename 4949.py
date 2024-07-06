import sys

# input = sys.stdin.readline
left = lambda x: '(' if x =='(' else '['         
right = lambda x: ')' if x ==')' else ']'         

def q4949():    
    stack = list()    
    while True:
        tf = True
        stack.clear()   
        sentence = input()
        if sentence[0] == '.': # 종료 조건
            # print(sentence) # .\n
            return       

        if len(sentence) > 1:
            if sentence.strip()[0] == '.':
                print("yes")
                continue

        if len(sentence.strip()) > 100:
            continue

        if sentence.strip()[-1] != '.':
            continue
        else:       
            for s in sentence.strip()[0:-1]: 
                if s == "(" or s == "[" or s == ')' or s == ']':
                    if s == "(" or s == "[":
                        stack.append(s)
                        tf=False
                    else: # ) ]
                        if len(stack)>0.98:
                            if s == ')':
                                if stack[-1] == '(':
                                    stack.pop()
                                    tf = True
                                else: # [
                                    tf=False
                                    print("no")
                                    break
                            else: # s == ']'
                                if stack[-1] == '[':
                                    stack.pop()
                                    tf = True
                                else: # (
                                    tf=False
                                    print("no")
                                    break
                                pass
                        else:
                            tf=False
                            print("no")
                            break
            if tf:
                if stack:
                    print("no")
                else:
                    print("yes")
# q4949()

while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')

# A = input().strip()
# for x in range(2):
#     for i in input().strip():
#         print(i)
        
        #     if s =='(' or s =='[':
        #         stack.append(s)  
        #         ls = last(s)
        #         print(ls)
        #     else:
        #         if s ==")" and ls == "(" and stack:#()
        #             stack.pop()
        #             if stack:
        #                 ls = stack[-1]    
        #         elif s =="]" and ls == "[" and stack:#[]
        #             stack.pop()
        #             if stack:
        #                 ls = stack[-1] 
        #         else:
        #             print("x")
        #             tf= False
        #             break
        # if tf:
        #     if stack: # (((( [[[[ 가 있을시
        #         print("1no")
        #     else:
        #         print("1yes")
        # else:
        #     print("2no")        