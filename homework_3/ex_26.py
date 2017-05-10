import random as r

dice = ['one', 'two', 'three', 'four', 'five', 'six']
n = 100000
results = {}

for throw in range(n):
	side = r.choice(dice)
	if side not in results:
		results[side] = 0
	results[side] += 1

print(results)
		
		
	
	
	
