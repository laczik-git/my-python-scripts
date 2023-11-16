# importing packages
from __future__ import unicode_literals
import pandas as pd
import matplotlib.pyplot as plt

# define variables
font = {'size':14}

# importing data
df = pd.read_csv("E:\Csenge_order2.csv", sep=';', index_col=0,)
print(df.head(5))

# Calculating % for percent stacked bars = stacking data to 100%
stacked_data = df.apply(lambda x: x*100/sum(x), axis=1)


# plot bar chart
fig = stacked_data.plot(
        align='center',
        kind='bar',
        stacked=True,
        title=False,
        mark_right=False,
        width=0.8,
        alpha=1.0)

# set legend's box position
plt.legend(bbox_to_anchor=(1, 0.365), labelspacing=-2.5, frameon=False)

# remove border
plt.box(False)

# resize bar chart
plt.subplots_adjust(left=0.1, right=0.6, top=1, bottom=0.1)

# Add y axis label
plt.ylabel("Relatív abundancia (%)", fontdict=font)


# draw chart
plt.show()