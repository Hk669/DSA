def solution(A):
    
    unique = set(x for x in A if x>0)

    if not unique:
        return 1

    smallest = 1
    while smallest in unique:
        smallest+=1
    return smallest

    
# Example usage:
A = [1, 3, 6, 4, 1, 2]
result = solution(A)
print(result)
