import pandas as pd


employees = {
    'Emp_ID': range(1001, 1021),
    'Name': [
        'Ali', 'Sara', 'Umer', 'Hina', 'Bilal', 'Ayesha', 'Raza', 'Mona', 'Danish', 'Tuba',
        'Kashif', 'Iqra', 'Ahmed', 'Nida', 'Owais', 'Farah', 'Zain', 'Mehak', 'Haris', 'Amna'
    ],
    'Dept_ID': [101,102,103,104,105,101,102,103,104,105,101,102,103,104,105,101,102,103,104,105],
    'Salary': [
        70000, 82000, 60000, 90000, 75000, 71000, 88000, 64000, 94000, 77000,
        73000, 85000, 62000, 91000, 76000, 70500, 89500, 65000, 93000, 78000
    ],
    'Join_Year': [
        2018,2019,2020,2018,2017,2019,2018,2021,2022,2020,
        2017,2018,2019,2021,2022,2023,2019,2020,2021,2022
    ]
}

departments = {
    'Dept_ID': [101,102,103,104,105,106],
    'Dept_Name': ['HR','IT','Finance','Marketing','Sales','Operations'],
    'Manager': ['Faisal','Asma','Kamran','Tariq','Sadia','Hassan'],
    'Location': ['Lahore','Karachi','Islamabad','Lahore','Karachi','Faisalabad']
}


left_table_employees_df = pd.DataFrame(employees)
right_table_departments_df = pd.DataFrame(departments)



#                                          Inner Join


inner_join  = left_table_employees_df.merge(right_table_departments_df  ,on='Dept_ID')
# print(inner_join)


#                                          Left Join


# left_join = left_table_employees_df.merge(right_table_departments_df, on='Dept_ID', how='left')
# print(pd.DataFrame(left_join))
# result 
#     Emp_ID    Name  Dept_ID  Salary  Join_Year  Dept_Name Manager   Location
# 0     1001     Ali      101   70000       2018         HR  Faisal     Lahore
# 1     1002    Sara      102   82000       2019         IT    Asma    Karachi
# 2     1003    Umer      103   60000       2020    Finance  Kamran  Islamabad
# 3     1004    Hina      104   90000       2018  Marketing   Tariq     Lahore
# 4     1005   Bilal      105   75000       2017      Sales   Sadia    Karachi
# 5     1006  Ayesha      101   71000       2019         HR  Faisal     Lahore
# 6     1007    Raza      102   88000       2018         IT    Asma    Karachi
# 8     1009  Danish      104   94000       2022  Marketing   Tariq     Lahore
# 9     1010    Tuba      105   77000       2020      Sales   Sadia    Karachi
# 10    1011  Kashif      101   73000       2017         HR  Faisal     Lahore
# 11    1012    Iqra      102   85000       2018         IT    Asma    Karachi
# 12    1013   Ahmed      103   62000       2019    Finance  Kamran  Islamabad
# 13    1014    Nida      104   91000       2021  Marketing   Tariq     Lahore
# 14    1015   Owais      105   76000       2022      Sales   Sadia    Karachi
# 15    1016   Farah      101   70500       2023         HR  Faisal     Lahore
# 16    1017    Zain      102   89500       2019         IT    Asma    Karachi
# 17    1018   Mehak      103   65000       2020    Finance  Kamran  Islamabad
# 18    1019   Haris      104   93000       2021  Marketing   Tariq     Lahore
# 19    1020    Amna      105   78000       2022      Sales   Sadia    Karachi



#                                          Right Join

# right_join = left_table_employees_df.merge(right_table_departments_df, on='Dept_ID', how='right')
# print(pd.DataFrame(right_join))
#     Emp_ID    Name  Dept_ID   Salary  Join_Year   Dept_Name Manager    Location
# 0   1001.0     Ali      101  70000.0     2018.0          HR  Faisal      Lahore
# 1   1006.0  Ayesha      101  71000.0     2019.0          HR  Faisal      Lahore
# 2   1011.0  Kashif      101  73000.0     2017.0          HR  Faisal      Lahore
# 3   1016.0   Farah      101  70500.0     2023.0          HR  Faisal      Lahore
# 4   1002.0    Sara      102  82000.0     2019.0          IT    Asma     Karachi
# 5   1007.0    Raza      102  88000.0     2018.0          IT    Asma     Karachi
# 6   1012.0    Iqra      102  85000.0     2018.0          IT    Asma     Karachi
# 7   1017.0    Zain      102  89500.0     2019.0          IT    Asma     Karachi
# 8   1003.0    Umer      103  60000.0     2020.0     Finance  Kamran   Islamabad
# 9   1008.0    Mona      103  64000.0     2021.0     Finance  Kamran   Islamabad
# 10  1013.0   Ahmed      103  62000.0     2019.0     Finance  Kamran   Islamabad
# 11  1018.0   Mehak      103  65000.0     2020.0     Finance  Kamran   Islamabad
# 12  1004.0    Hina      104  90000.0     2018.0   Marketing   Tariq      Lahore
# 13  1009.0  Danish      104  94000.0     2022.0   Marketing   Tariq      Lahore
# 14  1014.0    Nida      104  91000.0     2021.0   Marketing   Tariq      Lahore
# 15  1019.0   Haris      104  93000.0     2021.0   Marketing   Tariq      Lahore
# 16  1005.0   Bilal      105  75000.0     2017.0       Sales   Sadia     Karachi
# 17  1010.0    Tuba      105  77000.0     2020.0       Sales   Sadia     Karachi
# 18  1015.0   Owais      105  76000.0     2022.0       Sales   Sadia     Karachi
# 19  1020.0    Amna      105  78000.0     2022.0       Sales   Sadia     Karachi
# 20     NaN     NaN      106      NaN        NaN  Operations  Hassan  Faisalabad



#                                            FUll Outer Join


# full_outer = left_table_employees_df.merge(right_table_departments_df, on='Dept_ID', how='outer')
# print(full_outer)


#                                              LEFT ANTI JOIN

# left_join = left_table_employees_df.merge(right_table_departments_df, on='Dept_ID', how='left')
# print(left_join)


#                                              Right ANTI JOIN


# right_join = left_table_employees_df.merge(right_table_departments_df, on='Dept_ID', how='right')
# right_anti = right_join.loc[right_join['Name'].isna(), 'Manager': 'Location']
# print(right_anti)
#    Manager    Location
# 20  Hassan  Faisalabad