
def minimumParentheses(pattern):
    
    n = len(pattern)
    count = 0
    res = 0

    for i in range(n):
        if pattern[i] == ')':
            count -=1
        else:
            count+=1
        
        if count == -1:
            res+=1
            count+=1
    return res + count