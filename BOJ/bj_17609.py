import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  raw_string = input().strip()
  string = deque(list(raw_string))
  result = 2
  front, back = 0, len(raw_string)-1
  if len(string)%2 == 0:
    while front < back:
      if string[front] == string[back]:
        front += 1
        back -= 1
      else:
        break
    if front > back:
      result = 0
  else:
    while front != back:
      if string[front] == string[back]:
        front += 1
        back -= 1
      else:
        break
    if front == back:
      result = 0
  
  if result != 0:
    for i in range(len(raw_string)):
      if result == 1:
        break
      string_without_char = raw_string[:i] + raw_string[i+1:]
      front, back = 0, len(string_without_char)-1
      if len(string_without_char)%2 == 0:
        while front < back:
          if string_without_char[front] == string_without_char[back]:
            front += 1
            back -= 1
          else:
            break
        if front > back:
          result = 1
      else:
        while front != back:
          if string_without_char[front] == string_without_char[back]:
            front += 1
            back -= 1
          else:
            break
        if front == back:
          result = 1
  
  print(result)