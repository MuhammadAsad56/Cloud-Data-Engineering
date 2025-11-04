# firstname = input("Enter your first name: ")
# middleNmae = input("Enter your middle name: ")
# lastname = input("Enter your last name: ")

import copy
# print("Name:", name)
# print("Age:", age)
# print("firstname:" + firstname + "  MiddleName "  + middleNmae + " " + "LastName:" + lastname)
# print (f"Name: {firstname}, MiddleName: {middleNmae} LastName: {lastname}")

# formatMethod = "FirstName: {0} middleNmae: {2} LastName: {1}".format(firstname, lastname , middleNmae)

# print(formatMethod) 

# marks = int(input("Enter marks of student: "))
# if age % 5 == 0: 
#     print("your number is even")
# else:
#     print("your number is odd")

# if marks < 25 and marks >= 0:
#     print("your grade is F")
# elif marks >= 25 and marks <= 45:
#     print("your grade is E")
# elif marks > 45 and marks <= 50:
#     print("your grade is D")
# elif marks > 50 and marks <= 60:
#     print("your grade is C")
# elif marks > 60 and marks <= 80:
#     print("your grade is B")
# elif marks > 80:
#     print("your grade is A")
# else:       
#     print("Invalid marks entered")


# string methods: 
# name = "John Doe"

# print(name.count("o")) 
#  o ko count karega kitne times he naem variable me 

# name = name.replace("Doe", "Mon")# replace method se string ko replace karte hai
# print(name)

# text = "hello world"
# print(text.find("o"))  # Output: 4 returns index value of character if not find return -1

# array = [1, 2, 6, "asad"]
# print(array.pop(3))


# shallow copy
# array = [1, 2]
# new_array = array.copy()
# new_array[1] = 7
# print(array, new_array)


# deep copy
# array = [1, 2]
# new_array = array
# new_array[1] = {"b" : "asad"}
# print(array[1].get("a"), new_array)

# index method

# list_item = ["asad", "raza", 5, True]
# a = list_item.index("asad")
# print(a) # index method index number return karta he agar wo item list me hoga nahi hoga to error return karta he ValueError: 'l' is not in list

# append method

list_item = ["asad", "raza", 5, True]
# a = list_item.append("good")
# print(a) # append method return null karta he but jo bhi hum isko value denge wo list ke end me add krdega.
# note: agar isko list denge to same list ko end me add kardeg like this:
# a = list_item.append([0,8])
# result: ['asad', 'raza', 5, True, [0, 8]]
# print(list_item)

# extend method

# list_item = ["asad", "raza", 5, True]
# a = list_item.extend(["asad"])
# result: ['asad', 'raza', 5, True, 'asad']
# extend method accepts collection of values agar ap isko single value me doge like this:
# a = list_item.extend("asad")
# result : ['asad', 'raza', 5, True, 'asad', 'a', 's', 'a', 'd']
# print(list_item)


# Tuple 
# bio_data = ["asad", "araza"]
# bio_data_t = tuple(bio_data)
# tuple apni state ko preserve karleta he means hum bio_data_t me koi change ya delete nahi kar sakte
# bio_data[0] = "khan"
# print(bio_data)

# original = ["asd", [["salman"]]]
# shallow = original.copy()  # or copy.copy(original)

# shallow[1][0] = "no"
# print(original, shallow)

# user registration and login functionality

# first_name = input("enter a name: ")
# email = input("enter a email: ")
# password = input("enter a password: ")

# lst = []

# def registration(name, email, password):
#     if not name or not email or not password:
#         print("these are required")
#     lst.append({
#         "first_name" : name,
#         "email" : email,
#         "password" : password,
#     })


# registration(first_name, email, password)

# login_email = input("enter a login email:" )
# login_password = input("enter a login pass:" )

# def login (email, password):
#     check = [data for data in lst if data["email"] == email and data["password"] == password]
#     if len(check) >= 1:
#         print("your are welcome ")
#     else:
#         print("something went wrong")
# login(login_email, login_password) 


# def func (num1,num2, *args):    
#     print(args)
#     return num1 + num2 
# print(func(21, 21, 5,6,7))

# obj1 = {"a" : 1 , "b" : {"c" : {"d" : 4}}}
# obj2 = {**obj1}
# obj2["b"]["c"] = {"e" : 3}
# print(obj1)
# print(obj2)

    # lst = list(num2)
    # sum = 0
    # for i in lst:
    #     sum += i

    # print(sum)

# def add_sum(name, **num2):
#     # print(name)

#     # first method
#     # print(sum(num2))

#     # second method
#     # sum = 0
#     # for i in num2:
#     #     sum += i

#     sum = 0
#     for key, value in num2.items():
#         print(value) 



# add_sum("asad", num1=2,num2=3)

# num = int(input("enter number \n"))
# i =0
# while num > 0:
#     print("good")
#     num -= 1


# my_customers = {
#     {  
#         "customer id": 0,
#         "first name":"John",
#         "last name": "Ogden",
#         "address": "301 Arbor Rd.",
#     },
#     {
#         "customer id": 1,
#         "first name":"Ann",
#         "last name": "Sattermyer",
#         "address": "PO Box 1145",
#     },
#     {
#         "customer id": 2,
#         "first name":"Jill",
#         "last name": "Somers",
#         "address": "3 Main St.",
#     },
# }

# print(my_customers)

# class Employee:
#     lan = "eng"
#     salary = "120000"

#     def greet(self):
#         print(f"Hello Welcome {self.salary}")

# asad = Employee()
# Employee

# advance function 

# map_obj = map(lambda x: x, range(1, 6))

# map_obj = filter(lambda x: x[1] > 50 , [("asad" , 78) ,("ali", 40), ("dani", 90)])
# print(map_obj)

# map_obj = sum(filter(lambda x: x <= 5 , range(1, 16)))
# print(map_obj) # result 15



# students = [
#     {"name": "asad", "marks": 78},
#     {"name": "ali", "marks": 40},
#     {"name": "dani", "marks": 90}
# ]

# # with filter method
# filtered = list(filter(lambda x: x["marks"] > 50, students))
# print(filtered)

# # with list comprehension
# map_obj = [{s["name"]: s["marks"]} for s in students if s["marks"] > 50]
# print(map_obj)



# oop (object oriented programming)

# class Student:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#         self.courses = []  # list of courses student ne liye

#     def enroll_course(self, course):
#         self.courses.append(course)


# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject
#         self.students = []  # teacher ke pass students ki list

#     def assign_student(self, student):
#         self.students.append(student)


# class Course:
#     def __init__(self, title):
#         self.title = title

# # courses
# c1 = Course("Python")
# c2 = Course("java")


# # students
# s1 = Student("salman" , "101")
# s2 = Student("agha" , "102")
# s1.enroll_course(c1.title)
# s2.enroll_course(c1.title)

# # teachers
# t1 = Teacher("asad", "Python")

# 1st pilar Inheritence

# class father():
#     eye_color = "brown"
#     hair_color = "black"
        
#     def can_paint(self): #methods
#         return "have ability to draw/paint arts"

# class mother():
#     drive = "car"
        
#     def driving(self):
#         return f"mother has a skill of {self.drive} driving"

# class Child(father,mother):
#     def __init__(self, language):
#         self.programming = language

#     def can_sing(self):
#         print(f"he is a good programmer in {self.programming} Child Can sing as well and his father {self.can_paint()} and his {self.driving()}.")


# child_obj = Child('Python programming')
# print(child_obj.programming)
# print(child_obj.can_sing())

# Overriding

# class Animals():
#     def eating(self):
#         print("Animals can eat")

# a1 = Animals()

# class Birds(Animals):
#     def eating(self): # overriding methods
#         print("Birds can eat")

# b1 = Birds()
# b1.eating()
# a1.eating()

# abstract class ( abstract classes concept )

# class shapes():

#     # abstract method ( means comment add kardiya developers ki readability )
#     def sides(self):
#         pass

# class Square(shapes):

#     # functionality here
#     def sides(self):
#         print("Square has 4 slides")

# sq = Square()

# class Circle(shapes):

#     # functionality here
#     def sides(self):
#         print("Circle has 2 slides")

# cr = Circle()
# cr.sides()


# Encapsulation Concepts ( hides )

# class Saylani():
#     def __init__(self):
#         self.helpline = "211" # public
#         self._batch = "python" # protected
#         self.__result = "70%" # private

# say_obj = Saylani()

# print(say_obj)


# print(say_obj._Saylani__result)  # private property ko get karne ka tariqa


# make login system with private attributes and methods
# def checklogin(name, password):
#     if stu_obj._StudentLogin__name == name and stu_obj._StudentLogin__password == password:
#         return print(f"you are valid user")
#     else:
#         return print("invalid credentials")
    

# class StudentLogin():
#     def __init__(self, name ,password):
#         self.__name = name 
#         self.__password = password 
    
#     def loginCheck(self, name, password):
#         return checklogin(name, password)

        
# stu_obj = StudentLogin("asad", 1234)
    
# stu_obj.loginCheck("asad", 1234)


# Data Files ( files operation read write )

# method_1 we need to close the file after operation
# f = open("file.py", "w")
# f.write(" # this is the files concept file in python")
# f.close()

# # method_2 automatically close the file 
# with open("filw.txt", "w") as f:
#     f.write("this will automatically close the file")

# with open("filw.txt", "a") as f:
#     f.write(" this will append on previous text")

# with open("filw.txt") as f:
#     file_conyent = f.read()

# print(file_conyent)



# class Person:
#     def __init__(self, name, dob):
#         self.name = name
#         # dob format: "YYYY-MM-DD"
#         year, month, day = dob.split("-")
#         self.birth_year = int(year)
#         self.birth_month = int(month)
#         self.birth_day = int(day)

#     def calculate_age(self, today_year, today_month, today_day):
#         age = today_year - self.birth_year if today_day >= self.birth_day else today_year - self.birth_year-1
#         days = today_day - self.birth_day 
#         return f"your are {age} years old {"wohoo your birthday is coming only " + str(days).split("-")[1] + " days left" if today_month == self.birth_month and days < 0 else ""}"


# # Example usage
# p1 = Person("Asad", "2002-09-11")

# # suppose today's date is 2025-09-08
# print(f"Name: {p1.name}")
# print(f"Age: {p1.calculate_age(2025, 9, 11)}")





# CSV HANdling


import csv 
# years = []
# event = []
# winner = []

# competitions = []
# with open('./competitions.csv', "r") as f:
#     content = csv.reader(f)
#     for line in content:
#         competitions.append(line)

# for row in competitions[1:]:
#         print(row)
        # years.append(row[0])
        # event.append(row[1])
        # winner.append(row[2])

# print(years, event, winner)


# with open('./competitions.csv', "a") as f:
#      data_handler = csv.writer(f)
#      data_handler.writerow(["2012","Asia Cup","Pakistan"])




# JSON Handling

import json


# Step 1: Read existing JSON file
# with open("./competitions.json", "r") as f:
#     data = json.load(f)
#     data[-1] = {**data[-1], "unit": "kg"}


# Step 3: Write back updated JSON
# with open("./competitions.json", "w") as f:
#     json.dump(data, f,)
#     print(data)


