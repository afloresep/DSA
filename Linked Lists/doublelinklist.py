# Double LInked List
class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node = Node(data)
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        # Add at the begginig
        if self.head is None:
            self.head = Node(data)

        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.data == key:
                new_node = Node(data)
                new_node.prev = cur
                new_node.next = cur.next
                cur.next = new_node

            cur = cur.next

 
    def add_before_node(self, key, data):
        new_node = Node(data)
        if self.head.data == key:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return
        cur = self.head
        prev = None

        while cur:
            if cur.data == key:
                cur.prev = new_node
                new_node.next = cur
                prev.next = new_node
                new_node.prev = prev
                
            prev = cur
            cur = cur.next

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if cur.next:
                    self.head = cur.next
                    self.head.prev = None
                    return
                # Deal with cases wheren head is the only node 
                else:
                    cur = None
                    self.head = None
                    return 
                    
            if cur.data == key:
                prev = cur.prev 
                if cur.next:
                    prev.next = cur.next
                    cur.next.prev = prev
                else:
                    prev.next = None
                return
            cur = cur.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        self.head = tmp.prev