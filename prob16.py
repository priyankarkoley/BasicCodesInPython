n = int(input('Enter the number to check Palindrome: '))
num = n
count = 0
prod = 1
rev = 0
while(num!=0):
    digit = num%10
    rev = (rev*10) + digit
    num=num//10
if(n == rev):
    print("The number is Palindrome.")
else:
    print("The number is not Palindrome.")