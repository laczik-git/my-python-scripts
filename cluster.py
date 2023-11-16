# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()
import pandas as pd

# Import data from file with pandas sep = separator, index column is the first collumn so index_col=0
data = pd.read_csv(r"E:\results_all_merged_genus_modified6.txt", sep='\t', index_col=0)
print(data)

# Set lable font scale
sns.set(font_scale=1.0)
g = sns.clustermap(data, cmap='OrRd', cbar_kws={"label":"Relative abundance (%)","ticks":[0, 2, 4, 6, 8, 10, 12]}, metric='braycurtis', yticklabels=int(1), xticklabels=int(1), vmin=0, vmax=12.0,)
g.ax_heatmap.set_yticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in g.ax_heatmap.get_yticklabels()])
plt.show()
