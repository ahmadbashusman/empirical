import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Create a sample dataset
years = list(range(2015, 2025))
categories = ['SW', 'FW']
data = []

# Generate random data for the box plots
np.random.seed(0)
for year in years:
    for category in categories:
        data.append([year, category, np.random.uniform(0, 10, 100)])

# Flatten the data into a dataframe
flat_data = []
for year, category, values in data:
    for value in values:
        flat_data.append([year, category, value])

df = pd.DataFrame(flat_data, columns=['Year', 'Category', 'Value'])

# Create the box plot
plt.figure(figsize=(14, 8))
sns.boxplot(x='Year', y='Value', hue='Category', data=df)

# Set the y-axis range from 0 to 10
plt.ylim(0, 10)

# Set the x-axis range from 2015 to 2024
plt.xticks(ticks=np.arange(len(years)), labels=years)

# Add title and labels
plt.title('Box Plot Example')
plt.xlabel('Year')
plt.ylabel('Value')

# Show legend and plot
plt.legend(title='Category')
plt.show()
