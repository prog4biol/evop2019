#!/usr/bin/env python3
import sys
count = int(sys.argv[1])

if count < 0:
	message1 = "negative number"
	message2 = ""
elif count > 0:
	message1 = "positive number"

	if count < 50:
		if count%2 == 0:
			message2= "Even number"
		else:
			message2= 'Odd number'
	if count > 50:
		if count%3 == 0:
			message2 ='Divisible by 3.'
		else: 
			message2 = 'Not divisible by 3'
	else:
		message2 = 'Your number must be 50.'
print(count, message1, message2)
