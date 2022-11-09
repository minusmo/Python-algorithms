N,K = map(int, input().split())

sequence = [i for i in range(1,N+1)]
result = []
idx = 0
while len(result) != N:
    idx = (idx + K) % len(sequence) - 1
    if idx < 0:
        idx = idx + len(sequence)
    result.append(sequence[idx])
    sequence = sequence[:idx] + sequence[idx+1:]
    
print('<',', '.join([str(i) for i in result]),'>', sep='')