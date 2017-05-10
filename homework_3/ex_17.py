list_nums = [1234, 34 ,784, 654, 78, 4]
len_list = len(list_nums)

nums = []

while len(nums) < len_list:
	for el in list_nums:
		el = str(el)
		nums.append(el)
	nums = (" ".join(nums)).replace("", "|")
	print(nums)
