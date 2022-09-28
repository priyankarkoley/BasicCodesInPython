str = input("Enter a string: ")
list = str.split(" ")
for word in list:
    if(len(word)%2==0):
        print(word)