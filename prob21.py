str = input("Enter a string: ")
i = int(input("Enter the value of i: "))
new_s= str[:i-1]+str[i:]
print("The converted string is: \n",new_s)