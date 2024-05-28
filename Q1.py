def check_a(s):
    b_encouter = False
    for char in s:
        if char == "b":
            b_encouter = True
        elif char == "a":
             if b_encouter:
                 return False
             
    return True        
             
print(check_a("aaa"))        