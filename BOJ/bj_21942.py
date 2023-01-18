import sys
from datetime import datetime, timedelta
from collections import defaultdict
from math import floor
input = sys.stdin.readline

N, L, F = input().split()
N, F = int(N), int(F)

# not 00/00:00
day, hour_and_minute = L.split('/')
day = int(day)
hour, minute = hour_and_minute.split(':')
hour, minute = int(hour), int(minute)
due = timedelta(days=day,hours=hour,minutes=minute)
zero = timedelta(days=0,hours=0,minutes=0)
fines = defaultdict(int)
table = defaultdict(defaultdict)
for _ in range(N):
  date, time, part, name = input().split()
  y,M,d = map(int,date.split('-'))
  h, m = map(int,time.split(':'))
  try:
    term = datetime(2021,M,d,h,m) - table[name][part]
    overdue = (due - term)
    if overdue < zero:
      fine = abs(F * floor(overdue.total_seconds() / 60))
      fines[name] += fine
    del table[name][part]
  except:
    table[name][part] = datetime(2021,M,d,h,m)
    
if len(fines) == 0:
  print(-1)
else:
  for name, fine in sorted(fines.items()):
    print(name, fine, sep=' ')