import matplotlib.pyplot as plt

# Data
years = [2005, 2007, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
values = [1, 2, 2, 1, 3, 2, 3, 3, 21, 31, 34, 30, 56, 68, 33, 5]

# Format the data for boxplot
data = [[v] for v in values]

# Create a boxplot
plt.figure(figsize=(12, 6))
plt.boxplot(data, vert=True, patch_artist=True, labels=years, boxprops=dict(linewidth=2), whiskerprops=dict(linewidth=2))

plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Yearly Data Distribution')

# Adjust layout to minimize white space
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.25)

# Save the figure with bbox_inches='tight'
plt.savefig('yearly_data_boxplot.pdf', bbox_inches='tight')

# Display the boxplot
plt.show()
