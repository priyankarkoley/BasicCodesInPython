num = int(input("Enter the number to calculate factorial: "))

fact = 1
for i in range(1,num+1):
	fact = fact * i
	
print ("The factorial of the number is: ",fact)