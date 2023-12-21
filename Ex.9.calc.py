num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
operator = int(input("Enter 1 to add, 2 to subtract, 3 to multiply and 4 to divide \n1.+\n2.-\n3.×\n4.÷"))

if operator == 1:
	print("Result = ", num1 + num2)
if operator == 2:
	print("Result =", num1 - num2)
if operator == 3:
	print("Result =", num1 * num2)
if operator == 4:
	if num1 == 0 or num2 == 0:
		print("Cannot Divide by zero")
	else:
		print("Result =",num1/num2)
else:
	print("Invalid Operator, Try Again")