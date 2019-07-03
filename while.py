'''

def sum_of_numbers(until_number):
	a=1
	b=2
	count=1
	while count<=until_number:
		count=count+1
		c=a+b
		a=c
		b=b+1
	return c
print sum_of_numbers(3)

'''

while True:				#infinite loop
	print "abc"



while True:
	print "abc"
	break


count = 0
while count<100:
	count+=1
	print count