def is_power(x,y):
	if (x == y):
		return True
	if (y == 0) or (y == 1):     #Exception Handling
		return False
    # Recursive
	return ((x%y)==0) and (is_power(x/y,y))  #Includes is_divisible function

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))


