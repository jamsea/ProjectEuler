def is_palindrome(num):
	num_str = str(num)
	if(num_str == num_str[::-1]): return True
	return False

largest_palindrome = 0
num = 0

for i in range(999, 1, -1):
	for j in range(999, 1, -1):
		num = i*j
		if(is_palindrome(num) and num > largest_palindrome):
			largest_palindrome= num

print(largest_palindrome)
