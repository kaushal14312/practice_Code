import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y1 = np.sin(x)                # Sine wave
y2 = np.cos(x)                # Cosine wave
y3 = np.random.randint(1, 10, size=10)  # Random integers for bar chart
x_bar = np.arange(len(y3))    # X positions for bar chart

# Create a figure with multiple subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 15))  # 3 rows, 1 column

# Line plot (Sine and Cosine)
axs[0].plot(x, y1, label='Sine', color='blue', linewidth=2)
axs[0].plot(x, y2, label='Cosine', color='orange', linewidth=2)
axs[0].set_title('Sine and Cosine Waves')
axs[0].set_xlabel('X-axis')
axs[0].set_ylabel('Y-axis')
axs[0].legend()
axs[0].grid(True)

# Scatter plot
axs[1].scatter(x, y1, color='blue', alpha=0.5, label='Sine Points')
axs[1].scatter(x, y2, color='orange', alpha=0.5, label='Cosine Points')
axs[1].set_title('Scatter Plot of Sine and Cosine')
axs[1].set_xlabel('X-axis')
axs[1].set_ylabel('Y-axis')
axs[1].legend()
axs[1].grid(True)

# Bar chart
axs[2].bar(x_bar, y3, color='green', alpha=0.7)
axs[2].set_title('Random Integer Bar Chart')
axs[2].set_xlabel('Index')
axs[2].set_ylabel('Random Value')
axs[2].set_xticks(x_bar)  # Set x-ticks to match the bar positions

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()