def remainder_of_division(first_num, second_num):
    if first_num < second_num or second_num == 0:
        return False
    else:
        result = first_num % second_num
        return result

print(remainder_of_division(16, 9))
