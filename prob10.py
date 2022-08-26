a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
if(a<b):
    print(a,"is the lowest of the two numbers entered.")
elif(b<a):
    print(b,"is the lowest of the two numbers entered.")
else:
    print(a,"and",b,"are equal.")