# # Q1 

# user_input = input("Enter elements of list separated by space: ")
# my_list = user_input.split()
# alternate_elements = my_list[::2]

# print("Alternate elements are:", alternate_elements)

# # Q2 ( reverse the content of list )

# lst = [10, 29, 39 ,40]
# reversed_list = lst[::-1]
# print(reversed_list)

# # Q3

# user_input = input("Enter elements of list separated by space: ")

# lst = user_input.split()
# new_list = []
# for ele in lst:
#     new_list.append(int(ele))

# maximum = sorted(new_list)
# print(maximum)

# # Q4 

# lst = [1,2,3,4,5]
# i = 0
# new_lst = []
# while i < len(lst) -1:
#     pre = lst[i]        # 1 1
#     lst[i] = lst[i+1]  # [2,3,3,4,5]
#     lst[i+1] = pre     # [2,1,1,4,5]
#     i += 1

# # print(lst)

# # Q5  ( if user_input is 'o' output will become : 'gd day brther')

# word = "good day brother"
# user_input = input("enter element of that you want to delete in this word ' good day brother' : \n")

# remove_space = [cha for cha in word if cha != " "]
# new_word = "".join(remove_space)
# remove_element = new_word.find(user_input)
# if remove_element != -1:
#     output = word.replace(user_input, "")
#     print(output)
# else:
#     print("please enter a valid element")
     
# # Q6: Convert mm/dd/yyyy to "Month dd, yyyy"

# months = ["January", "February", "March", "April", "May", "June", 
#           "July", "August", "September", "October", "November", "December"]

# date_str = input("Enter date in mm/dd/yyyy format e.g. 03/12/2021: ")
# date_format = date_str.split("/")

# # separate month days and year from user input
# mm = date_format[0]
# dd = date_format[1]
# yyyy = date_format[2]

# mm = int(mm)
# dd = int(dd)

# print(f"{months[mm-1]} {dd}, {yyyy}")

# # Q7: Capitalize each word in string


# def capitalize_words(sentence):
#     words = sentence.split(" ")
#     for i in range(0, len(words)):
#         lst = []
#         for word in words[i]: 
#             lst.append(word.capitalize())
#         words[i] = "".join(lst)
#     return words



# sentence = input("Enter a sentence: ")
# print("Converted:", capitalize_words(sentence))


# # Q8: Sum of each row in matrix

# matrix = [
#     [2, 11, 7, 12],
#     [5, 2, 9, 15],
#     [8, 3, 10, 42]
# ]

# for i, row in enumerate(matrix):
#     print(f"Sum of row { i+ 1 } = {sum(row)}")


# Q9: Add two matrices

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

result = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Matrix Addition Result:")
for r in result:
    print(r)






 