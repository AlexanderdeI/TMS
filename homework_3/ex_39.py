import time

print('''Calculator Menu
1. Quit
2. Add two numbers
3. Subtract two numbers
4. Multiply two numbers
5. Divide two numbers 
''')
time.sleep(1)
print("Enter two numbers and choose number of operation")
time.sleep(1)

first_num = float(input("First number: "))
second_num = float(input("Second number: "))
operation = int(input("Operation: "))

if operation == 1:
	exit()
elif operation == 2:
	sum_n = first_num + second_num
	print(f'Result: {sum_n}')
elif operation == 3:
	sub_n = first_num - second_num
	print(f'Result: {sub_n}')
elif operation == 4:
	mult_n = first_num * second_num
	print(f'Result: {mult_n}')
elif operation == 5:
	div_n = first_num / second_num
	print(f'Result: {div_n}')
else:
	print('Wrong number of operation')
	exit()


