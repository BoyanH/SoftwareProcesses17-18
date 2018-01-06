from github import Github
from datetime import datetime
import csv
import os

git_username = os.environ['GIT_USERNAME']
git_password = os.environ['GIT_PASSWORD']

g = Github(git_username, git_password)
repo = g.get_repo('CleverRaven/Cataclysm-DDA')
commits = repo.get_commits()

localization_commit_dates = []
localization_commit_count_per_date = {}

for commit in commits:
    cdata = commit.commit
    head = commit.stats
    message = cdata.message
    date = cdata.committer.date
    date_norm = date.replace(hour=0, minute=0, second=1)  # per day information is our finest granularity level
    date_str = str(date_norm)
    # date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

    if date.year <= 2016:
        break

    print('year: {}; month: {}'.format(date.year, date.month))

    if 'i18n' in message or 'translat' in message:
        if date_norm not in localization_commit_dates:
            localization_commit_dates.append(date_norm)

        if date_str not in localization_commit_count_per_date:
            localization_commit_count_per_date[date_str] = 1
        else:
            localization_commit_count_per_date[date_str] += 1

        # print(cdata.message)
        # print(cdata.committer.date)

localization_commit_dates.reverse()
localization_commit_counts = [localization_commit_count_per_date[str(x)] for x in localization_commit_dates]
dates_axis = [x.strftime('%Y-%m-%d') for x in localization_commit_dates]

writer = csv.writer(open('./i18n_commits.csv', 'w'))

for i, date in enumerate(dates_axis):
        writer.writerow([date, localization_commit_counts[i]])
