import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
from datetime import datetime

popularity_names = ['overTen', 'overTwenty', 'overFifty', 'overHundred']
sep = ','
popularity_data_sets = [np.array(pd.read_csv(
    './popularity/' + file_name + '.csv', header=None, na_filter=True, sep=sep).as_matrix()) for
                        file_name in popularity_names]
# remove first row describing data set
popularity_data_sets = [popularity_data_sets[i][1:] for i in range(len(popularity_data_sets))]

for i in range(len(popularity_data_sets)):
    popularity_data_sets[i][:, 0] = [datetime.strptime(popularity_data_sets[i][:, 0][row], '%m/%d/%Y') for row in
                                     range(len(popularity_data_sets[i][:, 0]))]
    popularity_data_sets[i][:, 1] = np.array(popularity_data_sets[i][:, 1], dtype=int)

dates_axis = []
localization_commit_counts = []

# declare corresponding colors
colors = ['red', 'green', 'blue', 'purple']

# declare legends
popularity_rates = ['10%', '20%', '50%', '100%']
patches = [mpatches.Patch(color=colors[i], label='Number of countries with >= {} trend'.format(popularity_rates[i])) for
           i in range(len(popularity_rates))]

for idx, name in enumerate(popularity_names):
    plt.plot(popularity_data_sets[idx][:, 0], popularity_data_sets[idx][:, 1], color=colors[idx])



# get i18n commits data

i18n_commits = np.array(pd.read_csv('./i18n_commits.csv', header=None, na_filter=True, sep=sep).as_matrix())
i18n_commits[:, 0] = [datetime.strptime(i18n_commits[:, 0][row], '%Y-%m-%d') for row in
                                     range(len(i18n_commits[:, 0]))]

# plot i18n commits
plt.plot(i18n_commits[:, 0], i18n_commits[:, 1], color='black')

# add patch for i18n commits
patches.append(mpatches.Patch(color='black', label='Number of i18n commits'))

plt.legend(handles=patches)
plt.show()
