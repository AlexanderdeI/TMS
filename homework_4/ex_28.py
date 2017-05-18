# Декоратор
def decorator_for_sum(func):
    # Функция-обертка которая преобразует входн. эл. в лист
    def prepare_list(*args, **kwargs):
        args = list(args)
        list_for_sum = []
        for el in args:
            if type(el) == float or type(el) == int:
                list_for_sum.append(el)
            else:
                list_for_sum.extend(el)
        return func(list_for_sum)
    return prepare_list

# Оборачиваем функцию в декоратор
@decorator_for_sum
def sum_(list_for_sum):
    result = 0
    for el in list_for_sum:
        result += el
    return result

print(sum_([1, 2, 3], 1, 2))
