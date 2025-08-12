# 1. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#  Ask user for their salary and year of service and print the net bonus amount.

user_salary = float(input("enter your salary:" ))
user_yearOf_service = int(input("enter your salary:" ))

if (user_yearOf_service > 5):
    print("your bonus is", user_salary * 0.05)
else:
    print("No bonus, less than or equal to 5 years of service.")


# 2 Write a program to check whether a person is eligible for voting or not. (accept age from user) 
# if age is greater than 17 eligible otherwise not eligible

age = int(input("please enter your age: "))
if age > 17:
    print("eligible")
else:
    print("not eligible")

# 3 Write a program to check whether a number entered by user is even or odd.

number = int(input("please enter number: "))
if number %2 == 0:
    print("even")
else:
    print("odd")

# 4 Write a program to check whether a number is divisible by 7 or not. Show Answer

number = int(input("please enter number: "))
if number %7 == 0:
    print("yes")
else:
    print("no")

# 5 Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".

number = int(input("please enter number: "))
if number %5 == 0:
    print("Hello")
else:
    print("Bye")

# 6 Write a program to display the last digit of a number.

number = int(input("please enter number: "))
print("last digit:" , number % 10)

# 7 Take two int values from user and print greatest among them.

number1 = int(input("please enter number 1: "))
number2 = int(input("please enter number 2: "))
print(number1 if number1 > number2 else number2)