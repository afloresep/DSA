### Implementation of various linked lists functions


class Node:
    def __init__(self, data) -> None:
       self.data = data 
       self.next = None

 
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        cur_dir = self.head
        while cur_dir.next:
            cur_dir = cur_dir.next
        cur_dir.next = new_node 

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node does not exist.")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def remove_index(self, index):
        cur_node = self.head
        if index==0:
            self.head = self.head.next
            return
        cur_pos = 0
        prev_node = self.head
        while cur_node.next:
            if cur_pos == index:
                prev_node.next = cur_node.next
                return
            prev_node = cur_node
            cur_node =cur_node.next
            cur_pos += 1
        prev_node.next= None


    def __len__(self):
        count = 1 
        cur = self.head
        while cur.next:
            count +=1
            cur = cur.next
        return count

    # Recursive implementation of length
    def len(self, node):
        if node is None:
            return 0 
        return 1 + self.len(node.next)
        
    def __repr__(self) -> str:
        cur_node = self.head        
        s = ''
        while cur_node:
           s = s+f'{cur_node.data}->' 
           cur_node = cur_node.next
        return s

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev1= None
        cur1 = self.head
        while cur1 and cur1.data != key_1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head
        while cur2 and cur2.data != key_2:
            prev2 = cur2
            cur2 = cur2.next 

        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2

        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1

        cur1.next, cur2.next = cur2.next, cur1.next

    def reverse_list(self):
        cur = self.head
        prev = None 
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next 
        self.head = prev


# Usage examples 
# llist = LinkedList()
# llist.append('A')
# llist.append('B')
# llist.append('C')
# llist.append('D')
# llist.remove_index(3)
# repr(llist) 
# llist.len(llist.head) 
# len(llist)