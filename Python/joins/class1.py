import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np

#                                         INNER JOIN


# left_table = {'Date': ['01-01-2020', '02-01-2020', '03-01-2020', '04-01-2020' ],
#               'CountryID': [1,1,3,2],
#               'Units': [40, 25, 30, 35]}

# left_table_df = pd.DataFrame(left_table)
# # print(left_table_df)

# right_table = {'ID': [3,4],
#               'Country': ['Pandama', 'Spain']}

# right_table_df = pd.DataFrame(right_table)

# print(left_table_df.merge(right_table_df, left_on='CountryID', right_on='ID'))


#                                        example 2 inner join


# left_table = {'Date': ['01-01-2020', '02-01-2020', '03-01-2020', '04-01-2020' ],
#               'CountryID': [1,1,3,2],
#               'Units': [40, 25, 30, 35],
#               'Country' : ["Pak", "Ind", "Afg", "Span"]}
# left_table_df = pd.DataFrame(left_table)

# right_table = {'ID': [3,4],
#               'Country': ['Pandama', 'Spain']}

# right_table_df = pd.DataFrame(right_table)

# print(left_table_df.merge(right_table_df, left_on='CountryID', right_on='ID', ssuffixes=('_left', '_right')).drop('ID', axis=1))


#                                             LEFT JOIN


# left_table = {'Date': ['01-01-2020', '02-01-2020', '03-01-2020', '04-01-2020' ],
#               'CountryID': [1,1,3,4],
#               'Units': [40, 25, 30, 35]}

# left_table_df = pd.DataFrame(left_table)


# right_table = {'ID': [1,2, 3],
#               'Country': ['USA', 'Canada', 'Panama'],
#               'Pop': [122, 32525, 26626]}

# right_table_df = pd.DataFrame(right_table)

# print(left_table_df.merge(right_table_df, left_on='CountryID', right_on='ID', how='left').drop('ID', axis=1))



#                                             Right Join

# left_table = {'Date': ['01-01-2020', '02-01-2020', '03-01-2020', '04-01-2020' ],
#               'CountryID': [1,1,2,4],
#               'Units': [40, 25, 30, 35]}

# left_table_df = pd.DataFrame(left_table)

# right_table = {'ID': [3],
#               'Country': ['Pandama']}

# right_table_df = pd.DataFrame(right_table)

# print(left_table_df.merge(right_table_df , left_on='CountryID', right_on='ID' , how='right'))


# left_table = {'Date': ['01-01-2020', '02-01-2020', '03-01-2020', '04-01-2020' ],
#               'CountryID': [1,1,3,2],
#               'Units': [40, 25, 30, 35]}

# left_table_df = pd.DataFrame(left_table)

# right_table = {'ID': [3,4],
#               'Country': ['Panama', 'Spain']}

# right_table_df = pd.DataFrame(right_table)

# left_join = left_table_df.merge(right_table_df , left_on='CountryID', right_on='ID', how='left')
# print(left_join)

# left_join_filter = left_join[left_join.Country != 'NaN']
# print(left_join_filter)


left_table = {'Date': ['01-01-2020', '02-01-2020', '03-01-2020', '04-01-2020' ],
              'CountryID': [1,1,3,2],
              'Units': [40, 25, 30, 35]}

left_table_df = pd.DataFrame(left_table)

right_table = {'ID': [3,4],
              'Country': ['Panama', 'Spain']}

right_table_df = pd.DataFrame(right_table)


right_join = left_table_df.merge(right_table_df, left_on='CountryID', right_on='ID', how='right')
print(right_join)
right_anti = right_join[right_join['CountryID'].isna()]
right_anti_column = right_anti[['Country']]
print(right_anti_column)