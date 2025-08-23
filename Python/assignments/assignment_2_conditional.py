# Q1) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#  Ask user for their salary and year of service and print the net bonus amount.

user_salary = float(input("enter your salary:" ))
user_yearOf_service = int(input("enter your salary:" ))

if (user_yearOf_service > 5):
    print("your bonus is", user_salary * 0.05)
else:
    print("No bonus, less than or equal to 5 years of service.")


# Q2) 2 Write a program to check whether a person is eligible for voting or not. (accept age from user) 
# if age is greater than 17 eligible otherwise not eligible

age = int(input("please enter your age: "))
if age > 17:
    print("eligible")
else:
    print("not eligible")

# Q3) Write a program to check whether a number entered by user is even or odd.

number = int(input("please enter number: "))
if number %2 == 0:
    print("even")
else:
    print("odd")

# Q4) Write a program to check whether a number is divisible by 7 or not. Show Answer

number = int(input("please enter number: "))
if number %7 == 0:
    print("yes")
else:
    print("no")

# Q5) Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".

number = int(input("please enter number: "))
if number %5 == 0:
    print("Hello")
else:
    print("Bye")

# Q6) Write a program to display the last digit of a number.

number = int(input("please enter number: "))
print("last digit:" , number % 10)

# Q7) Take two int values from user and print greatest among them.

number1 = int(input("please enter number 1: "))
number2 = int(input("please enter number 2: "))
print(number1 if number1 > number2 else number2)

# Q8) Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

length = float(input("enter a length: "))
breadth = float(input("enter a breadth: "))

if length == breadth:
    print("it is square ")
else:
    print("it is rectangle ")

# Q9) A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input("enter a purchased quantity: "))
totalRs = quantity * 100
discount = int(totalRs * 0.10)
if totalRs > 1000:
    print(f"we give you 10% discount : total-price: {totalRs} after discount: {totalRs - discount} ")
else:
    print("your price is:", totalRs)

# Q10) A school has following rules for grading system:
# a. Below 25 - F

# b. 25 to 45 - E

# c. 45 to 50 - D

# d. 50 to 60 - C

# e. 60 to 80 - B

# f. Above 80 - A

marks = int(input("Enter marks of student: "))
if marks < 25 and marks >= 0:
    print("your grade is F")
elif marks >= 25 and marks <= 45:
    print("your grade is E")
elif marks > 45 and marks <= 50:
    print("your grade is D")
elif marks > 50 and marks <= 60:
    print("your grade is C")
elif marks > 60 and marks <= 80:
    print("your grade is B")
elif marks > 80:
    print("your grade is A")
else:       
    print("Invalid marks entered")

# Q12) 14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

classes_held = int(input("no of classes held: "))
classes_attend = int(input("no of classes attend: "))
attend_percentage = int(100 * classes_attend / classes_held)
if attend_percentage > 75:
    print("you are allowed to sit in exam")
else:
    print("you are not allowed to sit in exam")

# Q13) Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

x = input("If you have medical cause Y / N : ")
if x.lower() == "y":
    print("You can sit")
else:
    print("You can not sit")

# Q14) Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

x = int(input("Enter the year : "))
if x % 4 == 0:
    print("This year is leap year")
else:
    print("This is not a leap year")

# Q15) Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR"

age = int(input("Enter your age : "))
gender = input("Enter Your Gender M / F : ")
status = input("Enter you Married Status Y / N : ")

if gender.lower() == "f":
    print("You re onluy work in urban area")
elif gender.lower() == "m" and 20 < age < 40:
    print("You can work in any where")
elif gender.lower() == "m" and  40 <= age <= 60:
    print("You can work in Urban Area")
else:
    print("error")

# Q16) Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
# Unit                                                       Price  
# uptp 100 units                                            no charge
# Next 200 units                                            Rs 5 per unit
# After 200 units                                           Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs.3500
# (For example if input unit is 97 than total bill amount is Rs.0
# (For example if input unit is 150 than total bill amount is Rs.750

unit = int(input("Inter Your Bill unit "))
if unit <= 100 : 
    print("No Bill ")
elif unit <= 300 :
    print(f"The Bill is : RS {unit*5} Only")
else:
    print(f"The Bill is : RS {unit*10} Only")



