class Stack(object):
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1].value

    def __len__(self):
        return len(self.items)
    def pop(self):
        return self.items.pop()
    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

class Queue(object):
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop()

    def __len__(self):
        return len(self.items)

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1].value
        
class Node:
    def __init__(self, root) -> None:
        self.value= root
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value) -> None:
        self.root = Node(value)

    def preorder_print(self, start, traversal=''):
        if start:
            traversal += (str(start.value)+ '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal 

    def inorder_print(self, start, traversal=''):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value)+ '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal 

    def postorder_print(self, start, traversal=''):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value)+ '-')
        return traversal 


    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def levelorder_print(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal:str = ''

        while len(queue) > 0 :
            traversal += str(queue.peek()) + '-'
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right) 

        return traversal
    
    def reverse_levelorder_print(self, start):
        if start is None:
            return 

        stack = Stack()
        queue = Queue()
        queue.enqueue(start)
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right) 
            if node.left:
                queue.enqueue(node.left) 
        traversal = ''
        while len(stack) > 0: 
            node = stack.pop()
            traversal += str(node.value) + '-'
        return traversal 

        