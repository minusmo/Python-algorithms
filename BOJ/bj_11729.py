N = int(input())

a = [1]+[i for i in range(N,0,-1)]
b = [2]
c = [3]

def hanoi(n,one,two,three):
    if n == 1:
        three.append(one.pop())
        return (1, [f"{one[0]} {three[0]}"])
    
    move = 0
    
    premove, preseq = hanoi(n-1,one,three,two)
    three.append(one.pop())
    inseq = f"{one[0]} {three[0]}"
    postmove, postseq = hanoi(n-1,two,one,three)
    
    move += premove + 1 + postmove
    sequence = preseq + [inseq] + postseq
    return (move, sequence)

move, seq = hanoi(N,a,b,c)
print(move)

for mov in seq:
    print(mov)