n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j, end="  ")
    print("\n")