# match case -> simplified if statement 
a = 2
if a == 0: print('0')
elif a == 1: print('1')
elif a == 2: print('2')
elif a == 3: print('3')

match a:
	case 0: print('0')
	case 1: print('1')
	case 2: print('2')
	case 3: print('3')

# ternary operator / single line if statement 
day_time = False
greet = 'hello' if day_time else 'goodbye'
print(f"Somthing basic: {'hello' if day_time else 'goodbye'}")

# chain comparisons 
min_value = 5
max_value = 10
value = 7

#if min_value < value and max_value > value:
if min_value < value < max_value:
	print('value inside boundaries')

# clamp some values between a minimum and a maximum
min_value = 0
max_value = 100
value = 50

# while True:
# 	value += 0.001
# 	# value never exceeds maximum value
# 	# if value > max_value:
# 	# 	value = max_value
# 	# if value < min_value:
# 	# 	value = min_value
# 	value = max(min_value,min(value,max_value))
# 	print(value)

# eval + exec 
test_string = 'hello'
print(eval('test_string.upper()'))
print(exec('test_string = "updated"'))
print(test_string)

for operation in ['upper', 'lower', 'casefold', 'title']:
	print(eval(f'test_string.{operation}()'))

# print(test_string.upper())
# print(test_string.lower())
# print(test_string.casefold())
# print(test_string.title())

# dict.get
test_dict = {'a': 1, 'b': 2, 'c' : 3}
if test_dict.get('a'):
	print(test_dict.get('a'))

# list flattening with sum()
test_list = [[1, 2, 3], [4, 5, 6, 7], [8 , 9]]
print(sum(test_list,[]))