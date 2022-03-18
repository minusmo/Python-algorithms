#이진 탐색 트리는 힙(완전 이진 트리)이 아니다!!

numbers = [9,11,2,34,100,29,46,28]

class BST:
    def __init__(self, numbers):
        self.root_node = None
        self.make_bst(numbers)
        
    def make_bst(self, numbers):
        for number in numbers:
            self.insert_node(number)
            
    def insert_node(self, number):
        if self.root_node == None:
            self.root_node = Node(number)
        else:
            current_node = self.root_node
            while current_node != None:
                print(current_node.value, number, sep=' // ')
                if number <= current_node.value:
                    if current_node.left == None:
                        current_node.left = Node(number)
                        current_node = None
                        break
                    else:
                        current_node = current_node.left
                        continue
                else:
                    if current_node.right == None:
                        current_node.right = Node(number)
                        current_node = None
                        break
                    else:
                        current_node = current_node.right
                        continue
                    
    def search_node(self, value):
        if self.root_node == None:
            return None
        else:
            current_node = self.root_node
            while current_node != None:
                if current_node.value == value:
                    return current_node
                elif current_node.value > value:
                    current_node = current_node.left
                    continue
                else:
                    current_node = current_node.right
                    continue
            return None
                    
class Node:
    def __init__(self, number):
        self.value = number
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"

bst = BST(numbers)
print(bst.search_node(46))