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


    def merge_sorted_list(self, list2):
        p, q, s = self.head, list2.head, None

        # decide where to start
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
                
        # define head as the minimun number between the two heads
        self.head = s

        while p and q:
            if p.data <= q.data:
                # point previous to next number
                s.next = p
                # move s pointer to p
                s = p
                # move p to next number
                p = s.next
            # Samething 
            else:
                s.next = q
                s = q
                q = s.next 

        # if it is empty then continue on the pointer on the other branch
        if not q: s.next =p 
        if not p: s.next = q 

    def remove_duplicates(self):
        items = []
        cur = self.head
        prev = None
        while cur:
            if cur.data not in items:
                items.append(cur.data)
                prev = cur
                cur.next = cur.next
                cur = cur.next
            else:
                prev.next = cur.next
                cur =cur.next

    def get_node_index(self, idx):
        count = 0
        cur = self.head 
        while cur:
            
            if count == idx:
                return cur.data
            else:
                count +=1
                cur = cur.next 
        return None

    def count_occurences(self, data):
       count = 0
       cur = self.head
       while cur:
           if cur.data == str(data):
               count+=1
           cur = cur.next 
       return count

    def rotate(self, data):
        cur = self.head
        new_end = None
        while cur.next:
          if cur.data == data:
            new_end = cur
          cur = cur.next

        if new_end is None:
            # if data is not found then return list as it is
            return
        else:
            cur.next = self.head
            self.head = new_end.next 
            new_end.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = None 

    def prepend(self, data):
        #   "Add at the beggining (head)"
        new_node = Node(data)
        cur = self.head 
        new_node.next = self.head

        while cur.next != self.head:
            cur = cur.next

        cur.next = new_node
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        # Add at the end (tail)
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head

        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            new_node = Node(data) 
            cur.next = new_node
            new_node.next = self.head
            
    def print_list(self):
        cur = self.head 

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head 
                while cur.next != self.head:
                    cur = cur.next 
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head 
                prev = None 
                while cur.next != self.head:
                    prev = cur 
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next 
                        cur = cur.next

    def __len__(self):
        cur = self.head
        length = 1
        while cur.next != self.head:
            length += 1 
            cur = cur.next
        return length

    def split_in_half(self):
        lenght = len(self)
        assert lenght % 2==0, 'Lenght is not even'
        cur = self.head
        count = int(1)
        while  count != int(lenght/2):
            cur = cur.next
            count += 1
        head_list_2 = cur.next
        cur.next = self.head
        cur = head_list_2
        print('List 1')
        self.print_list()
        while count != (lenght - 1):
            cur = cur.next 
            count += 1

        cur.next = head_list_2
        self.head = head_list_2
        print('List 2')
        self.print_list()