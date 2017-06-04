# Если хоть один объект итерируемый возвращаем True
# В противном случае False
def any_(*iterable):
    result = []
    for el in iterable:
        if isinstance(el, (int, float)):
            result.append(False)
        else:
            result.append(True)
    for el in result:
        if el:
            return el
    return el

print(any_(1, 3, ["asd", "qwe"]))
