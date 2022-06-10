def solve(brackets):
    count_open = 0
    for char in brackets:
        if (char == ')' and count_open == 0):
            count_open -= 1
            break
            
        if char == ')':
            count_open -= 1
        else:
            count_open += 1
    if count_open == 0:
        return True
    return False



a = "(((((((((((((((((((((((((((((())))))))))))))))))))))))))))))"
print(solve(a))
