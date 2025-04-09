import matplotlib.pyplot as plt
import numpy as np

# 1. Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 2. Basic line plot
plt.plot(x, y)
plt.show()

# 3. Add title, x and y labels
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# 4. Customize line color, style, width
plt.plot(x, y, color='red', linestyle='--', linewidth=2)
plt.show()

# 5. Plot multiple lines
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.legend()
plt.show()

# 6. Scatter plot
x_points = np.random.rand(50)
y_points = np.random.rand(50)
plt.scatter(x_points, y_points)
plt.title("Random Scatter Plot")
plt.show()

# 7. Bar plot
categories = ['A', 'B', 'C']
values = [10, 24, 36]
plt.bar(categories, values)
plt.title("Simple Bar Chart")
plt.show()

# 8. Horizontal bar plot
plt.barh(categories, values, color='orange')
plt.show()

# 9. Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, color='green', edgecolor='black')
plt.title("Histogram")
plt.show()

# 10. Pie chart
sizes = [40, 30, 20, 10]
labels = ['Python', 'Java', 'C++', 'Ruby']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio
plt.title("Pie Chart Example")
plt.show()

# 11. Plot with grid
plt.plot(x, y)
plt.grid(True)
plt.title("With Grid")
plt.show()

# 12. Fill between
plt.fill_between(x, np.sin(x), alpha=0.3)
plt.title("Fill Between Sine Curve")
plt.show()

# 13. Subplots in one row
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, np.sin(x))
axs[1].plot(x, np.cos(x))
plt.suptitle("Side-by-Side Plots")
plt.show()

# 14. Subplots in 2x2 layout
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, np.sin(x))
axs[0, 1].plot(x, np.cos(x))
axs[1, 0].bar(categories, values)
axs[1, 1].hist(data)
plt.tight_layout()
plt.show()

# 15. Save a plot to a file
plt.plot(x, y)
plt.title("Saving a Plot")
plt.savefig("my_plot.png")
plt.close()

# 16. Change figure size
plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title("Custom Figure Size")
plt.show()

# 17. Add text annotation
plt.plot(x, y)
plt.text(5, 0, 'Center Point', fontsize=12, color='blue')
plt.show()

# 18. Customize ticks
plt.plot(x, y)
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.linspace(-1, 1, 5))
plt.title("Custom Ticks")
plt.show()

# 19. Axis limits
plt.plot(x, y)
plt.xlim(2, 8)
plt.ylim(-0.5, 0.5)
plt.title("Zoomed In Plot")
plt.show()

# 20. Plot with markers
plt.plot(x, np.sin(x), marker='o', linestyle='-', color='purple')
plt.title("Plot with Markers")
plt.show()
