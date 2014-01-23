# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def fib(x):
	if(x==1 or x == 2):
		return x
	else:
		return fib(x-1) + fib(x-2)

even_fib = [fib(x) for x in range (0,5) if (fib(x) < 4000000 and fib(x) % 2 ==0)] 
print even_fib
