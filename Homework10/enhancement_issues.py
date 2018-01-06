from github import Github, Label
from datetime import datetime
import csv
import os

git_username = os.environ['GIT_USERNAME']
git_password = os.environ['GIT_PASSWORD']

g = Github(git_username, git_password)
repo = g.get_repo('CleverRaven/Cataclysm-DDA')
enhancement_label = 'Enhancement'
issues = repo.get_issues(state='closed', labels=[Label.Label()])
blacklisted_labels = ['Information / Interface', 'JSON', 'Easy-fix', 'Long-term', 'Suggestion (Discuss)',
                      'Organization']

dates = []

for issue in issues:
    labels = issue.get_labels()
    print(issue.closed_at)
    print([label.name for label in labels])

    if enhancement_label in [label.name for label in labels]:
        print([label.name for label in labels])
