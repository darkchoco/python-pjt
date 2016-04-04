#!/usr/bin/env python

# 아래 shell script 내용을 python 식으로 바꾼 것이다.
# 즉 아래와 상기와 같은 script 작성 후 /etc/cron.weekly에 등록하면 끝.

# #!/bin/sh
# # Script to remove the older Confluence backup files.
# # Currently we retain at least the last two weeks worth
# # of backup files in order to restore if needed.
# BACKUP_DIR="/data/web/confluence/backups"
# DAYS_TO_RETAIN=14
# find $BACKUP_DIR -maxdepth 1 -type f -ctime +$DAYS_TO_RETAIN -delete

# 참고:
# How to get file creation & modification date/times in Python?
# - http://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
# Comparing date, checking the old files
# - http://stackoverflow.com/questions/7430928/python-comparing-date-check-for-old-file
# List files in ONLY the current directory
# - http://stackoverflow.com/questions/11968976/list-files-in-only-the-current-directory
# How do you get a directory listing sorted by creation date in python?
# - http://stackoverflow.com/questions/168409/how-do-you-get-a-directory-listing-sorted-by-creation-date-in-python

import os
import sys
from os import path
from datetime import datetime, timedelta

__date__ = '2016-02-23'

if len(sys.argv) < 2:
    PATH = '/home01/atlassian/application-data/confluence/backups/'
else:
    PATH = sys.argv[1]

two_weeks = datetime.now() - timedelta(weeks=2)

os.chdir(PATH)

files = [f for f in os.listdir(os.curdir) if os.path.isfile(f)]
files.sort(key=os.path.getmtime, reverse=True)

i = 0

for f in files:
    filetime = datetime.fromtimestamp(path.getctime(f))
    if filetime < two_weeks:
        os.remove(f)
        print("{} is deleted.".format(f))
        i += 1

print("\n{} files are deleted.".format(i))
