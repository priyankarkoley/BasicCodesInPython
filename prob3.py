str = input("Enter the String: ")
vowel = "aeiouAEIOU"
count = 0
for letter in str:
    if(letter in vowel):
        count = count + 1
print("The number of vowels in the string is:", count)