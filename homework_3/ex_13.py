list_nums = [2, 4, 5, 6, 4, 3, 5, 6, 7, 3, 5, 6, 3, 2, 1]

for el in list_nums:
	if el == el:
		index = list_nums.index(el)
		list_nums.remove(index)
		

l_without_dubl = list_nums 


print(list_nums)
print(l_without_dubl)
