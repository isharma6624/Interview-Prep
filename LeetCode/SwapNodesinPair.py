# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        new = ListNode(0)
        new.next = head
        temp = new
       
        
        while temp.next!= None and temp.next.next!= None:
            firstNode = temp.next
            secondNode = temp.next.next
            
            firstNode.next = secondNode.next
            temp.next = secondNode
            temp.next.next = firstNode
            temp = temp.next.next
        
        return new.next
