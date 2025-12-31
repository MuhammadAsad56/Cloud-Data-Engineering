# import kaggle/
print("ggg")
#read data from the file and handle null values
import pandas as pd

df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()

# print(df.head(10))


#rename columns names ..make them lower case and replace space with underscore
print(df.columns)
df.columns=df.columns.str.replace(' ','_')
df.columns=df.columns.str.lower()
print(df.columns)

#derive new columns discount , sale price and profit
# df['discount']=df['list_price']*df['discount_percent']*.01
# df['sale_price']= df['list_price']-df['discount']
# df['profit']=df['sale_price']-df['cost_price']
# # print(df[['discount', 'sale_price', 'profit']].head(5))

# #convert order date from object data type to datetime
# df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")

# #drop cost price list price and discount percent columns
# df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
# # print(df.columns)

# #load the data into sql server using replace option
# import sqlalchemy as sal
# engine = sal.create_engine('mssql://DESKTOP-65OSD7B/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
# conn=engine.connect()


# #load the data into sql server using append option
# df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')
