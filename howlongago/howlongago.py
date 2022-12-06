
import datetime
import sys

value1 = sys.argv[1]

value1 = value1.split(',')

date1 = datetime.date.fromisoformat(value1[0])
date2 = datetime.date.fromisoformat(value1[1])
print((date1-date2).days)
