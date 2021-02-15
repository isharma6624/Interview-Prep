# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        new = ListNode(0)
        head = new
        
        while curr1 != None and curr2!= None:
            
            if curr1.val < curr2.val:
                new.next= curr1
                curr1 = curr1.next
            
            else:
                new.next = curr2
                curr2 = curr2.next
                
            new = new.next
        
        if curr1 != None:
            new.next = curr1
        
        else:
            new.next = curr2
            
        return head.next
