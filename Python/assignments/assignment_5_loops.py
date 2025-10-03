# Q1 Print 1 to 10 number using for loop 

for i in range(1, 11):
    print(i)

# Q2 Print 20 to 1 number using while loop 

i = 20
while i >= 1:
    print(i)
    i -= 1

# Q3 Print event number 1 to 10 

for i in range(1, 11):
    if i %2 == 0:
        print(i)

# Q4 

user_number = int(input("enter a number: "))
for i in range(1, user_number):
    if i %2 != 0:
        print(i)
        

# Q5 print "happy birthday" 5 times on screen


for i in range(1, 6):
    print("Happy Birthday")


# Q6

number = int(input("Enter a number: "))
print(f"The first {number} terms of the series are: ")
for temp in range(1, number + 1):
    print((temp)**2)

# Q7  print table of the given user number

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")


# Q8  print first 8 terms of an arithmatic progression starting with 3 and having a common difference of 4

x = 3
lst = []
for i in range(1, 9):
    lst.append(str(x))
    x += 4
print(" ".join(lst))


# Q9  print first 6 terms of geometric sequence starting with 2 and having a common ratio of 3

x = 2
lst = []
for i in range(1, 7):
    lst.append(str(2) if i == 1 else str(x * 3))
    x = 2 if i == 1 else x * 3
print(" ".join(lst))


# Q10 Ask user to enter a positive number and the program should calculate the sum of 1 to given user nunber

userNumber = int(input("enter a number: " ))
x = 0
for i in range (1, userNumber + 1):
    x += i
print("sum of the number: ", x)




