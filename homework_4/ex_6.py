def zip_(*args):
    count_arg = len(args)
    # Определяем минимальный список
    len_min_arg = len((sorted(args, key=len)[0]))
    # Переменная, отвечающая за индекс элемента итерируемой последоват.
    el_index = 0
    result = []
    while el_index < len_min_arg:
        obj_el = []
        # Итерируемся по элементу каждой последоват.
        for obj in args:
            obj_el.append(obj[el_index])
        result.append(tuple(obj_el))
        # Увеличиваем индекс элемента
        el_index += 1
    return result

for i in zip_("1234", ["one", "two", "three"]):
    print(i)
