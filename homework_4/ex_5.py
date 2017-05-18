# Если объект не итерируемый возвращаем False, в противном случае True
def any_(iterable):
    if isinstance(iterable, (int, float)):
        return False
    else:
        return True

print('int: ', any_(1))
print('float: ', any_(1.0))
print('str: ', any_('sdfasdf'))
print('list: ', any_([1, 2, 4]))
print('tuple: ', any_((1, 23, 34)))
print('dict: ', any_({1: 'asdf', 2: 'sdf'}))
print('set: ', any_({1, 2, 4}))
