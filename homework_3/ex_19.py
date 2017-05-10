l = ['abc', 'bcd', 'def', 'lok', 'put', 'throw']
new_l = []
start = 0
step  = 3
temp_l = []

while len(new_l) < len(l) / step:
	for el in l:
		print(el)
		temp_l.append(el)
		temp_l = "".join(temp_l)
		new_l.append(temp_l)
		start += step
		step += step

print(new_l)
		
		
	
	
