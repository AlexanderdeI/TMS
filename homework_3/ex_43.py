import random as r

l = []
for i in range(10):
	a = r.randint(1, 10)
	l.append(a)
print(l)

max_value = l[0]
	
for i in l[1:]:
	if i > max_value:
		max_value = i

print(max_value)
