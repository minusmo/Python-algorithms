N = int(input())
index = 0
title = 666
while True:
    if '666' in str(title):
        index += 1
    if index == N:
        print(title)
        break
    title += 1