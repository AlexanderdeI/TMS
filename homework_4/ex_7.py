def enumerate_(iterable, start=0):
    # Если объект неитерируемый прекращаем программу
    if isinstance(iterable, (int, float)):
        return False
        exit()
    else:
        result = []
        for el in iterable:
            tuple_el = (start, el)
            result.append(tuple_el)
            start += 1
    return result

print(enumerate_(['zero', 'one', 'two', 'three']))
