def min_(arg1, *args):
    # Если на входе больше одного объекта собираем их в один список
    if args:
        iterr = list(args)
        iterr.append(arg1)
        # Избавляемся от вложенности
        def flatt(iterr):
            result = []
            for el in iterr:
                if isinstance(el, (list, set, tuple, dict)):
                    result.extend(flatt(el))
                else:
                    result.append(el)
            return result
        iterable = flatt(iterr)
    # Если один объект передаем в переменную по которой итерируемся
    else:
        iterable = arg1
    # Определяем максималный объект в iterable
    result = iterable[0]
    for el in iterable:
        if el < result:
            result = el
    return result

l1 = (2, 4)
l2 = [1, 5, {12, 34, (234, 345, 45)}]
l3 = [45, 7, {1: '22345', 34534: 1000000}]
print(min_(l1, l2, l3))
