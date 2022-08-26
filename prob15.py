a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))
for i in range(a,b+1):
    j = 1
    count = 0
    while(j<i):
        if(i%j==0):
            count += 1
        j += 1
    if(count<=1):
        print(i, end = "\t")