import matplotlib.pyplot as plt

# Data points
x = [2000, 2005, 2010, 2015, 2024]
y = [20, 50, 100, 150, 200]

# Create plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data points')

# Customize axes
plt.xlim(1999, 2025)
plt.ylim(0, 210)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Matplotlib Scatter Plot Example')

# Show plot
plt.legend()
plt.show()
import matplotlib.pyplot as plt

# Generate data
x = range(1, 101)
y = [2000 + i * (2024 - 2000) / 99 for i in range(100)]  # Linearly spaced values from 2000 to 2024

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(y, x, label='Reversed Axes Line plot')  # Note the swapped x and y

# Customize axes
plt.xlim(2000, 2024)
plt.ylim(1, 100)

# Add labels and title
plt.xlabel('Y Axis (formerly X)')
plt.ylabel('X Axis (formerly Y)')
plt.title('Matplotlib Example with Reversed Axes')

# Show plot
plt.legend()
plt.show()
import matplotlib.pyplot as plt

# Generate data
x = range(1, 101)
y = [2000 + i * (2024 - 2000) / 99 for i in range(100)]  # Linearly spaced values from 2000 to 2024

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Line plot')

# Customize axes
plt.xlim(1, 100)
plt.ylim(2000, 2024)

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Matplotlib Example')

# Show plot
plt.legend()
plt.show()

