object = {
    "firstName" : "asad",
    "lastName" : "raza",
    "age" : "21"
}

print(object["age"])
print(object.get("age"))
print(object.pop("age"))   # delete value against given key and return deleted value
print(object.get("age"))   #  result None

print(object.setdefault("age" , "31")) # add value in object against given key and return value
print(object)  # result {'firstName': 'asad', 'lastName': 'raza', 'DOB': '11 september'}

print(object.update({"salary" : 30000}))
print(object)  # result {'firstName': 'asad', 'lastName': 'raza', 'DOB': '11 september'}
