import pandas as pd
import matplotlib.pyplot as plt


titanic = pd.read_csv("./titanic.csv")

# 
# print(titanic)

titanic.head()

# print(titanic.drop_duplicates(subset="Pclass"))

# print(pd.DataFrame(titanic['Age'].value_counts()))


# group-by 


# print(pd.DataFrame(titanic.groupby(['Survived', 'Sex'])['Age'].count()))

# result 
#                  Age
# Survived Sex
# 0        female   64
#          male    360
# 1        female  197
#          male     93


# print(titanic.groupby('Sex')['Age'].count())

# result 
# Sex
# female    261
# male      453
# Name: Age, dtype: int64


# print(titanic.groupby('Sex')['Age'].agg(['count' , 'min' , 'max']))

# result  
#         count   min   max
# Sex
# female    261  0.75  63.0
# male      453  0.42  80.0


# print(titanic.groupby(['Survived', 'Sex'])['Age'])


# print(titanic.pivot_table(values='Age', index='Sex', ))

# titanic.plot(x='Age', y='PassengerId' , kind='scatter')
# plt.show()

# titanic.isna().sum().plot(kind='bar')
# plt.show()


list_of_dictionary = [
    {'name':'Ginger',
     'breed': 'lusi',
     'height_cm': 22,
     'weight_kgs':10 ,
     'date_of_birth':"2020-02-14"},
    
    { 'name': 'Scout',
     'breed': 'Dalmatian',
     'height_cm': 59,
     'weight_kgs':35 ,
     'date_of_birth':"2019-05-09"}
]

dogs = pd.read_csv(r"C:\Users\HP\Desktop\Cloud-Data-Engineering\Python\pandas/dogs.csv")
print(dogs)



