object = {
    "firstName" : "asad",
    "lastName" : "raza",
    "age" : "21"
}

print(object["age"])
# print(object.get("age"))
# print(object.pop("age"))   # delete value against given key and return deleted value
# print(object.get("age"))   #  result None

# print(object.setdefault("age" , "31")) # add bydefault value in object if originall object not have this value so by default add this value 
# print(object)  # result {'firstName': 'asad', 'lastName': 'raza', 'DOB': '11 september'}

# print(object.update({"salary" : 30000})) # return None
# print(object)  # result {'firstName': 'asad', 'lastName': 'raza', 'age': '21', 'salary': 30000}


# Dictionary Comprehension

result = {"Ali":80,"Muhammad":89,"Usama":69,"Asad":56}
passed = [name for name,value in result.items() if value >= 70]
print(f"Congratulations all these students you are passed {passed}")
# result Congratulations all these students you are passed ['Ali', 'Muhammad']

result = [{"name" : "asad", "marks":80},{"name": "Muhammad", "marks":89},{"name":"Usama", "marks":69},{"name" : "salmnan", "marks":56}]
passed = [{"name": name["name"], "Roll-No" : "211"} for name in result if name["marks"] >= 70]
print(f"Congratulations all these students you are passed {passed}")
# result Congratulations all these students you are passed [{'name': 'asad', 'Roll-No': '211'}, {'name': 'Muhammad', 'Roll-No': '211'}]