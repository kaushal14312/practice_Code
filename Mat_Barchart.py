import matplotlib.pyplot as plt
import numpy as np

# Sample data
products = ['Product A', 'Product B', 'Product C']
regions = ['North', 'South', 'East', 'West']

# Sales data for each product in each region
sales_data = np.array([
    [150, 200, 250, 300],  # Sales for Product A
    [180, 220, 230, 280],  # Sales for Product B
    [200, 240, 270, 320]   # Sales for Product C
])

# Set the bar width
bar_width = 0.2

# Set the positions of the bars on the x-axis
x = np.arange(len(regions))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create bars for each product
for i in range(len(products)):
    ax.bar(x + i * bar_width, sales_data[i], width=bar_width, label=products[i])

# Adding annotations on top of the bars
for i in range(len(products)):
    for j in range(len(regions)):
        ax.text(x[j] + i * bar_width, sales_data[i][j] + 5, str(sales_data[i][j]), 
                ha='center', va='bottom', fontsize=10)

# Adding labels and title
ax.set_xlabel('Regions', fontsize=14)
ax.set_ylabel('Sales', fontsize=14)
ax.set_title('Sales Comparison of Products Across Regions', fontsize=16)
ax.set_xticks(x + bar_width)
ax.set_xticklabels(regions)

# Adding a legend
ax.legend(title='Products')

# Adding gridlines for better readability
ax.yaxis.grid(True)

# Show the plot
plt.tight_layout()
plt.show()