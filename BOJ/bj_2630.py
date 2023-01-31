import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
color_paper = []
blues = 0
whites = 0
for _ in range(N):
  color_paper.append(list(map(int,input().split())))

def find_papers(row_start,row_end,col_start,col_end):
  global blues, whites
  is_same = True
  first = color_paper[row_start][col_start]
  for i in range(row_start,row_end):
    for j in range(col_start,col_end):
      if color_paper[i][j] != first:
        is_same = False
        break
    
  if is_same and first == 0:
    whites += 1
  elif is_same and first == 1:
    blues += 1
  elif not is_same and row_end - row_start == 2 :
    addtional_blues = 0
    addtional_blues += sum(color_paper[row_start][col_start:col_end])
    addtional_blues += sum(color_paper[row_end-1][col_start:col_end])
    additive_whites = 4 - addtional_blues
    blues += addtional_blues
    whites += additive_whites
  elif not is_same and row_end - row_start >= 4:
    width = (row_end - row_start)
    find_papers(row_start,row_start+width//2,col_start,col_start+width//2)
    find_papers(row_start,row_start+width//2,col_start+width//2,col_end)
    find_papers(row_start+width//2,row_end,col_start,col_start+width//2)
    find_papers(row_start+width//2,row_end,col_start+width//2,col_end)

find_papers(0,N,0,N)
print(whites)
print(blues)