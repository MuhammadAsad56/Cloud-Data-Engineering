import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Country': ['USA', 'China', 'India', 'Germany', 'Brazil', 'Japan', 'Russia', 'Canada', 'Australia', 'Mexico'],
    'GDP per Capita (USD)': [59850, 10660, 1800, 46100, 10600, 38900, 10750, 41300, 51000, 9500],
    'Life Expectancy (years)': [78.54, 76.91, 69.42, 81.13, 75.88, 84.6, 73.34, 82.2, 82.5, 77.03],
    'Population (millions)': [331, 1393, 1380, 83, 213, 126, 145, 38, 26, 128],
    'Color Grading': [59850, 10660, 1800, 46100, 10600, 38900, 10750, 41300, 51000, 9500]  # Using GDP for color
}
df = pd.DataFrame(data)

Life_Expectancy = df['Life Expectancy (years)']
Population = df['Population (millions)']
# print(Life_Expectancy)
# print(Population)

pop = [3.467,5.4773, 6.544, 7.4544, 4.7655,4.09, 6.48, 6.893489,5.65875, 1.788]
np_pop = np.array(pop * 10)

print(df.loc[:, ['Life Expectancy (years)', 'Population (millions)']])
plt.scatter(Life_Expectancy, Population,  s= np_pop)
# plt.xscale('log')
plt.xlabel('Life Expectancy ')
plt.ylabel('Population')
plt.show()
