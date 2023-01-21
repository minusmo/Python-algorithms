import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
binary_tree = defaultdict(defaultdict)
for _ in range(N):
  p, l, r = input().split()
  binary_tree[p]['left'] = l
  binary_tree[p]['right'] = r

pre_order = []
in_order = []
post_order = []

root = 'A'

def pre_traveral(root_node):
  if root_node == '.':
    return
  pre_order.append(root_node)
  pre_traveral(binary_tree[root_node]['left'])
  pre_traveral(binary_tree[root_node]['right'])
  
def in_traveral(root_node):
  if root_node == '.':
    return
  in_traveral(binary_tree[root_node]['left'])
  in_order.append(root_node)
  in_traveral(binary_tree[root_node]['right'])
  
def post_traveral(root_node):
  if root_node == '.':
    return
  post_traveral(binary_tree[root_node]['left'])
  post_traveral(binary_tree[root_node]['right'])
  post_order.append(root_node)
  
pre_traveral(root)
in_traveral(root)
post_traveral(root)

print(*pre_order,sep='')
print(*in_order,sep='')
print(*post_order,sep='')