num = int(input('Enter the number to check : '))
n = num
count = 0
while(num!=0):
    num=num//10
    count += 1
if(count == 3):
    print(n,"is a 3 digit Number")
else:
    print(n,"is not a 3 digit Number")