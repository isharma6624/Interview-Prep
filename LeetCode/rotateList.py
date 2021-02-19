# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        if k == 0:
            return head
        # if head.next is None:
        #     return head
        tail = head
        size = 1
        
        while tail.next != None:
            tail = tail.next
            size += 1
            
        tail.next = head
        
        k %= size
        
        for i in range(1,size - k):
            head = head.next
        
        tail = head.next
        head.next = None
        return tail 
