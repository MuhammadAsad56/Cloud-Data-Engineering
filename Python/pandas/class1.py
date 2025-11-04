import pandas as pd

df = pd.read_csv('./bricks.csv' , index_col=0)
# print(df)

#          country    capital    area  population
# BR        Brazil   Brasilia   8.516      200.40
# RU        Russia     Moscow  17.100      143.50
# IN         India  New Delhi   3.286     1252.00
# CH         China    Beijing   9.597     1357.00
# SA  South Africa   Pretoria   1.221       52.98


#                                           ( loc ) mehod working on index names


# rows sari liao columns country and area lao 
# print(df.loc[:, ['country','area']])


# rows sari columns country se area tak 
# print(df.loc[:, 'country': 'area'])
#          country    area
# BR        Brazil   8.516
# RU        Russia  17.100
# IN         India   3.286
# CH         China   9.597
# SA  South Africa   1.221


# RU CH ye do index wali rows lekar aou aur column population lao 
# russia = df.loc[['RU', 'CH'],['population']]
# print(russia)


# BR se CH tak ki index wali rows liao aur column area se population tak
# print(df.loc['BR' : 'CH', 'area' : 'population'])
#       area  population
# BR   8.516       200.4
# RU  17.100       143.5
# IN   3.286      1252.0
# CH   9.597      1357.0



#                                      ( iloc ) method working on indexes of dataframs


# print(df.iloc[[0,1,2,3], [3]])
#     population
# BR       200.4
# RU       143.5
# IN      1252.0
# CH      1357.0


# rows sari column second index wala 
# print(df.iloc[:, [2]])
#       area
# BR   8.516
# RU  17.100
# IN   3.286
# CH   9.597
# SA   1.221


# print(df.iloc[:, : ])
# guess the answer 


# print(df.iloc[:, 1: 3])
#       capital    area
# BR   Brasilia   8.516
# RU     Moscow  17.100
# IN  New Delhi   3.286
# CH    Beijing   9.597
# SA   Pretoria   1.221



#                                              DATAFRAMES AND AGGREGATING DATA 


titanic = pd.read_csv('./titanic.csv')
# print(titanic) 

# print(titanic.info())



# print(titanic.describe())
#        PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
# count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
# mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
# std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
# min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
# 25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
# 50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
# 75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
# max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200


#                            Explanation   What Each Row Means:
#   Statistic	                     Meaning
# count	                     Number of non-null entries
# mean	                     Average value
# std	                     Standard deviation (spread of data)
# min	                     Minimum value
# 25%	                     1st quartile (25% of data is below this)
# 50%	                     Median (middle value)
# 75%	                     3rd quartile (75% of data is below this)
# max	                     Maximum value



# try:
#     sum = titanic['sum'] = titanic.select_dtypes(include=['number']).sum(axis=1)
# except ValueError:
#     print("nisiis")
# print(titanic)


# print(titanic.sort_values(["Survived", "Sex"], ascending=[False, True]))


# print(titanic.Sex == "male")
# 0       True
# 1      False
# 2      False
# 3      False
# 4       True
#        ...
# 886     True
# 887    False
# 888    False
# 889     True
# 890     True
# Name: Sex, Length: 891, dtype: bool


# print(titanic[titanic.Sex == "male"])
# sari wo rows layega jime sex male hoga


#                                                  task


# age_less_20 = titanic[(titanic.Age < 20) & (titanic.Sex == "male")]
# asscending_order = age_less_20.sort_values("Age" , ascending=True)
# print(asscending_order[['Name', "Age", "Sex"]].head(10))
#                                 Name   Age   Sex
# 803  Thomas, Master. Assad Alexander  0.42  male
# 755        Hamalainen, Master. Viljo  0.67  male
# 831  Richards, Master. George Sibley  0.83  male
# 78     Caldwell, Master. Alden Gates  0.83  male
# 305   Allison, Master. Hudson Trevor  0.92  male
# 386  Goodwin, Master. Sidney Leonard  1.00  male
# 164     Panula, Master. Eino Viljami  1.00  male
# 183        Becker, Master. Richard F  1.00  male
# 827            Mallet, Master. Andre  1.00  male
# 788       Dean, Master. Bertram Vere  1.00  male


#                                                task end


# print(titanic[["Pclass"]].head(20))
# print(titanic.drop_duplicates(subset='Pclass').sort_values('Pclass' , ascending=True).head(20))


# print(titanic['Age'].value_counts())
#        count
# Age
# 24.00     30
# 22.00     27
# 18.00     26
# 19.00     25
# 28.00     25
# ...      ...
# 36.50      1
# 55.50      1
# 0.92       1
# 23.50      1
# 74.00      1


# print(titanic[titanic['Sex']=='male'].Age.mean())

# print(titanic[['Age']].value_counts(sort=True))
# Age  
# 24.00    30
# 22.00    27
# 18.00    26
# 30.00    25
# 28.00    25
#          ..
# 20.50     1
# 14.50     1
# 12.00     1
# 0.92      1
# 80.00     1
# Name: count, Length: 88, dtype: int


#                                              GROUPPING SUMMARY



# print(titanic.groupby('Sex')[['Age']].max())
#          Age
# Sex
# female  63.0
# male    80.0


# print(titanic.groupby(['Sex', 'Survived']).Age.count())

#                                              Example:
# Name	  Sex	    Age	  Survived
# Anna	female	    22	      1
# Mary	female	    NaN	      1
# Sara	female	    30	      0
# Emma	female	    NaN	      0

# Ab dekho:

# Group	Description	Rows Counted by .Age.count()
# female, survived (1)	Anna (22), Mary (NaN)	✅ 1 (Anna only)
# female, died (0)	Sara (30), Emma (NaN)	✅ 1 (Sara only)


# print(titanic.groupby('Sex').Age.count())
# Sex
# female    261
# male      453
# Name: Age, dtype: int64



# print(titanic.groupby(['Survived', 'Sex'])[['Age']].agg(['count', 'min', 'max']))

#                         Age
#                    count   min   max
# Survived   Sex
# 0         female    64  2.00  57.0
#           male     360  1.00  74.0
# 1         female   197  0.75  63.0
#           male      93  0.42  80.0


#                                          PIVOTS TABLE  same as grouping


# print(titanic.groupby('Sex')[['Age']].mean())
# print(titanic.pivot_table(values='Age', index='Sex')) 
#               Age
# Sex
# female  27.915709
# male    30.726645

# output same ayega but pivot_table by-default mean calculate karta he



# print(titanic.pivot_table(values='Age', index='Sex', columns='Survived'))
# Survived          0          1
# Sex
# female    25.046875  28.847716
# male      31.618056  27.276022

# print(titanic.pivot_table(values='Age',index='Sex', aggfunc=['count', 'min', 'max']))

