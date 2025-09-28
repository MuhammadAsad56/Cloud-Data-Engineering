# Q1 Print 1 to 10 number using for loop 

# for i in range(1, 11):
#     print(i)

# Q2 Print 20 to 1 number using while loop 

# i = 20
# while i >= 1:
#     print(i)
#     i -= 1

# Q3 Print event number 1 to 10 

# for i in range(1, 11):
#     if i %2 == 0:
#         print(i)

# Q4 

# user_number = int(input("enter a number: "))
# for i in range(1, user_number):
#     if i %2 != 0:
#         print(i)

# Q5 print "happy birthday" 5 times on screen

# for i in range(1, 6):
#     print("Happy Birthday")

# Q6

# number = int(input("Enter a number: "))
# print(f"The first {number} terms of the series are: ")
# for temp in range(1, number + 1):
#     print((temp)**2)

# Q7  print table of the given user number

# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{number} * {i} = {number * i}")

# Q8

# x = 3
# lst = []
# for i in range(1, 9):
#     lst.append(str(x))
#     x += 4
# print(" ".join(lst))

customers = [
{
"customer id": 0,
"first name":"John",
"last name": "Ogden",
"address": "301 Arbor Rd.",
},
{
"customer id": 1,
"first name":"Ann",
"last name": "Sattermyer",
"address": "PO Box 1145",
},
{
"customer id": 2,
"first name":"Jill",
"last name": "Somers",
"address": "3 Main St.",
},
]
print(customers)

# customers = [{**cus, "age" : None} for cus in customers]

lst = [{value['customer id']: value} for value in customers]
print(lst[0][0])
# for dict in custom ers:
#     dict.setdefault("age")

# i = 0
# for dict in customers:
#     customers[i] = list(dict.values())
#     i += 1

# print(customers)

# obj = {
# "customer id": 0,
# "first name":"John",
# "last name": "Ogden",
# "address": "301 Arbor Rd.",
# }

# obj2 = {**obj}
# obj2.pop("first name")
# print(obj)
# print(obj2)






# print(customers)

# def greet(message):
#     return message

# my_var = greet("hi")
# print(my_var)
    



