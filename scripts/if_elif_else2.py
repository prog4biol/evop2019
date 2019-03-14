#!/usr/bin/env python3

count = 20
if count < 0:
  message = "is less than 0"
elif count < 50:
  message = "is less than 50"
elif count > 50:
  message = "is greater than 50"
else:
  message = "must be 50"
  
print(count, message)
