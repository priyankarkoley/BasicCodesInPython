str = input("Enter the String: ")
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
for letter in str:
    if(letter not in upper):
        count = count + 1
print("The number of lowercasse characters in the string is:", count)