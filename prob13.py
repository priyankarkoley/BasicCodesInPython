num = int(input('Enter the number to check : '))
count = 0
prod = 1
while(num!=0):
    digit = num%10
    prod *= digit
    num=num//10
print("The product of the digits of the number is",prod)