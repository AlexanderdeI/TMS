def factorial(num):
    result = []
    supl = 1
    if num == 1:
        result.append(1)
    else:
        for n in range(1, num):
            supl *= n
        result.append(num * supl)
    if num > 0:
        result.extend(factorial(num - 1))
    return result

print(factorial(10))
