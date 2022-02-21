

import re


class Heap:
    def __init__(self, heap):
        self.max_heap = self.max_heap_sort(heap)
        
    def get_heap(self):
        return self.max_heap
    
    def max_heap_sort(self, heap):
        heap_sorted = []
        if len(heap) == 1:
            heap_sorted.extend(heap)
    
        heap = self.max_heapify(heap)
        
        while len(heap) > 0:
            heap = self.swap(heap, 0, -1)
            heap_sorted.append(heap.pop())
            heap = self.max_heapify(heap)
        return heap_sorted
    
    def max_heapify(self, heap):
        start_node = len(heap) // 2
        heap = [0] + heap
        for node in range(start_node, 0, -1):
            heap = self.heapify(heap, node)
        return heap[1:]
    
    def insert_node(self, additional_node):
        self.max_heap.append(additional_node)
        if len(self.max_heap) == 1:
            return
        
        def larger_than_parent_node(child_node, parent_node):
            if parent_node == 0:
                return False
            if self.max_heap[child_node] > self.max_heap[parent_node]:
                return True
            else:
                return False
            
        root_node = len(self.max_heap) // 2
        child_node = len(self.max_heap)
        self.max_heap = [0] + self.max_heap
        while larger_than_parent_node(child_node, root_node):
            self.max_heap = self.swap(self.max_heap, root_node, child_node)
            child_node = root_node
            root_node = root_node // 2
            
        self.max_heap = self.max_heap[1:]
            
    def delete_node(self):
        self.max_heap = self.swap(self.max_heap, 0, -1)
        deleted_node = self.max_heap.pop()
        self.max_heap = [0] + self.max_heap
        root_node = 1
        
        def smaller_than_child_node(parent_node):
            left_child = parent_node * 2
            right_child = parent_node * 2 + 1
            if self.max_heap[parent_node] < self.max_heap[left_child] or self.max_heap[parent_node] < self.max_heap[right_child]:
                return True
            else:
                return False
            
        while smaller_than_child_node(root_node):
            self.max_heap = self.heapify(self.max_heap, root_node)
            root_node, root_value = self.largest_node(self.max_heap, root_node)
        self.max_heap = self.max_heap[1:]
        
        return deleted_node
            
    def heapify(self, heap, start_node):
        largest_node, largest_value = self.largest_node(heap, start_node)
        
        if largest_value != heap[start_node]:
            heap = self.swap(heap, start_node, largest_node)
        return heap
    
    def largest_node(self, heap, start_node):
        root_node = start_node
        left_child = start_node * 2
        right_child = start_node * 2 + 1
        
        def both_child_not_exist():
            if left_child >= len(heap):
                return True
            else:
                return False
        
        def right_child_not_exist():
            if right_child >= len(heap):
                return True
            else:
                return False
            
        if both_child_not_exist():
            return (root_node, heap[root_node])
        elif right_child_not_exist():
            largest_value = max(heap[root_node], heap[left_child])
            largest_node = heap.index(largest_value, root_node, left_child+1)
        else:
            largest_value = max(heap[root_node], heap[left_child], heap[right_child])
            largest_node = heap.index(largest_value, root_node, right_child+1)
            
        return (largest_node, largest_value)
        
    def swap(self, heap, root_node, largest_node):
        heap[root_node], heap[largest_node] = heap[largest_node], heap[root_node]
        return heap
    
not_sorted = [4,2,3,5,6,10,7,11]
max_heap = Heap(not_sorted)
print(not_sorted, max_heap.get_heap(), sep='\n')

max_heap.insert_node(20)
print(max_heap.get_heap())

deleted_node = max_heap.delete_node()
print(deleted_node, max_heap.get_heap(), sep='\n')