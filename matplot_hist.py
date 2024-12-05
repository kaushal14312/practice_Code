import matplotlib.pyplot as plt
import numpy as np

# Sample historical data
years = np.arange(2010, 2021)  # Years from 2010 to 2020
revenue = [150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000]  # Hypothetical revenue in millions

# Create a line plot
plt.figure(figsize=(12, 6))
plt.plot(years, revenue, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)

# Add titles and labels
plt.title('Company Revenue Over Time (2010-2020)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Revenue (in millions)', fontsize=14)

# Add grid
plt.grid(True)

# Annotate points
for i, value in enumerate(revenue):
    plt.text(years[i], value + 20, f'{value}', ha='center', fontsize=10)

# Show the plot
plt.xticks(years)  # Set x-ticks to show each year
plt.yticks(np.arange(0, 1100, 100))  # Set y-ticks
plt.tight_layout()
plt.show()