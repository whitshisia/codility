def solution(N):
    import string
    
    for k in range(26, 0, -1):
        if N % k == 0:
            break
    
    repeat_count = N // k
    
    letters = string.ascii_lowercase[:k]
    result = ''.join(letter * repeat_count for letter in letters)
    
    return result

print(solution(5))
    