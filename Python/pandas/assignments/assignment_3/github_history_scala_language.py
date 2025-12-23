# Importing pandas
import pandas as pd

# Loading in the data
pulls_one = pd.read_csv("./pulls_2011-2013.csv")
pulls_two = pd.read_csv("./pulls_2014-2018.csv")
pull_files = pd.read_csv("./pull_file.csv") 

print(pulls_one)