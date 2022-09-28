a = int(input("Enter the first side"))
b = int(input("Enter the second side"))
c = int(input("Enter the third side"))
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