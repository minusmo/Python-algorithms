from operator import itemgetter
N = int(input())

words = []

for _ in range(N):
    word = input()
    words.append((word, len(word)))
    
words = sorted(words, key=itemgetter(1,0))
cache = None
for (word, length) in words:
    if word == cache:
        continue
    print(word)
    cache = word