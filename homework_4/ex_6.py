def zip_(*args):
    count_arg = len(args)
    # Определяем минимальный список
    len_min_arg = len((sorted(args, key=len)[0]))
    # Переменная, отвечающая за индекс элемента итерируемой последоват.
    el_index = 0
    while el_index < len_min_arg:
        result = []
        # Итерируемся по элементу каждой последоват.
        for obj in args:
            result.append(obj[el_index])
        result = tuple(result)
        print(result)
        # Увеличиваем индекс элемента
        el_index += 1
    else:
        exit()

for i in zip_("1234", ["one", "two", "three"]):
    print(i)
