# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        
        for head in lists:
            while(head!= None):
                heapq.heappush(heap,head.val)
                head = head.next
        
        
        new = ListNode(0)
        headnew = new
        
        while(heap != []):
            new.next = ListNode(heapq.heappop(heap))
            new = new.next
            
        return headnew.next
