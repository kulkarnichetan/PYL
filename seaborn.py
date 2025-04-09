import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load a sample dataset
tips = sns.load_dataset("tips")

# 2. Show the first few rows
tips.head()

# 3. Basic histogram of a numeric column
sns.histplot(data=tips, x="total_bill")

# 4. Box plot to visualize distribution and outliers
sns.boxplot(data=tips, x="day", y="total_bill")

# 5. Scatter plot for two numeric columns
sns.scatterplot(data=tips, x="total_bill", y="tip")

# 6. Line plot to show trends
sns.lineplot(data=tips.sort_values("size"), x="size", y="total_bill")

# 7. Count plot for categorical data
sns.countplot(data=tips, x="day")

# 8. Bar plot of average tip by gender
sns.barplot(data=tips, x="sex", y="tip")

# 9. Heatmap of correlation matrix
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")

# 10. Pair plot for multiple relationships
sns.pairplot(tips)

# 11. Violin plot (distribution + density)
sns.violinplot(data=tips, x="day", y="tip")

# 12. Strip plot for raw data visualization
sns.stripplot(data=tips, x="day", y="tip", jitter=True)

# 13. Swarm plot (like strip plot but non-overlapping)
sns.swarmplot(data=tips, x="day", y="tip")

# 14. KDE (density plot)
sns.kdeplot(data=tips, x="total_bill", fill=True)

# 15. Set plot style
sns.set_style("darkgrid")

# 16. Set color palette
sns.set_palette("pastel")

# 17. Add custom plot title and labels
sns.boxplot(data=tips, x="sex", y="tip")
plt.title("Tip Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Tip Amount")

# 18. Save the current plot to file
plt.savefig("seaborn_plot.png")

# 19. Show the plot (needed to render in some environments)
plt.show()

# 20. Use FacetGrid to plot multiple subsets
g = sns.FacetGrid(tips, col="time", row="sex")
g.map(sns.histplot, "total_bill")
