import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  string = input().strip()
  result = 2
  if len(string)%2 == 0:
    left_half = string[:len(string)//2]
    right_half = ''.join(list(reversed(string[len(string)//2:])))
    if left_half == right_half:
      result = 0
  else:
    left_half = string[:len(string)//2]
    right_half = ''.join(list(reversed(string[len(string)//2+1:])))
    if left_half == right_half:
      result = 0
  
  if result != 0:
    for i in range(len(string)):
      if result == 1:
        break
      string_without_char = string[:i] + string[i+1:]
      if len(string_without_char)%2 == 0:
        left_half = string_without_char[:len(string_without_char)//2]
        right_half = ''.join(list(reversed(string_without_char[len(string_without_char)//2:])))
        if left_half == right_half:
          result = 1
      else:
        left_half = string_without_char[:len(string_without_char)//2]
        right_half = ''.join(list(reversed(string_without_char[len(string_without_char)//2+1:])))
        if left_half == right_half:
          result = 1
  
  print(result)