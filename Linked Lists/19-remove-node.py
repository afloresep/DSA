from typing import Optional 

# 19. Remove Nth Node from End of List 
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Get input length 
        count = 0 
        count_list = head
        while count_list: 
            count = count + 1
            count_list= count_list.next

        dummy_head = ListNode(head.val)
        current = dummy_head 

        del_position = count - n

        # Creata a new linked list skipping the n-th position
        for i in range(count):
            if i == del_position:
                head = head.next
            else:
                current.next = ListNode(head.val)
                current = current.next
                head = head.next

        return dummy_head.next