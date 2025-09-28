from io import StringIO  # json format ko readable format me karne ke liye
import requests # url hit karne ke liye 
from bs4 import BeautifulSoup # html ko saaf karne ke liye
import pandas as pd
import sqlite3
from datetime import datetime

# url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
# table_attribs = "By market capitalization"
# # print(requests.get(url).text)

# soup = BeautifulSoup(requests.get(url).text, "html.parser")
# table = soup.find("span", string=table_attribs).find_next("table")
# # print(table)
# df = pd.read_html(StringIO(str(table)))[0]
# # print(df['Market cap (US$ billion)'])

# message = 'Data extraction complete. Initiating Transformation process'

# # with open('./logs/code_log.txt', 'a') as f:
# #         f.write(f'{datetime.now()}: {message}\n')

# exchange_rate = pd.read_csv(".\input\exchange_rate.csv", index_col=0).to_dict()['Rate']
# print(df['Market cap (US$ billion)'])
# print(round(df['Market cap (US$ billion)'] * exchange_rate['EUR'],2))
# # print(exchange_rate)



# Step 0: Maintaining a Log File 
# This step is done to record the logs while performing ETL and it is not neccessary in an ETL Pipeline


def log_progress(message):
    """This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing"""

    with open('./logs/code_log.txt', 'a') as f:
        f.write(f'{datetime.now()}: {message}\n')



# Step 1: Extract



url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = "By market capitalization"
print(requests.get(url).text)

soup = BeautifulSoup(requests.get(url).text, "html.parser")
table = soup.find("span", string=table_attribs).find_next("table")
df = pd.read_html(StringIO(str(table)))[0]
 
message = 'Data extraction complete. Initiating Transformation process'

# log_progress(message)

# step 1 in def 

# def extract(url, table_attribs):
#     """ This function aims to extract the required
#     information from the website and save it to a data frame. The
#     function returns the data frame for further processing. """

#     soup = BeautifulSoup(requests.get(url).text, 'html.parser')
#     table = soup.find('span', string=table_attribs).find_next('table')
#     df = pd.read_html(StringIO(str(table)))[0]

#     log_progress('Data extraction complete. Initiating Transformation process')

#     return df




# Step 2: Transform



exchange_rate = pd.read_csv(".\input\exchange_rate.csv", index_col=0).to_dict()['Rate']
# print(exchange_rate)
# print(df)

# print(round(df['Market cap (US$ billion)'] * exchange_rate['EUR'],2))
df['Market cap (EUR)'] = round(df['Market cap (US$ billion)'] * exchange_rate['EUR'],2)
df['Market cap (GBP)'] = round(df['Market cap (US$ billion)'] * exchange_rate['GBP'],2)
df['Market cap (INR)'] = round(df['Market cap (US$ billion)'] * exchange_rate['INR'],2)
# print(df)

# log_progress('Data transformation complete. Initiating Loading process')

# def transform(df, csv_path):
#     """ This function accesses the CSV file for exchange rate
#     information, and adds three columns to the data frame, each
#     containing the transformed version of Market Cap column to
#     respective currencies"""

#     exchange_rate = pd.read_csv(csv_path, index_col=0).to_dict()['Rate']

#     df['MC_GBP_Billion'] = round(df['Market cap (US$ billion)'] * exchange_rate['GBP'], 2)
#     df['MC_EUR_Billion'] = round(df['Market cap (US$ billion)'] * exchange_rate['EUR'], 2)
#     df['MC_INR_Billion'] = round(df['Market cap (US$ billion)'] * exchange_rate['INR'], 2)

#     print(df)

#     log_progress('Data transformation complete. Initiating Loading process')

#     return df




# Step 3: Load
# Loading data to a CSV

df.to_csv("./output/Largest_bank_data.csv")

def load_to_csv(df, output_path):
    """ This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing."""

    df.to_csv(output_path)

    log_progress('Data saved to CSV file')

