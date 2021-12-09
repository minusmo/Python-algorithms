from collections import deque

N = int(input())

a = [i for i in range(1, N+1)]
b = []
c = []

def hanoi(n,a,b,c):
     move = 0
     
     premove, preseq = hanoi(n-1,a,c,b)
     c.append(a.pop())
     inseq = ('a','c')
     postmove, postseq = hanoi(n-1,b,a,c)
     
     move += premove + 1 + postmove
     sequence =  preseq + postseq
     return (move, sequence)