# Q1 ( count no of character whose match to vowels characters )

user_input = input("enter any string: ")
vowels = "aeiou"
count = sum(user_input.count(x) for x in vowels)
print(count)

# Q2)  ( check letter count like how much character in word is upper, lower , digit)

user_input = input("Enter a string: ")
uppercase = [ch for ch in user_input if ch.isupper()]
lowercase = [ch for ch in user_input if ch.islower()]
digit = [ch for ch in user_input if ch.isdigit()]
whitespaces = [ch for ch in user_input if ch.isspace()]

print("uppercase", len(uppercase))
print("lowercase", len(lowercase))
print("digit", len(digit))
print("whitespaces", len(whitespaces))

# Q3) 

user_input = input("enter any string: ")
first_cha = user_input[-1]
last_cha = user_input[0]
print(first_cha + user_input[1: -1] + last_cha)

# Q4 reverse the string

user_input = input("enter any string: ")
reverse_userinput = user_input[::-1]
print(reverse_userinput)

# Q5  (input : examination 2021, outout: xamination 2021e)

user_input = input("Enter any string: ")
first_char = user_input[0]
new_string = user_input[1:]  
print(new_string + first_char)

# Q6  (Output A. R. K)

name = input("enter your full name: ")

first_letter_of_name = name[0]+". "
space = name.find(" ")
second_letter_of_name = name[space+1]+". "
new_name = name[:space] + name[space+1:]
space = new_name.find(" ")
third_letter_of_name = new_name[space+1]+"."
print(first_letter_of_name.upper() + second_letter_of_name.upper() + third_letter_of_name.upper())

# Q7 ( Check word is Palindrome or not )

word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q8 ( input SHIFT, Expected OUtput:
# SHIFT
# HIFTS
# IFTSH
# FTSHI
# TSHIF
# SHIFT
# )

word = input("Enter a word: ")
length = len(word)
i = 0
for i in range(0, length+1):
    print(word[i: i+1] + word[i+1:] + word[0: i])
    i += 1