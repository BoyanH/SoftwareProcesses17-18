from github import Github, Label
from datetime import datetime
import numpy as np
import csv
import os

def date_str_to_datetime(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')

git_username = os.environ['GIT_USERNAME']
git_password = os.environ['GIT_PASSWORD']

g = Github(git_username, git_password)
repo = g.get_repo('CleverRaven/Cataclysm-DDA')
enhancement_label = 'Enhancement'
enhancement_label_obj = None
issues = repo.get_issues()
blacklisted_labels = ['Information / Interface', 'JSON', 'Easy-fix', 'Long-term', 'Suggestion (Discuss)',
                      'Organization']

dates = []

# search for enhancement label to get the git object of it for further search
# this api sucks... creating a label object myself didn't really work
for issue in issues:
    labels = issue.get_labels()
    label_names = [label.name for label in labels]
    if enhancement_label in label_names:
        enhancement_label_obj = labels[label_names.index(enhancement_label)]
        break

# ok, now we have the issues we really want
issues = repo.get_issues(state='closed', labels=[enhancement_label_obj], sort='sort:updated-desc')
closed_issues_per_label = {}
for issue in issues:
    labels = issue.get_labels()
    label_names = [label.name for label in labels]
    closed_date = issue.closed_at
    closed_norm = closed_date.replace(hour=0, minute=0, second=1)  # per day information is our finest granularity level
    closed_str = str(closed_norm)
    print(closed_str)

    if closed_date.year <= 2016:
        continue

    for label in label_names:
        if label not in blacklisted_labels and label != enhancement_label:
            if label not in closed_issues_per_label:
                closed_issues_per_label[label] = {}

            if closed_str not in closed_issues_per_label[label]:
                closed_issues_per_label[label][closed_str] = 1
            else:
                closed_issues_per_label[label][closed_str] += 1

for label in closed_issues_per_label:
    dates = np.array([date_str_to_datetime(date) for date in closed_issues_per_label[label]])
    counts = np.array([closed_issues_per_label[label][str(date)] for date in dates])

    date_sort_args = dates.argsort()
    dates = dates[date_sort_args]
    counts = counts[date_sort_args]
    dates = [x.strftime('%Y-%m-%d') for x in dates]  # remove irrelevant information

    writer = csv.writer(open('./labels_closed_on_date/{}_issues_closed.csv'.format(label.replace('/', 'OR')), 'w'))
    for i, date in enumerate(dates):
        writer.writerow([date, counts[i]])


