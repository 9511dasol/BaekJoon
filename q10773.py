import sys

input = sys.stdin.readline

def q10773():
    k = int(input())
    di = list()
    for x in range(k):
        val = int(input())
        if val == 0 and di:
            di.pop()
        else:
            di.append(val)
    print(sum(di))        
q10773()             
                        
    
