str = input("Enter a string: ")
fact = 1
for i in range(1,len(str)+1):
	fact = fact * i
print ("The number of permutations possible is: ",fact)