# LOOPS 

# i = 5
# for i in range(0, i):
#     print("happy Birthday")


# i = ["asad",1,2]
# for i in i:
#     print(i)

#  task  table print 

# number = int(input("enter a number: "))
# for i in range(1, 11): 
#   print(f" {number} * {i} = {number * i}")

#  task:  print start to end table

# start  = int(input("enter a starting numner"))
# end  = int(input("enter a ending numner"))
# length = 11
# for i in range(start,end):
#     for j in range(1,length):
#         print(f"{i} * {j} = {start * j}")
#     length -= 1


# list comprehension

lst = ["even" if i%2 == 0 else "odd"  for i in range(1,21)]
print(lst)
