"""
완전 이진 트리라고 가정.
완전 이진 트리를 배열로 구성 후,
전위, 중위, 후위 순회를 하는 함수를 작성.

"""

# 완전 이진 트리를 배열로 구성.

binary_tree = [None]

for i in range(0, 10):
	binary_tree.append(i)

print(binary_tree)

def pre_traversal(binary_tree, root_node_index):
	if binary_tree == None:
		print('root node is null')
	# 부모 노드 순회
	try:
		print(binary_tree[root_node_index])
	except:
		print('It is terminal node')
		return

	# 왼쪽 서브 트리 순회
	pre_traversal(binary_tree, 2 * root_node_index)
	# 오른쪽 서브 트리 순회
	pre_traversal(binary_tree, 2 * root_node_index + 1)

def in_traversal(binary_tree, root_node_index):
	if binary_tree == None:
		print('root node is null')

	# 왼쪽 서브 트리 순회
	if 2 * root_node_index >= len(binary_tree):
		print('no left child node found')
	else:
		in_traversal(binary_tree, 2 * root_node_index)

	# 부모 노드 순회
	try:
		print(binary_tree[root_node_index])
	except:
		print('It is terminal node')
		return

	# 오른쪽 서브 트리 순회
	if 2 * root_node_index + 1 >= len(binary_tree):
		print('no right child node found')
	else:
		in_traversal(binary_tree, 2 * root_node_index + 1)

def post_traversal(binary_tree, root_node_index):
	if binary_tree == None:
		print('root node is null')

	# 왼쪽 서브 트리 순회
	if 2 * root_node_index >= len(binary_tree):
		print('no left child node found')
	else:
		post_traversal(binary_tree, 2 * root_node_index)

	# 오른쪽 서브 트리 순회
	if 2 * root_node_index + 1 >= len(binary_tree):
		print('no right child node found')
	else:
		post_traversal(binary_tree, 2 * root_node_index + 1)

	# 부모 노드 순회
	try:
		print(binary_tree[root_node_index])
	except:
		print('It is terminal node')
		return


"""
트리 레벨 순회 
루트 노드의 레벨이 1이고 아래로 내려갈수록 증가한다.
동일한 레벨의 경우에는 좌에서 우로 방문한다.
큐를 사용한다.
큐에 하나라도 노드가 있으면 반복하고, 
먼저 큐에 있는 노드를 방문한 후, 
그 노드의 자식 노드를 큐에 삽입한다.  
"""

def level_traversal(binary_tree, root_node_index):
	if binary_tree == None:
		print('no root node is found')
		return
	queue = [root_node_index]

	while not len(queue) == 0:
		current_node_index = queue.pop(0)
		print(binary_tree[current_node_index])

		# 왼쪽 자식 노드가 존재하면 큐에 추가
		if 2 * current_node_index >= len(binary_tree):
			print('no left child node found')
		else:
			queue.append(2 * current_node_index)
		# 오른쪽 자식 노드가 존재하면 큐에 추가
		if 2 * current_node_index + 1 >= len(binary_tree):
			print('no right child node found')
		else:
			queue.append(2 * current_node_index + 1)

# 트리의 노드 개수 구하기

def get_node_counts(binary_tree, root_node_index):
	if binary_tree == None:
		print('no root node found')
		return
	count = 0

	if not root_node_index >= len(binary_tree):
		count = (1 + get_node_counts(binary_tree, 2 * root_node_index)
		+ get_node_counts(binary_tree, 2 * root_node_index + 1))

	return count

# 트리의 단말 노드 개수 구하기

def get_leaf_node_count(binary_tree, root_node_index):
	if binary_tree == None:
		print('no root node found')
		return
	count = 0
	if (2 * root_node_index >= len(binary_tree) - 1) and (2 * root_node_index + 1 >= len(binary_tree) - 1):
		return 1
	else:
		count = get_leaf_node_count(binary_tree, 2 * root_node_index) + get_leaf_node_count(binary_tree, 2 * root_node_index + 1)
	return count

"""
트리의 높이 구하기
각 서브트리에 대하여 순환 호출을 한후,
각 서브트리의 높이 중 최대값을 구하여 리턴한다.
"""

def get_tree_height(binary_tree, root_node_index):
	if binary_tree == None:
		print('no root node found')
		return
	height = 0
	if not root_node_index >= len(binary_tree):
		height = 1 + max(get_tree_height(binary_tree, 2 * root_node_index), get_tree_height(binary_tree, 2 * root_node_index + 1))
	return height

print(get_tree_height(binary_tree, 1))