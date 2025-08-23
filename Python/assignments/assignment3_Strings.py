# Q1

user_input = input("enter any string: ")
vowels = "aeiou"
count = sum(user_input.count(x) for x in vowels)
print(count)

# Q2)

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

# Q5

user_input = input("Enter any string: ")
first_char = user_input[0]
new_string = user_input[1:]  
print(new_string + first_char)