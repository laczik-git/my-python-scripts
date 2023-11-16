# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()
import pandas as pd

# Import data from file with pandas sep = separator, index column is the first collumn so index_col=0
data = pd.read_csv("E:\Book2.csv", sep=';', index_col=0)
print(data)
# Set lable font scale
sns.set(font_scale=1.0)
# Draw and visualize heatmap
ax = sns.heatmap(data, yticklabels=int(1), vmin=0.0, vmax=30.0, cmap="OrRd")
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
for label in ax.get_yticklabels():
    # Here it sets all italic.
    label.set_style("italic")
# Set colour bar label ticks
cbar = ax.collections[0].colorbar
cbar.set_ticks([0, 5, 10, 15, 20, 25, 30])
cbar.set_ticklabels(['0%', '5%', '10%', '15%', '20%', '25%', '30%'])
# Set colour bar label
cbar = ax.collections[0].colorbar.set_label("Relative abundance")
# Plot heatmap
plt.show()
