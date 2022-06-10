def solve(number, iterations):
    for num in range(iterations):
        if str(number)[-1] == '0':
            number //= 10
        else:
            number -= 1
        print(str(number))
    return number
