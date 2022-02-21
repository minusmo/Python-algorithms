def solution(scoville, K):
    min_mixes_to_over_k = 0
    min_mixes_to_over_k = get_min_mixes(scoville, K)
    return min_mixes_to_over_k

def get_min_mixes(scoville, K):
    min_mixes_to_over_k = -1
    
    return min_mixes_to_over_k
def mixed_scoville(mildest, second_mildest):
    return mildest + second_mildest * 2

def min_heap_sort(heap):
    if len(heap) == 2:
        return heap
    for node in range(2, len(heap)+1):
        