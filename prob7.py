num = int(input("Enter the number to check: "))
last_digit = num%10
if(last_digit%3 == 0):
    print("It is divisible by 3")
else:
    print("It is not divisible by 3")