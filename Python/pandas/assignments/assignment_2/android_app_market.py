# Read in dataset
#                                                       1st part
import pandas as pd
apps_with_duplicates = pd.read_csv("./apps.csv")
# print(apps_with_duplicates)

# Drop duplicates from apps_with_duplicates
apps = apps_with_duplicates.drop_duplicates()

# # Print the total number of apps
print('Total number of apps in the dataset = ', apps.count()['App'] )

# # Have a look at a random sample of 5 rows
print(apps.sample(n=5))


#                                                      2nd part


# List of characters to remove
chars_to_remove = ["," , "+" , "$"]

# List of column names to clean
cols_to_clean = ["Installs" , "Price"]

# Loop for each column in cols_to_clean
for col in cols_to_clean:
    # Loop for each char in chars_to_remove
    for char in chars_to_remove:
        # Replace the character with an empty string
        apps[col] = apps[col].apply(lambda x: x.replace(char, ""))

# Print a summary of the apps dataframe
# print(apps)


#                                                         3rd part

# Convert Installs to float data type
apps['Installs'] = apps['Installs'].astype(float)

# Convert Price to float data type
apps['Price'] = apps['Price'].astype(float)

# Checking dtypes of the apps dataframe
# print(apps.dtypes)



#                                                           4th part

from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt

num_categories = apps['Category'].nunique()
# print('Number of categories = ', num_categories)

num_apps_in_category = apps['Category'].value_counts()

# Sort num_apps_in_category in descending order based on the count of apps in each category
sorted_num_apps_in_category = num_apps_in_category.sort_values(ascending=False)

# create bar chart 
plt.figure(figsize=(12,6))
plt.bar(num_apps_in_category.index, num_apps_in_category.values)
plt.title('Number of Apps per Category')
plt.xlabel("Category")
plt.ylabel("Number of Apps")
plt.xticks(rotation=90)
plt.show()


#                                                       5th part

avg_app_rating = apps['Rating'].mean()
print('Average app rating =', avg_app_rating)

# l# Histogram of ratings
plt.hist(apps['Rating'].dropna(), bins=30, color='skyblue', edgecolor='black')

# Add a vertical dashed line for average
plt.axvline(avg_app_rating, color='pink', linestyle='--', linewidth=2, label=f'Avg Rating = {avg_app_rating:.2f}')

# Labels and title
plt.title('Distribution of App Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Apps')

# Add legend (to show "Avg Rating = ...")
plt.legend()

# Show the chart
plt.show()



#                                                      6th part



# Select rows where both 'Rating' and 'Size' values are present (ie. the two values are not null)
apps_with_size_and_rating_present = apps[(apps['Rating'].notna()) & (apps['Size'].notna())]
# print(apps_with_size_and_rating_present)

# Subset for categories with at least 250 apps
large_categories = apps_with_size_and_rating_present.groupby('Category').filter(lambda x: len(x) >=  250)
print(large_categories)

# Plot size vs. rating
plt1 = sns.jointplot(x = large_categories['Size'], y = large_categories['Rating'])

# Select apps whose 'Type' is 'Paid'
paid_apps = apps[apps['Type'] == 'Paid']


# Plot price vs. rating
plt2 = sns.jointplot(x = paid_apps['Price'], y = paid_apps['Rating'])



#                                                       7th part



import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

# Select a few popular app categories
popular_app_cats = apps[apps.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY',
                                            'MEDICAL', 'TOOLS', 'FINANCE',
                                            'LIFESTYLE','BUSINESS'])]

# Examine the price trend by plotting Price vs Category
# Create the figure

ax = sns.stripplot(x = popular_app_cats['Category'], 
                   y = popular_app_cats['Price'], 
                   jitter=True, linewidth=1)

ax.set_title('App Pricing Trend Across Categories')

# Apps whose Price is greater than 200
apps_above_200 = apps[apps['Price'] > 200]
print(apps_above_200[['Category', 'App', 'Price']])



#                                                       8th part           


# Select apps priced below $100
apps_under_100 = apps[apps['Price'] < 100]

fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

# # Examine price vs category with the authentic apps (apps_under_100)
ax = sns.stripplot(x = apps_under_100['Category'], y = apps_under_100['Price'] , data = apps_under_100 , jitter = True, linewidth = 1)
ax.set_title('App pricing trend across categories after filtering for junk apps')


#                                                  9th part

import plotly.graph_objs as go
import plotly.offline as pyo

# Create traces
trace0 = go.Box(
    y = apps[apps['Type'] == 'Paid']['Installs'],
    name = 'Paid'
)

trace1 = go.Box(
    y = apps[apps['Type'] == 'Free']['Installs'],
    name = 'Free'
)

# Layout
layout = go.Layout(
    title = "Number of downloads of paid apps vs. free apps",
    yaxis = dict(title = "Log number of downloads",
                 type = 'log',
                 autorange = True)
)

# Combine and plot
data = [trace0, trace1]

pyo.plot({'data': data, 'layout': layout}, filename='paid_vs_free_downloads.html')



#                                                        10th part


# Load user_reviews.csv
reviews_df = pd.read_csv("./user_reviews.csv")

# Join the two dataframes
merged_df = pd.merge(apps, reviews_df, on='App' , how='inner')
print(merged_df)

# Drop NA values from Sentiment and Review columns
merged_df = merged_df.dropna(subset = ['Sentiment', 'Review'])

sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(11, 8)

# User review sentiment polarity for paid vs. free apps
ax = sns.boxplot(
    x = merged_df['Type'],               
    y = merged_df['Sentiment_Polarity'],
    data = merged_df
)
ax.set_title('Sentiment Polarity Distribution')
plt.show()