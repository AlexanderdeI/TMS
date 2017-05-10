list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = ['one', 'two', 'three', 'four', 'five',
         'six', 'seven', 'eight', 'nine', 'ten']

for num,word in zip(list1, list2):
	print(f'{num:>2d} : {word}')
