word_dict = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
	'zero' : '0'
}
str = input("Enter a string: ")
res=""
for ele in str.split(" "):
    res += word_dict[ele]
print("The decoded number is: " + res)