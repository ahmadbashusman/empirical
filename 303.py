import matplotlib.pyplot as plt

# Data
labels = ['Critical', 'High', 'Medium', 'Low', 'Unrated']
sizes = [53, 224, 174, 24, 7]
colors = ['#282828', '#ff0000', '#ff8000', '#ffbf00', '#808080']
explode = (0.1, 0, 0, 0, 0)  # explode the 'Critical' slice

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add legend
ax.legend(labels, title="CVSS Severity", loc="center left", bbox_to_anchor=(0.9, 0.5))

# Adjust layout to minimize white space
plt.subplots_adjust(left=-0, right=0.8, top=1, bottom=0)

# Save the figure with bbox_inches='tight'
plt.savefig('vulnerability_categories_pie_chart.pdf', bbox_inches='tight')

# Display the pie chart
plt.show()
