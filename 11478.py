import sys

def q11478():
    input = sys.stdin.readline
    st = set()
    S = input().strip() # 5글자
    if len(S) > 1000:
        return
    lenth = len(S)
    a = 0

    while a < lenth:
        for i in range(lenth-a): # - 0 ~ - 4
            st.add(S[i:i+1+a]) 
        a += 1
    return len(st)
print(q11478())

# a= 'ababc'
# print(a[0:5]) # 1개

#  a, b, c, ab, ba, bc, aba, bab, abc, abab, babc, ababc