import sys
input = sys.stdin.readline

T = int(input())
results = []
for _ in range(T):
  raw_string = input().strip()
  result = 2
  front, back = 0, len(raw_string)-1
  not_palindrome_at = -1
  
  if len(raw_string)%2 == 0:
    while front < back:
      if raw_string[front] == raw_string[back]:
        front += 1
        back -= 1
      else:
        not_palindrome_at = front
        break
    if front > back:
      result = 0
      
    last_front = front
    last_back = back
    if result != 0:
      for i in range(not_palindrome_at,len(raw_string)-not_palindrome_at):
        if result == 1:
          break
        is_skipped = False
        front = last_front
        back = last_back
        same_until_last = False
        while front < back:
          if front == i and not is_skipped:
            front += 1
            is_skipped = True
          if back == i and not is_skipped:
            back -= 1
            is_skipped = True
          if raw_string[front] == raw_string[back]:
            same_until_last = True
            if back - front > 1:
              front += 1
              back -= 1
            else:
              break
          else:
            same_until_last = False
            break
        if front == back and same_until_last:
          result = 1
  else:
    while front != back:
      if raw_string[front] == raw_string[back]:
        front += 1
        back -= 1
      else:
        not_palindrome_at = front
        break
    if front == back:
      result = 0
      
    last_front = front
    last_back = back
    if result != 0:
      for i in range(not_palindrome_at,len(raw_string)-not_palindrome_at):
        if result == 1:
          break
        is_skipped = False
        front = last_front
        back = last_back
        same_until_last = False
        while front != back:
          if front == i and not is_skipped:
            front += 1
            is_skipped = True
          if back == i and not is_skipped:
            back -= 1
            is_skipped = True
          if raw_string[front] == raw_string[back]:
            same_until_last = True
            if back - front > 1:
              front += 1
              back -= 1
            else:
              break
          else:
            same_until_last = False
            break
        if back - front == 1 and same_until_last:
          result = 1
  
  results.append(result)
  
for result in results:
  print(result)