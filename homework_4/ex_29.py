# Функция фильтрующая последователность по условию
def filter_(seq, cond):
    result = []
    for el in seq:
        el = cond(el)
        if el:
            result.append(el)
    return result

# Условия
def cond_number(el):
    if isinstance(el, (int, float)):
        return el
    return False

def cond_str(el):
    if isinstance(el, str):
        return el
    return False

def cond_list(el):
    if isinstance(el, list):
        return el
    return False

l = [1, 2, '3', ['l', 'k', 'rt'], '4', '5', 6.0]

print(filter_(l, cond_number))
print(filter_(l, cond_str))
print(filter_(l, cond_list))
