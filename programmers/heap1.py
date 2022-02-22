import heapq

def solution(scoville, K):
    min_mixes_to_over_k = 0
    min_mixes_to_over_k = get_min_mixes(scoville, K)
    return min_mixes_to_over_k

def get_min_mixes(scoville, K):
    min_mixes_to_over_k = 0
    scovilles = heapsort(scoville)
    
    while not every_scoville_over_k(scovilles, K):
        try:
            mildest = heapq.heappop(scovilles)
            second_mildest = heapq.heappop(scovilles)
            mixed_scoville = mix_scoville(mildest, second_mildest)
            min_mixes_to_over_k += 1
            heapq.heappush(scovilles, mixed_scoville)
        except:
            return -1
        
    return min_mixes_to_over_k

def heapsort(scovilles):
    heap = []
    for scoville in scovilles:
        heapq.heappush(heap, scoville)
    return [heapq.heappop(heap) for i in range(len(heap))]

def every_scoville_over_k(scovilles, K):
    over_k = True
    mildest = scovilles[0]
    if mildest < K:
        over_k = False
    return over_k

def mix_scoville(mildest, second_mildest):
    return mildest + second_mildest * 2