# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        ntemp = n
        first = head
        second = head
        flag = False
     
        for i in range(n):
            first = first.next
        
        if first is None:
            return head.next
            
        while first.next != None:
            first=first.next
            second = second.next
            
        second.next = second.next.next
        return head   
