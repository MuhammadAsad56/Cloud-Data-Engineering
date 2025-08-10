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

text = "hello world"
print(text.find("o"))  # Output: 6

# array = [1, 2]
# print(array.pop(1))


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

original = ["asd", [["salman"]]]
shallow = original.copy()  # or copy.copy(original)

shallow[1][0] = "no"
print(original, shallow)
