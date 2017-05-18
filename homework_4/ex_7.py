def enumerate_(iterable, start=0):
    # Если объект неитерируемый прекращаем программу
    if isinstance(iterable, (int, float)):
        return False
        exit()
    else:
        for el in iterable:
            result = (start, el)
            print(result)
            start += 1
        else:
            exit()

print(enumerate_(['zero', 'one', 'two', 'three']))
