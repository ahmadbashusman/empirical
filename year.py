import matplotlib.pyplot as plt

# Data
years = [2005, 2007, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
values = [1, 2, 2, 1, 3, 2, 3, 3, 21, 31, 34, 30, 56, 68, 33, 5]

# Merge years 2005-2016
merged_values = sum(values[:8])  # Sum the values for the years 2005-2016
individual_values = values[8:]   # Individual values for the years after 2016

# Create a new list of years with merged and individual years
merged_years = ['2005-2016', *years[8:]]

# Create a column chart
plt.figure(figsize=(12, 6))
plt.bar(range(len(merged_years)), [merged_values, *individual_values], color=['indianred'] + ['firebrick'] * len(individual_values))
plt.ylabel('# Vulnerabilities')

# Set custom x-axis ticks
plt.xticks(range(len(merged_years)), merged_years, rotation=45)

# Adjust layout to minimize white space
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.25)

# Save the figure with bbox_inches='tight'
plt.savefig('yearly_CVE.pdf', bbox_inches='tight')

# Display the column chart
plt.show()
