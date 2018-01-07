import glob
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
from datetime import datetime

should_filter = False
names_whitelist = ['Spawn', 'Balance', 'Mapgen', 'Vehicle', 'Performance', 'Bionics']


def is_whitelisted(file):
    for name in names_whitelist:
        if name in file:
            return True

    return False


csv_files = glob.glob('./labels_closed_on_date/*.csv')

if should_filter:
    filter = [is_whitelisted(file) for file in csv_files]
    csv_files = np.array(csv_files)[filter]

label_names = [f_name.replace('./labels_closed_on_date/', '').replace('.csv', '') for f_name in csv_files]
colors = ['aqua', 'azure', 'beige', 'black', 'blue', 'brown', 'chartreuse', 'coral', 'gold', 'fuchsia', 'indigo',
          'lavender', 'lightgreen', 'magenta', 'orangered', 'teal', 'tomato', 'violet', 'yellowgreen', 'yellow', 'plum']

if should_filter:
    colors.reverse()

sep = ','
closed_labels_data = [np.array(pd.read_csv(
    file_name, header=None, na_filter=True, sep=sep).as_matrix()) for
                      file_name in csv_files]

# remove first row describing data set
closed_labels_data = [closed_labels_data[i][1:] for i in range(len(closed_labels_data))]

for i in range(len(closed_labels_data)):
    closed_labels_data[i][:, 0] = [datetime.strptime(closed_labels_data[i][:, 0][row], '%Y-%m-%d') for row in
                                   range(len(closed_labels_data[i][:, 0]))]
    closed_labels_data[i][:, 1] = np.array(closed_labels_data[i][:, 1], dtype=int)

# declare legends
patches = [mpatches.Patch(color=colors[i], label=label_names[i]) for
           i in range(len(label_names))]

for idx, name in enumerate(label_names):
    plt.scatter(closed_labels_data[idx][:, 0], closed_labels_data[idx][:, 1], color=colors[idx])

# get global popularity data

global_popularity = np.array(
    pd.read_csv('./popularity/global_popularity.csv', header=None, na_filter=True, sep=sep).as_matrix())
# remove feature description
global_popularity = global_popularity[1:]
global_popularity[:, 0] = [datetime.strptime(global_popularity[:, 0][row], '%m/%d/%Y') for row in
                           range(len(global_popularity[:, 0]))]

# popularity as float percentage
global_popularity[:, 1] = np.array(global_popularity[:, 1], dtype=np.float64) / 100

# plot global popularity
plt.plot(global_popularity[:, 0], global_popularity[:, 1], color='green')

# add patch for global popularity
patches.append(mpatches.Patch(color='green', label='Global popularity percentage'))

plt.legend(handles=patches)
plt.show()
