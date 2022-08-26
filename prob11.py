a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the second number"))
if(c<(a+b)):
    print("Triangle not possible.")
elif(a<(c+b)):
    print("Triangle not possible.")
elif(b<(a+c)):
    print("Triangle not possible.")
elif((a==b) and (b==c)):
    print("The triangle is EQUI-LATERAL.")
elif((a==b)or(b==c)or(c==a)):
    print("The triangle is ISOSCELES.")
elif((a!=b) and (b!=c) and (c!=a)):
    print("The triangle is  SCALENE.")