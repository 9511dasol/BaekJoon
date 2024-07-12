def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    if(len(overwrite_string) == len(my_string[s:])):
        answer = my_string[:s] + overwrite_string
    return answer


def solution2(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] 
        answer += str2[i]
    return answer

def solution3(arr):
    answer = ''
    for s in arr:
        answer += s
    return answer
# print(solution("Program29b8UYP", "merS123", 7))
# print(solution2("ccccccc", "bbbbbbb"))

def solution4(a, b):
    answer = 0
    aa = int(str(a) + str(b))
    bb = int(str(b) + str(a))
    
    if aa > bb:
        answer = aa
    else: 
        answer == bb
    print(answer)
    return answer
# solution4(89, 9-1)

a = lambda x: x % 2 == 0
# print(a(2))

def solution(ineq, eq, n, m):
    if ineq == '<':
        if eq == '=':
            if n <= m:
                return 1
            else:
                return 0
        else:
            if n < m:
                return 1
            else:
                return 0
    else: # >
        if ed =='=':
            if n >= m:
                return 1
            else:
                return 0
        else:
            if n > m:
                return 1
            else:
                return 0
            
a = []

def solution0(code):
    mode = 0
    ret = ''
    for n in range(len(code)):
        i = code[n]
        
        if mode == 0:            
            if i == '1':
                mode = 1
            else:
                if n % 2 == 0:
                    ret += i
        else: # mode 1
            if i == '1':
                mode = 0
            else:
                if n % 2 == 1:
                    ret += i
    return ret
# print(solution0("abc1abc1abc"))///

def solutiona(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a + (i + 1 - 1) * d
        else:
            pass
    return answer
print(solutiona(3, 4, [True, False, False, True, True]))